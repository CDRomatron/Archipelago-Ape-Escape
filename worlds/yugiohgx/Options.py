from __future__ import annotations

from dataclasses import dataclass
from Options import Choice, Option, PerGameCommonOptions, Range

from typing import Dict

class WinsEachOption(Range):
    """Choose how many wins are needed for each duelist. This also sets the number of locations per duelist.

    Supported values: 3-10
    Default value: 5
    """
    display_name = "Wins Per Duelist"
    range_start = 3
    range_end = 10
    default = 5

class InstantCardOption(Choice):
    """Choose if cards are automatically added to your collection upon finding a pack.
    This will be disabled for cardsanity.

    true: Three copies of every card in the pack are instantly added to your collection.
    false: Vanilla. Cards must be purchased from the shop.

    Supported values: true, false
    Default value: true
    """
    display_name = "Instantly Recieve Cards"
    option_true = 0x0
    option_false = 0x1
    default = option_true

class CardSanityOption(Choice):
    """Sets every card in the game as a location, and as an item.
    This will disable Instantly Recieve Cards option.

    true: Cards will be automatically added to your inventory upon finding. Locations will be sent when buying packs.
    false: Does not add all 1200 cards as locations and items.

    Supported values: true, false
    Default value: false
    """
    display_name = "Cardsanity"
    option_true = 0x0
    option_false = 0x1
    default = option_false

class LogicOption(Choice):
    """Sets the logic used for calculating the playthrough.
    Options to guarantee how many cards should be available to collect by that point.

    dorm: It is assumed that you can't beat Ra Yellow duelists with less than 400 cards available. 800 and timed duels
    for Obelisk Blue.
    access: It is assumed that you can't move up to Ra Yellow with less than 400 cards available. 800 and timed duels
    for Obelisk Blue.
    minimal: Only assumes Timed Duels items before Obelisk.

    Supported values: dorm, access, minimal
    Default value: dorm
    """
    display_name = "Logic Option"
    option_dorm = 0x0
    option_access = 0x1
    option_minimal = 0x2
    default = option_dorm

class DorothyLogicOption(Choice):
    """Sets how dorothy's gift should be used for calculating playthrough.

    ehsfw: Only Elemental Hero - Shining Flare Wingman becomes logically available from Dorothy's Gift.
    all: All cards become logically available from Dorothy's Gift.
    off: Removes Dorothy's Gift from the list of Packs. Elemental Hero - Shining Flare Wingman is given at start.

    Supported values: ehsfw, all, off
    Default value: ehsfw
    """
    display_name = "Dorothy's Pack Logic"
    option_ehsfw = 0x0
    option_all = 0x1
    option_off = 0x2
    default = option_ehsfw

@dataclass
class YugiohGXOptions(PerGameCommonOptions):
    wins: WinsEachOption
    instant: InstantCardOption
    cardsanity: CardSanityOption
    logic: LogicOption
    dorothy: DorothyLogicOption