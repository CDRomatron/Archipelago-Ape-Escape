import sys
import logging
import time
import Utils
from typing import TYPE_CHECKING, Optional, Dict, Set, ClassVar, Any, Tuple
from Options import Toggle
from NetUtils import ClientStatus
from worlds.oot.Patches import get_override_table_bytes
from .Packs import *
from .Options import InstantCardOption, CardSanityOption, WinsEachOption
from .Strings import gamename

# TODO: REMOVE ASAP - Borrowed from MM2
# This imports the bizhawk apworld if it's not already imported. This code block should be removed for a PR.
if "worlds._bizhawk" not in sys.modules:
    import importlib
    import os
    import zipimport

    bh_apworld_path = os.path.join(os.path.dirname(sys.modules["worlds"].__file__), "_bizhawk.apworld")
    if os.path.isfile(bh_apworld_path):
        importer = zipimport.zipimporter(bh_apworld_path)
        spec = importer.find_spec(os.path.basename(bh_apworld_path).rsplit(".", 1)[0])
        mod = importlib.util.module_from_spec(spec)
        mod.__package__ = f"worlds.{mod.__package__}"
        mod.__name__ = f"worlds.{mod.__name__}"
        sys.modules[mod.__name__] = mod
        importer.exec_module(mod)
    elif not os.path.isdir(os.path.splitext(bh_apworld_path)[0]):
        logging.error("Did not find _bizhawk.apworld required to play Ape Escape.")

import worlds._bizhawk as bizhawk
from worlds._bizhawk.client import BizHawkClient

if TYPE_CHECKING:
    from worlds._bizhawk.context import BizHawkClientContext
else:
    BizHawkClientContext = object


