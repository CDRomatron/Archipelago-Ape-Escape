from typing import TYPE_CHECKING

from BaseClasses import Region, Entrance
from .Locations import location_table, YugiohGXLocation
from .Packs import get_all_packs
from .Strings import Packs, Cards


def create_regions(world: "YuGiOhGXWorld"):
    options = world.options
    player = world.player
    multiworld = world.multiworld
    # menu
    menu = Region("Menu", player, multiworld)
    victory = Region("Victory", player, multiworld)

    slifer = Region("Slifer", player, multiworld)
    ra = Region("Ra", player, multiworld)
    obelisk = Region("Obelisk", player, multiworld)

    slifer.locations += [YugiohGXLocation(player, loc_name, location_table[loc_name], slifer) for loc_name in
                         get_array(get_next_x(1001, options.wins.value))] # Jaden
    slifer.locations += [YugiohGXLocation(player, loc_name, location_table[loc_name], slifer) for loc_name in
                         get_array(get_next_x(1011, options.wins.value))] # Syrus
    slifer.locations += [YugiohGXLocation(player, loc_name, location_table[loc_name], slifer) for loc_name in
                         get_array(get_next_x(1021, options.wins.value))] # Chumley
    slifer.locations += [YugiohGXLocation(player, loc_name, location_table[loc_name], slifer) for loc_name in
                         get_array(get_next_x(1031, options.wins.value))] # Banner
    slifer.locations += [YugiohGXLocation(player, loc_name, location_table[loc_name], slifer) for loc_name in
                         get_array(get_next_x(1041, options.wins.value))] # Blair
    slifer.locations += [YugiohGXLocation(player, loc_name, location_table[loc_name], slifer) for loc_name in
                         get_array(get_next_x(1051, options.wins.value))] # Gerard

    if options.logic == 0x01:
        slifer.locations += [YugiohGXLocation(player, loc_name, location_table[loc_name], slifer) for loc_name in
                        get_array(get_next_x(1061, options.wins.value))] # Bastion
    else:
        ra.locations += [YugiohGXLocation(player, loc_name, location_table[loc_name], ra) for loc_name in
                         get_array(get_next_x(1061, options.wins.value))]  # Bastion
    ra.locations += [YugiohGXLocation(player, loc_name, location_table[loc_name], ra) for loc_name in
                     get_array(get_next_x(1071, options.wins.value))] # Brier
    ra.locations += [YugiohGXLocation(player, loc_name, location_table[loc_name], ra) for loc_name in
                     get_array(get_next_x(1081, options.wins.value))] # Beauregard
    ra.locations += [YugiohGXLocation(player, loc_name, location_table[loc_name], ra) for loc_name in
                     get_array(get_next_x(1091, options.wins.value))] # Dimitri
    ra.locations += [YugiohGXLocation(player, loc_name, location_table[loc_name], ra) for loc_name in
                     get_array(get_next_x(1101, options.wins.value))] # Sartyr

    if options.logic == 0x01:
        slifer.locations += [YugiohGXLocation(player, loc_name, location_table[loc_name], slifer) for loc_name in
                              get_array(get_next_x(1111, options.wins.value))] # Alexis
        slifer.locations += [YugiohGXLocation(player, loc_name, location_table[loc_name], slifer) for loc_name in
                              get_array(get_next_x(1121, options.wins.value))] # Chazz
        slifer.locations += [YugiohGXLocation(player, loc_name, location_table[loc_name], slifer) for loc_name in
                              get_array(get_next_x(1151, options.wins.value))] # Fontaine
        slifer.locations += [YugiohGXLocation(player, loc_name, location_table[loc_name], slifer) for loc_name in
                              get_array(get_next_x(1161, options.wins.value))] # Crowler
        slifer.locations += [YugiohGXLocation(player, loc_name, location_table[loc_name], slifer) for loc_name in
                              get_array(get_next_x(1171, options.wins.value))] # Zane
    else:
        obelisk.locations += [YugiohGXLocation(player, loc_name, location_table[loc_name], obelisk) for loc_name in
                              get_array(get_next_x(1111, options.wins.value))]  # Alexis
        obelisk.locations += [YugiohGXLocation(player, loc_name, location_table[loc_name], obelisk) for loc_name in
                              get_array(get_next_x(1121, options.wins.value))]  # Chazz
        obelisk.locations += [YugiohGXLocation(player, loc_name, location_table[loc_name], obelisk) for loc_name in
                              get_array(get_next_x(1151, options.wins.value))]  # Fontaine
        obelisk.locations += [YugiohGXLocation(player, loc_name, location_table[loc_name], obelisk) for loc_name in
                              get_array(get_next_x(1161, options.wins.value))]  # Crowler
        obelisk.locations += [YugiohGXLocation(player, loc_name, location_table[loc_name], obelisk) for loc_name in
                              get_array(get_next_x(1171, options.wins.value))]  # Zane
    obelisk.locations += [YugiohGXLocation(player, loc_name, location_table[loc_name], obelisk) for loc_name in
                          get_array(get_next_x(1131, options.wins.value))]  # Torrey
    obelisk.locations += [YugiohGXLocation(player, loc_name, location_table[loc_name], obelisk) for loc_name in
                          get_array(get_next_x(1141, options.wins.value))]  # Damon

    victory.locations += [YugiohGXLocation(player, loc_name, location_table[loc_name], victory) for loc_name in
                          get_array([0])]

    regions = [menu, slifer, ra, obelisk, victory]

    if options.cardsanity == 0x00:
        for pack in Packs:
            packRegion = Region(pack.value, player, multiworld)
            regions += [packRegion]

        for card in Cards:
            cardRegion = Region(card.value, player, multiworld)
            cardRegion.locations += [YugiohGXLocation(player, card.value, location_table[card.value], cardRegion)]
            regions += [cardRegion]

    multiworld.regions.extend(regions)


def connect_regions(world: "YuGiOhGX", source: str, target: str, rule=None):
    source_region = world.get_region(source)
    target_region = world.get_region(target)

    connection = Entrance(world.player, source + "_to_" + target, source_region)
    if rule:
        connection.access_rule = rule

    source_region.exits.append(connection)
    connection.connect(target_region)


def get_array(array):
    res = dict()
    for i in array:
        for key, val in location_table.items():
            if int(val) == i + 129000000:
                res[key] = val
    return res


def get_next_five(inVal):
    out = []
    out.append(inVal)
    out.append(inVal + 1)
    out.append(inVal + 2)
    out.append(inVal + 3)
    out.append(inVal + 4)
    return out

def get_next_x(inVal, x):
    out = []
    for n in range(x):
        out.append(inVal+n)
    return out