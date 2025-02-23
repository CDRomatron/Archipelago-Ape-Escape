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
    This is disable Instantly Recieve Cards option.

    true: Cards will be automatically added to your inventory upon finding. Locations will be sent when buying packs.
    false: Does not add all 1200 cards as locations and items.

    Supported values: true, false
    Default value: false
    """
    display_name = "Cardsanity"
    option_true = 0x0
    option_false = 0x1
    default = option_false

@dataclass
class YugiohGXOptions(PerGameCommonOptions):
    wins: WinsEachOption
    instant: InstantCardOption
    cardsanity: CardSanityOption