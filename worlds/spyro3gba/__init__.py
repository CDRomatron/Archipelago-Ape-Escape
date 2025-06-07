import math
import os
import json
import pkgutil
from typing import ClassVar, Dict, List, Tuple, Optional, TextIO

import Utils
from BaseClasses import ItemClassification, MultiWorld, Tutorial, CollectionState, LocationProgressType
from logging import warning
from Options import OptionError
from worlds.AutoWorld import WebWorld, World

from .Items import item_table, Spyro3GBAItem, item_table_static, item_table_shuffle
from .Constants import Items, gamename, baseid
from .Locations import location_table
from .Regions import create_regions
from .Rom import Spyro3GBAProcedurePatch, write_tokens
from .Rules import set_rules
from Options import AssembleOptions
import settings

class Spyro3GBAWeb(WebWorld):
    theme = "stone"

    setup_en = Tutorial(
        "",
        "",
        "",
        "",
        "",
        ["CDRomatron"]
    )

    tutorials = [setup_en]

class Spyro3GBASettings(settings.Group):
    class Spyro3GBARomFile(settings.UserFilePath):
        """File name of your US Spyro 3 GBA ROM"""
        description = "Spyro 3 GBA ROM File"
        copy_to = "Spyro 3 (USA).gba"
        md5s = [Spyro3GBAProcedurePatch.hash]

    rom_file: Spyro3GBARomFile = Spyro3GBARomFile(Spyro3GBARomFile.copy_to)
class Spyro3GBAWorld(World):
    """
    Long description of game here
    """

    game = gamename
    web: ClassVar[WebWorld] = Spyro3GBAWeb()
    topology_present = True

    item_name_to_id = item_table

    for key, value in item_name_to_id.items():
        item_name_to_id[key] = value + baseid

    location_name_to_id = location_table

    for key, value in location_name_to_id.items():
        location_name_to_id[key] = value + baseid

    def __init__(self, multiworld: MultiWorld, player: int):
        super(Spyro3GBAWorld, self).__init__(multiworld, player)

    def generate_early(self) -> None:
        self.itempool = []

    def create_regions(self):
        create_regions(self)

    def set_rules(self):
        set_rules(self)

    def create_item(self, name: str) -> Spyro3GBAItem:
        item_id = item_table[name]
        classification = ItemClassification.progression

        item = Spyro3GBAItem(name, classification, item_id, self.player)
        return item

    def create_items(self):
        victory = self.create_item("Victory")
        heartrc = self.create_item(Items.HeartofRhynocsnClocks.value)
        fairyspellbook = self.create_item(Items.FairySpellBook.value)
        yetilamp = self.create_item(Items.YetiLamp.value)
        herosheartmedal = self.create_item(Items.HerosHeartMedal.value)
        medalofhonor = self.create_item(Items.MedalOfHonor.value)
        minidynamo = self.create_item(Items.MiniDynamo.value)
        heartcr = self.create_item(Items.HeartOfChateauRipto.value)
        spotonwarpdevice = self.create_item(Items.SpotOnWarpDevice.value)
        magicgolddust = self.create_item(Items.MagicGoldDust.value)

        for x in item_table_shuffle.keys():
            item = self.create_item(x)
            self.itempool += [item]

        self.get_location("Victory").place_locked_item(victory)
        self.get_location(Constants.Locations.DSRipto.value).place_locked_item(heartrc)
        self.get_location(Constants.Locations.FLRipto.value).place_locked_item(fairyspellbook)
        self.get_location(Constants.Locations.YSFreezeGoats.value).place_locked_item(yetilamp)
        self.get_location(Constants.Locations.RCWhackARhynoc.value).place_locked_item(herosheartmedal)
        self.get_location(Constants.Locations.KHSolveThe9SquarePuzzle.value).place_locked_item(medalofhonor)
        self.get_location(Constants.Locations.MMButlerFight.value).place_locked_item(minidynamo)
        self.get_location(Constants.Locations.CRRipto.value).place_locked_item(heartcr)
        self.get_location(Constants.Locations.CRRipto2.value).place_locked_item(spotonwarpdevice)
        self.get_location(Constants.Locations.CRMoneybags.value).place_locked_item(magicgolddust)

        self.multiworld.itempool += self.itempool

    def fill_slot_data(self):
        return {

        }

    def generate_output(self, output_directory: str):
        outfilepname = f"_P{self.player}"
        outfilepname += f"_{self.multiworld.get_file_safe_player_name(self.player).replace(' ', '_')}"
        self.rom_name_text = f'S3GBA{Utils.__version__.replace(".", "")[0:3]}_{self.player}_{self.multiworld.seed:11}\0'
        self.romName = bytearray(self.rom_name_text, "utf8")[:0x20]
        self.romName.extend([0] * (0x20 - len(self.romName)))
        self.rom_name = self.romName
        self.playerName = bytearray(self.multiworld.player_name[self.player], "utf8")[:0x20]
        self.playerName.extend([0] * (0x20 - len(self.playerName)))
        patch = Spyro3GBAProcedurePatch(player=self.player, player_name=self.multiworld.player_name[self.player])
        procedure = [("apply_tokens", ["token_data.bin"])]
        patch.procedure = procedure
        write_tokens(self, patch)

        # Write Output
        out_file_name = self.multiworld.get_out_file_name_base(self.player)
        patch.write(os.path.join(output_directory, f"{out_file_name}{patch.patch_file_ending}"))