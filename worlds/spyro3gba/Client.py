import math
import sys
import logging
import time
import Utils
from typing import TYPE_CHECKING, Optional, Dict, Set, ClassVar, Any, Tuple
from Options import Toggle
from NetUtils import ClientStatus
from .Constants import gamename

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
        logging.error("Did not find _bizhawk.apworld required to play Spyro: Attack of the Rhynocs.")

import worlds._bizhawk as bizhawk
from worlds._bizhawk.client import BizHawkClient

if TYPE_CHECKING:
    from worlds._bizhawk.context import BizHawkClientContext
else:
    BizHawkClientContext = object


class Spyro3GBAClient(BizHawkClient):
    game = gamename
    system = "GBA"
    local_checked_locations: Set[int]
    local_set_events: Dict[str, bool]
    local_found_key_items: Dict[str, bool]
    goal_flag: int

    combined_wram = "Combined WRAM"

    offset = 126000000

    def __init__(self) -> None:
        super().__init__()
        self.local_checked_locations = set()
        self.local_set_events = {}
        self.local_found_key_items = {}

    def initialize_client(self):
        self.pending_death_link: bool = False

    async def validate_rom(self, ctx: BizHawkClientContext) -> bool:
        from CommonClient import logger
        spyro3_rom_identifier_address: int = 0xAC
        bytes_expected: bytes = bytes.fromhex("414F57453744")
        try:
            bytes_actual: bytes = \
                (await bizhawk.read(ctx.bizhawk_ctx, [(spyro3_rom_identifier_address, len(bytes_expected), "ROM")]))[0]
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
            item_reads = []
            for x in range(13):
                item_reads.append((0x2fe7+x, 1, "IWRAM"))
                #item_reads.append((0x7000+x, 1, "IWRAM"))
            item_reads.append((0x5D38, 1, "IWRAM"))

            reads = await bizhawk.read(ctx.bizhawk_ctx, item_reads)

            currentLevel = int.from_bytes(reads[13], byteorder="little")

            item_in_inventory = set()
            #item_to_send = set()
            locations_to_send = set()

            for x in range(13):
                if x != 12:
                    for y in range(8):
                        from_bytes = int.from_bytes(reads[x], byteorder="little")
                        power = pow(2,y)
                        if from_bytes & power:
                            item_in_inventory.add(0x43 + y + (x*8))
                else:
                    for y in range(4):
                        if int.from_bytes(reads[x], byteorder="little") & pow(2,y):
                            item_in_inventory.add(0x43 + y + (x*8))

            for x in item_in_inventory:
                # A
                if x == 0x4E:
                    if currentLevel == 4:
                        locations_to_send.add(0x45 + self.offset)
                    elif currentLevel == 9:
                        locations_to_send.add(0x48 + self.offset)
                    elif currentLevel == 14:
                        locations_to_send.add(0x4D + self.offset)
                    elif currentLevel == 15:
                        locations_to_send.add(0x4E + self.offset)
                    elif currentLevel == 20:
                        locations_to_send.add(0x56 + self.offset)
                    elif currentLevel == 31:
                        locations_to_send.add(0x5D + self.offset)
                    elif currentLevel == 35:
                        locations_to_send.add(0x64 + self.offset)
                    elif currentLevel == 36:
                        locations_to_send.add(0x65 + self.offset)
                    elif currentLevel == 37:
                        locations_to_send.add(0x66 + self.offset)
                    elif currentLevel == 42:
                        locations_to_send.add(0x6C + self.offset)
                    elif currentLevel == 47:
                        locations_to_send.add(0x76 + self.offset)
                    elif currentLevel == 51:
                        locations_to_send.add(0x7D + self.offset)
                    elif currentLevel == 52:
                        locations_to_send.add(0x7E + self.offset)
                    elif currentLevel == 57:
                        locations_to_send.add(0x85 + self.offset)
                    elif currentLevel == 63:
                        locations_to_send.add(0x8D + self.offset)
                    elif currentLevel == 64:
                        locations_to_send.add(0x8E + self.offset)
                    elif currentLevel == 3:
                        locations_to_send.add(0x94 + self.offset)
                    elif currentLevel == 72:
                        locations_to_send.add(0x9C + self.offset)
                    elif currentLevel == 73:
                        locations_to_send.add(0x9D + self.offset)
                # B
                elif x == 0x56:
                    if currentLevel == 4:
                        locations_to_send.add(0x46 + self.offset)
                    elif currentLevel == 15:
                        locations_to_send.add(0x4F + self.offset)
                    elif currentLevel == 31:
                        locations_to_send.add(0x5E + self.offset)
                    elif currentLevel == 36:
                        locations_to_send.add(0x68 + self.offset)
                    elif currentLevel == 42:
                        locations_to_send.add(0x6D + self.offset)
                    elif currentLevel == 47:
                        locations_to_send.add(0x77 + self.offset)
                    elif currentLevel == 52:
                        locations_to_send.add(0x7F + self.offset)
                    elif currentLevel == 57:
                        locations_to_send.add(0x86 + self.offset)
                    elif currentLevel == 64:
                        locations_to_send.add(0x8F + self.offset)
                # C
                elif x == 0x5D:
                    if currentLevel == 4:
                        locations_to_send.add(0x4A + self.offset)
                    elif currentLevel == 31:
                        locations_to_send.add(0x60 + self.offset)
                    elif currentLevel == 36:
                        locations_to_send.add(0x6A + self.offset)
                    elif currentLevel == 42:
                        locations_to_send.add(0x6F + self.offset)
                    elif currentLevel == 64:
                        locations_to_send.add(0x90 + self.offset)
                # D
                elif x == 0x6D:
                    if currentLevel == 64:
                        locations_to_send.add(0x92 + self.offset)
                # E
                elif x == 0x76:
                    if currentLevel == 6:
                        locations_to_send.add(0x43 + self.offset)
                    elif currentLevel == 18:
                        locations_to_send.add(0x50 + self.offset)
                    elif currentLevel == 29:
                        locations_to_send.add(0x57 + self.offset)
                    elif currentLevel == 20:
                        locations_to_send.add(0x53 + self.offset)
                    elif currentLevel == 27:
                        locations_to_send.add(0x58 + self.offset)
                    elif currentLevel == 31:
                        locations_to_send.add(0x5B + self.offset)
                    elif currentLevel == 33:
                        locations_to_send.add(0x5F + self.offset)
                    elif currentLevel == 39:
                        locations_to_send.add(0x67 + self.offset)
                    elif currentLevel == 44:
                        locations_to_send.add(0x6E + self.offset)
                    elif currentLevel == 47:
                        locations_to_send.add(0x74 + self.offset)
                    elif currentLevel == 50:
                        locations_to_send.add(0x78 + self.offset)
                    elif currentLevel == 52:
                        locations_to_send.add(0x7C + self.offset)
                    elif currentLevel == 56:
                        locations_to_send.add(0x81 + self.offset)
                    elif currentLevel == 59:
                        locations_to_send.add(0x83 + self.offset)
                    elif currentLevel == 61:
                        locations_to_send.add(0x88 + self.offset)
                    elif currentLevel == 64:
                        locations_to_send.add(0x8C + self.offset)
                    elif currentLevel == 69:
                        locations_to_send.add(0x98 + self.offset)
                    elif currentLevel == 81:
                        locations_to_send.add(0xA1 + self.offset)
                # F
                elif x == 0x7E:
                    if currentLevel == 8:
                        locations_to_send.add(0x49 + self.offset)
                    elif currentLevel == 31:
                        locations_to_send.add(0x61 + self.offset)
                    elif currentLevel == 36:
                        locations_to_send.add(0x69 + self.offset)
                    elif currentLevel == 47:
                        locations_to_send.add(0x7A + self.offset)
                    elif currentLevel == 59:
                        locations_to_send.add(0x8A + self.offset)
                    elif currentLevel == 64:
                        locations_to_send.add(0x91 + self.offset)
                    elif currentLevel == 73:
                        locations_to_send.add(0x9E + self.offset)
                    elif currentLevel == 77:
                        locations_to_send.add(0xA2 + self.offset)
                # G
                elif x == 0x86:
                    if currentLevel == 15:
                        locations_to_send.add(0x52 + self.offset)
                    elif currentLevel == 20:
                        locations_to_send.add(0x55 + self.offset)
                    elif currentLevel == 34:
                        locations_to_send.add(0x62 + self.offset)
                    elif currentLevel == 42:
                        locations_to_send.add(0x70 + self.offset)
                    elif currentLevel == 47:
                        locations_to_send.add(0x79 + self.offset)
                    elif currentLevel == 52:
                        locations_to_send.add(0x82 + self.offset)
                    elif currentLevel == 68:
                        locations_to_send.add(0x99 + self.offset)
                # H
                elif x == 0x8E:
                    if currentLevel == 20:
                        locations_to_send.add(0x59 + self.offset)
                    elif currentLevel == 42:
                        locations_to_send.add(0x71 + self.offset)
                    elif currentLevel == 68:
                        locations_to_send.add(0x9A + self.offset)
                # I
                elif x == 0xA6:
                    if currentLevel == 8:
                        locations_to_send.add(0x44 + self.offset)
                    elif currentLevel == 15:
                        locations_to_send.add(0x4B + self.offset)
                    elif currentLevel == 47:
                        locations_to_send.add(0x73 + self.offset)
                    elif currentLevel == 53:
                        locations_to_send.add(0x7B + self.offset)
                    elif currentLevel == 59:
                        locations_to_send.add(0x89 + self.offset)
                    elif currentLevel == 64:
                        locations_to_send.add(0x8B + self.offset)
                    elif currentLevel == 3:
                        locations_to_send.add(0x93 + self.offset)
                # J
                elif x == 0xA5:
                    if currentLevel == 15:
                        locations_to_send.add(0x4C + self.offset)
                    elif currentLevel == 20:
                        locations_to_send.add(0x5A + self.offset)
                    elif currentLevel == 40:
                        locations_to_send.add(0x63 + self.offset)
                    elif currentLevel == 42:
                        locations_to_send.add(0x6B + self.offset)
                    elif currentLevel == 59:
                        locations_to_send.add(0x84 + self.offset)
                    elif currentLevel == 3:
                        locations_to_send.add(0x95 + self.offset)
                    elif currentLevel == 73:
                        locations_to_send.add(0x9B + self.offset)
                # K
                elif x == 0xA0:
                    if currentLevel == 68:
                        locations_to_send.add(0x96 + self.offset)
                # L
                elif x == 0x9F:
                    if currentLevel == 42:
                        locations_to_send.add(0x72 + self.offset)
                    elif currentLevel == 3:
                        locations_to_send.add(0x97 + self.offset)
                    elif currentLevel == 73:
                        locations_to_send.add(0x9F + self.offset)
                # M
                elif x == 0x9C:
                    if currentLevel == 73:
                        locations_to_send.add(0xA0 + self.offset)
                    elif currentLevel == 79:
                        locations_to_send.add(0xA6 + self.offset)
                # X
                elif x == 0x64:
                    if currentLevel == 12:
                        locations_to_send.add(0x47 + self.offset)
                    elif currentLevel == 16:
                        locations_to_send.add(0x51 + self.offset)
                    elif currentLevel == 19:
                        locations_to_send.add(0x54 + self.offset)
                    elif currentLevel == 46:
                        locations_to_send.add(0x75 + self.offset)
                    elif currentLevel == 55:
                        locations_to_send.add(0x80 + self.offset)
                    elif currentLevel == 60:
                        locations_to_send.add(0x87 + self.offset)
                    elif currentLevel == 82:
                        locations_to_send.add(0xA3 + self.offset)
                        locations_to_send.add(0xA4 + self.offset)
                    elif currentLevel == 77:
                        locations_to_send.add(0xA5 + self.offset)
                # BB
                elif x == 0x8D:
                    if currentLevel == 30:
                        locations_to_send.add(0x5C + self.offset)
                # Heart RC
                elif x == 0x47:
                    locations_to_send.add(0x47 + self.offset)
                # Yeti Lamp
                elif x == 0x54:
                    locations_to_send.add(0x54 + self.offset)
                # Medal Of Honor
                elif x == 0x80:
                    locations_to_send.add(0x80 + self.offset)
                # Heart CR
                elif x == 0xA3:
                    locations_to_send.add(0xA3 + self.offset)
                    locations_to_send.add(0x0 + self.offset)
                # Spot On Warp Device
                elif x == 0xA4:
                    locations_to_send.add(0xA4 + self.offset)
                # Magic Gold Dust
                elif x == 0xA6:
                    locations_to_send.add(0xA6 + self.offset)


            #if item_to_send is not None and item_to_send != set():
            #    for x in ctx.slot_data["item_locations"]:
            #        if x[0]-self.offset in item_to_send:
            #            locations_to_send.add(x[1])
            #    for x in [0x47,0x54,0x80,0xA3,0xA4,0xA5]:
            #        if x in item_to_send:
            #            locations_to_send.add(x+self.offset)

            if locations_to_send is not None and locations_to_send != set():
                await ctx.send_msgs([{
                    "cmd": "LocationChecks",
                    "locations": list(x for x in locations_to_send)
                }])

            itemWrites = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

            for item in ctx.items_received:
                itemID = item.item - self.offset
                if itemID not in [0x4E, 0x56, 0x5D, 0x6D, 0x76, 0x7E, 0x86, 0x8E, 0xA5, 0xA6, 0xA0, 0x9C, 0x64, 0x9F, 0x8D]:
                    page = math.floor((itemID - 0x43) / 8)
                    byteTotal = 2 ** ((itemID - 0x43) % 8)
                    itemWrites[page] += byteTotal

            writes = []
            for x in range(13):
                writes += [(0x2FE7 + x, itemWrites[x].to_bytes(8, "little"), "IWRAM")]

            await bizhawk.write(ctx.bizhawk_ctx, writes)

        except bizhawk.RequestFailedError:
            # Exit handler and return to main loop to reconnect
            pass

def bitfield(n):
    return [int(digit) for digit in bin(n)[2:]]  # [2:] to chop off the "0b" part