class YuGiOhGXClient(BizHawkClient):
    game = gamename
    system = "GBA"
    local_checked_locations: Set[int]
    local_set_events: Dict[str, bool]
    local_found_key_items: Dict[str, bool]
    goal_flag: int
    local_wins = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    local_dp_count = 0

    win_addresses = [
        0x4cfc,  # Jaden
        0x4d08,  # Syrus
        0x4d14,  # Chumley
        0x4d5c,  # Banner
        0x4de0,  # Blair
        0x4dec,  # Gerard
        0x4d20,  # Bastion
        0x4d98,  # Brier
        0x4da4,  # Beauregard
        0x4db0,  # Dimitri
        0x4d74,  # Sartyr
        0x4d2c,  # Alexis
        0x4d38,  # Chazz
        0x4dc8,  # Torrey
        0x4dbc,  # Damon
        0x4d68,  # Fontaine
        0x4d50,  # Crowler
        0x4d44  # Zane
    ]

    combined_wram = "Combined WRAM"

    offset = 129000000

    def __init__(self) -> None:
        super().__init__()
        self.local_checked_locations = set()
        self.local_set_events = {}
        self.local_found_key_items = {}
        local_wins = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    def initialize_client(self):
        self.pending_death_link: bool = False

    async def validate_rom(self, ctx: BizHawkClientContext) -> bool:
        from CommonClient import logger
        ygogx_rom_identifier_address: int = 0xA0
        bytes_expected: bytes = bytes.fromhex("595547494F484758444100004259474541349600")
        try:
            bytes_actual: bytes = \
                (await bizhawk.read(ctx.bizhawk_ctx, [(ygogx_rom_identifier_address, len(bytes_expected), "ROM")]))[0]
            if bytes_expected != bytes_actual:
                return False
        except Exception:
            return False

        if not self.game == gamename:
            return False
        ctx.game = self.game
        ctx.items_handling = 0b111
        ctx.want_slot_data = True
        ctx.watcher_timeout = 0.125

        self.initialize_client()
        return True

    def on_package(self, ctx: "BizHawkClientContext", cmd: str, args: Dict[str, Any]) -> None:
        if cmd == "Bounced":
            if "tags" in args:
                assert ctx.slot is not None
                if "DeathLink" in args["tags"] and args["data"]["source"] != ctx.slot_info[ctx.slot].name:
                    self.on_deathlink(ctx)

    async def set_auth(self, ctx: BizHawkClientContext) -> None:
        x = 3

    async def game_watcher(self, ctx: BizHawkClientContext) -> None:
        # Detects if the AP connection is made.
        # If not,"return" immediately to not send anything while not connected
        if ctx.server is None or ctx.server.socket.closed or ctx.slot_data is None or ctx.auth is None:
            self.initClient = False
            return
        # Detection for triggering "initialise_client()" when Disconnecting/Reconnecting to AP (only once per connection)
        if self.initClient == False:
            self.initClient = True
            self.initialize_client()

        try:
            # Read the number of wins from the game, send those locations to the server
            winReads = []
            for x in range(18):
                winReads.append((self.win_addresses[x], 2, self.combined_wram))
            reads = await bizhawk.read(ctx.bizhawk_ctx, winReads)

            wins = []

            for read in reads:
                wins.append(int.from_bytes(read, byteorder="little"))

            winsToSend = set()

            for x in range(18):
                if wins[x] != self.local_wins[x]:
                    if wins[x] < 11:
                        for y in range(wins[x]):
                            winsToSend.add(1001 + y + self.offset + (x * 10))

                    if 10 > wins[x] >= ctx.slot_data["wins"]:
                        wins[x] = 10

            if winsToSend is not None and winsToSend != set():
                await ctx.send_msgs([{
                    "cmd": "LocationChecks",
                    "locations": list(x for x in winsToSend)
                }])

            # Performing additional reads here
            extraReads = await bizhawk.read(ctx.bizhawk_ctx,
                                            [(0x4cf0, 2, self.combined_wram),
                                             (0x4cf2, 2, self.combined_wram),
                                             (0x3848, 2, self.combined_wram),
                                             (0x01d8, 1, self.combined_wram),
                                             (0x4ce8, 1, self.combined_wram),
                                             (0x4d64, 2, self.combined_wram)])
            winNumber = int.from_bytes(extraReads[0], byteorder="little")
            lossNumber = int.from_bytes(extraReads[1], byteorder="little")
            duelPoints = int.from_bytes(extraReads[2], byteorder="little")
            redEyesNumber = int.from_bytes(extraReads[3], byteorder="little")
            rank = int.from_bytes(extraReads[4], byteorder="little")
            shepard_wins = int.from_bytes(extraReads[5], byteorder="little")
            dp_count = 0

            # King of Games is 68, plus 0 for Red, 1 for Yellow, and 2 for Blue
            if rank == 68 or rank == 69 or rank == 70:
                await ctx.send_msgs([{
                    "cmd": "LocationChecks",
                    "locations": list(x for x in [129000000])
                }])
                await ctx.send_msgs([{
                    "cmd": "StatusUpdate",
                    "status": ClientStatus.CLIENT_GOAL
                }])

            # An array, of arrays, containing every card id in the pack
            packsFromItems = []

            # An array of every item, after removing the offset
            keyItems = []

            # An array of items ids, but only the cards for cardsanity
            cardsanitycards = []
            for item in ctx.items_received:
                if 1 <= item.item - self.offset <= 48:
                    packsFromItems.append(allPacks[item.item - self.offset - 1])
                elif ctx.slot_data["cardsanity"] == CardSanityOption.option_true \
                        and 10001 <= item.item - self.offset <= 11200:
                    cardsanitycards.append(item.item - self.offset - 10000)
                elif item.item - self.offset == 100:
                    dp_count += 1
                keyItems.append(item.item - self.offset)

            # Writing the cards to the inventory depending on settings.
            # Red-Eyes is used to check if starting inventory is set.
            writes = []
            if ctx.slot_data["instant"] == InstantCardOption.option_true \
                    and ctx.slot_data["cardsanity"] == CardSanityOption.option_false:
                writes += self.cardWrites(packsFromItems)
            elif ctx.slot_data["cardsanity"] == CardSanityOption.option_true:
                writes += self.cardWrites([cardsanitycards])
            elif redEyesNumber == 0x0A:
                writes += self.cardWrites([])

            # Add DP from items
            if dp_count > shepard_wins and dp_count > self.local_dp_count:
                new_dp = duelPoints + (1000 * (dp_count - shepard_wins))
                self.local_dp_count = dp_count
                writes.append((0x3848, new_dp.to_bytes(2, "little"), self.combined_wram))

            # Unlocked packed as saved across 6 bytes
            unlockedPacks = [0, 0, 0, 0, 0, 0]
            for x in range(48):
                if x + 1 in keyItems:
                    writes.append((0x4c08 + (x * 4), 0xC6.to_bytes(1, "little"), self.combined_wram))
                    if x + 1 >= 1 and x + 1 <= 8:
                        unlockedPacks[0] += pow(2, x % 8)
                    elif x + 1 >= 9 and x + 1 <= 16:
                        unlockedPacks[1] += pow(2, x % 8)
                    elif x + 1 >= 17 and x + 1 <= 24:
                        unlockedPacks[2] += pow(2, x % 8)
                    elif x + 1 >= 25 and x + 1 <= 32:
                        unlockedPacks[3] += pow(2, x % 8)
                    elif x + 1 >= 31 and x + 1 <= 40:
                        unlockedPacks[4] += pow(2, x % 8)
                    elif x + 1 >= 41 and x + 1 <= 48:
                        unlockedPacks[5] += pow(2, x % 8)
                else:
                    writes.append((0x4c08 + (x * 4), 0x00.to_bytes(1, "little"), self.combined_wram))

            # If player has the Strength Key Item, give 200 wins, unless the player has over 200 wins already.
            if 102 in keyItems and winNumber < 200:
                writes.append((0x4cf0, 0xc8.to_bytes(1, "little"), self.combined_wram))

            # If player has Cunning Key Item, set all timed duels to be complete, otherwise set all to be incomplete.
            timed = 0
            if 103 in keyItems:
                timed = 7
            for x in range(100):
                writes.append((0x5e44 + (x * 4), timed.to_bytes(1, "little"), self.combined_wram))

            # If player has the Knowledge Key Item, set all written questions to complete, otherwise set all to be
            # incomplete.
            written = 0
            if 104 in keyItems:
                written = 3
            for x in range(200):
                writes.append((0x5b24 + (x * 4), written.to_bytes(1, "little"), self.combined_wram))

            # Each duelist needs to be beaten ten times, however, if another option is chosen, we'll need to set it to
            # ten if the number matches the option number. This is set to ten when reading for the locations, and
            # written here.
            winWrites = []

            if wins[0] > self.local_wins[0]:
                winWrites.append((self.win_addresses[0], wins[0].to_bytes(1, "little"), self.combined_wram))
            if wins[1] > self.local_wins[1]:
                winWrites.append((self.win_addresses[1], wins[1].to_bytes(1, "little"), self.combined_wram))  # Syrus
            if wins[2] > self.local_wins[2]:
                winWrites.append((self.win_addresses[2], wins[2].to_bytes(1, "little"), self.combined_wram))  # Chumley
            if wins[3] > self.local_wins[3]:
                winWrites.append((self.win_addresses[3], wins[3].to_bytes(1, "little"), self.combined_wram))  # Banner
            if wins[4] > self.local_wins[4]:
                winWrites.append((self.win_addresses[4], wins[4].to_bytes(1, "little"), self.combined_wram))  # Blair
            if wins[5] > self.local_wins[5]:
                winWrites.append((self.win_addresses[5], wins[5].to_bytes(1, "little"), self.combined_wram))  # Gerard
            if wins[6] > self.local_wins[6]:
                winWrites.append((self.win_addresses[6], wins[6].to_bytes(1, "little"), self.combined_wram))  # Bastion
            if wins[7] > self.local_wins[7]:
                winWrites.append((self.win_addresses[7], wins[7].to_bytes(1, "little"), self.combined_wram))  # Brier
            if wins[8] > self.local_wins[8]:
                winWrites.append(
                    (self.win_addresses[8], wins[8].to_bytes(1, "little"), self.combined_wram))  # Beauregard
            if wins[9] > self.local_wins[9]:
                winWrites.append((self.win_addresses[9], wins[9].to_bytes(1, "little"), self.combined_wram))  # Dimitri
            if wins[10] > self.local_wins[10]:
                winWrites.append((self.win_addresses[10], wins[10].to_bytes(1, "little"), self.combined_wram))  # Sartyr
            if wins[11] > self.local_wins[11]:
                winWrites.append((self.win_addresses[11], wins[11].to_bytes(1, "little"), self.combined_wram))  # Alexis
            if wins[12] > self.local_wins[12]:
                winWrites.append((self.win_addresses[12], wins[12].to_bytes(1, "little"), self.combined_wram))  # Chazz
            if wins[13] > self.local_wins[13]:
                winWrites.append((self.win_addresses[13], wins[13].to_bytes(1, "little"), self.combined_wram))  # Torrey
            if wins[14] > self.local_wins[14]:
                winWrites.append((self.win_addresses[14], wins[14].to_bytes(1, "little"), self.combined_wram))  # Damon
            if wins[15] > self.local_wins[15]:
                winWrites.append(
                    (self.win_addresses[15], wins[15].to_bytes(1, "little"), self.combined_wram))  # Fontaine
            if wins[16] > self.local_wins[16]:
                winWrites.append(
                    (self.win_addresses[16], wins[16].to_bytes(1, "little"), self.combined_wram))  # Crowler
            if wins[17] > self.local_wins[17]:
                winWrites.append((self.win_addresses[17], wins[17].to_bytes(1, "little"), self.combined_wram))  # Zane

            # Update the unlocked packs states, based on items
            writes.append((0x3B5A8, unlockedPacks[0].to_bytes(1, "little"), self.combined_wram))
            writes.append((0x3B5A9, unlockedPacks[1].to_bytes(1, "little"), self.combined_wram))
            writes.append((0x3B5AA, unlockedPacks[2].to_bytes(1, "little"), self.combined_wram))
            writes.append((0x3B5AB, unlockedPacks[3].to_bytes(1, "little"), self.combined_wram))
            writes.append((0x3B5AC, unlockedPacks[4].to_bytes(1, "little"), self.combined_wram))
            writes.append((0x3B5AD, unlockedPacks[5].to_bytes(1, "little"), self.combined_wram))

            # Write number of received dp to shepard wins, as it's unused here.
            writes.append((0x4d64, dp_count.to_bytes(2, "little"), self.combined_wram))

            writes.extend(winWrites)
            await bizhawk.write(ctx.bizhawk_ctx, writes)

            # Update the locally stored wins, to later see if wins are needing sent.
            self.local_wins = wins

            # POSSILBLE BUG HERE!!! FIRST CARD MIGHT STAY SAME BETWEEN TWO PACKS!!! ALSO LAST LOOKED AT CARD IN INV MIGHT BE FOIL IF SORTED!!!
            # Cardsanity only section.
            if ctx.slot_data["cardsanity"] == CardSanityOption.option_true:
                pack_location = 0xBBB0
                # Check the first card in the inventory, to check A: if the card is different from previous, and B:
                # if the card has a special modifier. Also, additional check for location, 40 being shop.
                shop_bytes = await bizhawk.read(ctx.bizhawk_ctx, [(0x6190, 1, self.combined_wram),
                                                                        (0x2B130, 1, self.combined_wram)])

                forty_in_shop = int.from_bytes(shop_bytes[0], byteorder="little")
                selection_state = int.from_bytes(shop_bytes[1], byteorder="little")
                if (selection_state == 0x16 or selection_state == 0x13) and forty_in_shop == 0x40:
                    cards_in_pack = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]

                    # Loop while the 10th read card is not empty, or is the first run through.
                    while cards_in_pack[9] != 0:
                        cards_to_send = set()
                        pack_read_tuples = [
                            (pack_location + 0, 2, self.combined_wram),
                            (pack_location + 4, 2, self.combined_wram),
                            (pack_location + 8, 2, self.combined_wram),
                            (pack_location + 12, 2, self.combined_wram),
                            (pack_location + 16, 2, self.combined_wram),
                            (pack_location + 20, 2, self.combined_wram),
                            (pack_location + 24, 2, self.combined_wram),
                            (pack_location + 28, 2, self.combined_wram),
                            (pack_location + 32, 2, self.combined_wram),
                            (pack_location + 36, 2, self.combined_wram)
                        ]

                        pack_bytes = await bizhawk.read(ctx.bizhawk_ctx, pack_read_tuples)

                        # For each card, keep taking away 2048 to get the ID. Then add offset to send as location.
                        for x in range(10):
                            cards_in_pack[x] = int.from_bytes(pack_bytes[x], byteorder="little")
                            while cards_in_pack[x] > 2048:
                                cards_in_pack[x] -= 2048
                            if cards_in_pack[x] != 0:
                                cards_to_send.add(cards_in_pack[x] + 10000 + self.offset)

                        if cards_to_send is not None and cards_to_send != set():
                            await ctx.send_msgs([{
                                "cmd": "LocationChecks",
                                "locations": list(x for x in cards_to_send)
                            }])
                        pack_location += 40

        except bizhawk.RequestFailedError:
            # Exit handler and return to main loop to reconnect
            pass

    def cardWrites(self, packsFromItems):
        out = []
        cardlist = []
        cardlist.extend(starterDeck)
        for pack in packsFromItems:
            cardlist.extend(pack)
        for x in range(1200):
            val = 0x0
            if (x + 1) in cardlist:
                val = 0x1A
            cardTuple = (0x4 + (x * 12), val.to_bytes(1, "little"), self.combined_wram)
            out.append(cardTuple)
        return out
