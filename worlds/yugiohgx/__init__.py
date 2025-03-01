import math
import os
import json
from typing import ClassVar, Dict, List, Tuple, Optional, TextIO

from BaseClasses import ItemClassification, MultiWorld, Tutorial, CollectionState
from logging import warning
from Options import OptionError
from worlds.AutoWorld import WebWorld, World

from .Items import item_table, YugiohGXItem
from .Strings import Items, Packs, gamename
from .Locations import location_table, base_location_id
from .Regions import create_regions
from .Rules import set_rules
from .Client import YuGiOhGXClient
from .Options import YugiohGXOptions, WinsEachOption, InstantCardOption, CardSanityOption, LogicOption, \
    DorothyLogicOption
from Options import AssembleOptions

class YuGiOhGXWeb(WebWorld):
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

class YuGiOhGXWorld(World):
    """
    Long description of game here
    """

    game = gamename
    web: ClassVar[WebWorld] = YuGiOhGXWeb()
    options_dataclass = YugiohGXOptions
    options: YugiohGXOptions
    topology_present = True

    item_name_to_id = item_table

    for key, value in item_name_to_id.items():
        item_name_to_id[key] = value + base_location_id

    location_name_to_id = location_table

    for key, value in location_name_to_id.items():
        location_name_to_id[key] = value + base_location_id

    def __init__(self, multiworld: MultiWorld, player: int):
        super(YuGiOhGXWorld, self).__init__(multiworld, player)
        self.wins : Optional[int] = 0
        self.instant: Optional[int] = 0
        self.cardsanity: Optional[int] = 0
        self.logic: Optional[int] = 0
        self.dorothy: Optional[int] = 0

    def generate_early(self) -> None:
        self.itempool = []
        self.wins = self.options.wins
        self.instant = self.options.instant
        self.cardsanity = self.options.cardsanity
        self.logic = self.options.logic
        self.dorothy = self.options.dorothy

    def create_regions(self):
        create_regions(self)

    def set_rules(self):
        set_rules(self)

    def create_item(self, name: str) -> YugiohGXItem:
        item_id = item_table[name]
        classification = ItemClassification.progression

        item = YugiohGXItem(name, classification, item_id, self.player)
        return item

    def create_item_useful(self, name: str) -> YugiohGXItem:
        item_id = item_table[name]
        classification = ItemClassification.useful

        item = YugiohGXItem(name, classification, item_id, self.player)
        return item

    def create_item_filler(self, name: str) -> YugiohGXItem:
        item_id = item_table[name]
        classification = ItemClassification.filler

        item = YugiohGXItem(name, classification, item_id, self.player)
        return item

    def create_items(self):
        victory = self.create_item("Victory")
        wins = self.create_item(Strings.Items.Wins.value)
        timed = self.create_item(Strings.Items.Timed.value)
        written = self.create_item(Strings.Items.Written.value)

        self.itempool += [wins, timed, written]

        for x in Strings.Packs:
            self.itempool += [(self.create_item(x.value))]

        if self.options.cardsanity == 0x00:
            for x in Strings.Cards:
                self.itempool += [(self.create_item(x.value))]

        self.get_location("Victory").place_locked_item(victory)

        for _ in range(len(self.multiworld.get_unfilled_locations(self.player)) - len(self.itempool)):
            self.itempool += [self.create_item_useful(Strings.Items.DP.value)]

        self.multiworld.itempool += self.itempool

    def fill_slot_data(self):
        return {
            "wins": self.options.wins.value,
            "instant": self.options.instant.value,
            "cardsanity": self.options.cardsanity.value,
            "logic": self.options.logic.value,
            "dorothy": self.options.logic.value
        }


    def generate_output(self, output_directory: str):
        data = {
            "slot_data": self.fill_slot_data()
        }