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

            reads = await bizhawk.read(ctx.bizhawk_ctx, item_reads)

            item_to_send = set()
            locations_to_send = set()

            for x in range(13):
                if x != 12:
                    for y in range(8):
                        from_bytes = int.from_bytes(reads[x], byteorder="little")
                        power = pow(2,y)
                        if from_bytes & power:
                            item_to_send.add(0x43 + y + (x*8))
                else:
                    for y in range(4):
                        if int.from_bytes(reads[x], byteorder="little") & pow(2,y):
                            item_to_send.add(0x43 + y + (x*8))

            if item_to_send is not None and item_to_send != set():
                for x in ctx.slot_data["item_locations"]:
                    if x[0]-self.offset in item_to_send:
                        locations_to_send.add(x[1])
                for x in [0x47,0x51,0x54,0x6F,0x80,0x85,0xA3,0xA4,0xA5]:
                    if x in item_to_send:
                        locations_to_send.add(x+self.offset)

            if locations_to_send is not None and locations_to_send != set():
                await ctx.send_msgs([{
                    "cmd": "LocationChecks",
                    "locations": list(x for x in locations_to_send)
                }])



        except bizhawk.RequestFailedError:
            # Exit handler and return to main loop to reconnect
            pass

def bitfield(n):
    return [int(digit) for digit in bin(n)[2:]]  # [2:] to chop off the "0b" part