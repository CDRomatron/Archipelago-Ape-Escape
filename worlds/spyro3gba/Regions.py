from typing import TYPE_CHECKING

from BaseClasses import Region, Entrance
from .Locations import location_table, Spyro3GBALocation
from .Constants import Hubs, baseid, Regions, Subregions


def create_regions(world: "Spyro3GBAWorld"):
    options = world.options
    player = world.player
    multiworld = world.multiworld
    # menu
    menu = Region("Menu", player, multiworld)
    victory = Region("Victory", player, multiworld)

    # Dragon Shores
    ds4 = Region(Regions.DS4.value, player, multiworld)
    ds4Free = Region(Subregions.DS4Free.value, player, multiworld)
    ds4Quest = Region(Subregions.DS4Quest.value, player, multiworld)

    ds6 = Region(Regions.DS6.value, player, multiworld)
    ds6Free = Region(Subregions.DS6Free.value, player, multiworld)

    ds8 = Region(Regions.DS8.value, player, multiworld)
    ds8Free = Region(Subregions.DS8Free.value, player, multiworld)
    ds8Green = Region(Subregions.DS8Green.value, player, multiworld)

    ds9 = Region(Regions.DS9.value, player, multiworld)
    ds9Free = Region(Subregions.DS9Free.value, player, multiworld)

    ds12 = Region(Regions.DS12.value, player, multiworld)
    ds12Boss = Region(Subregions.DS12Boss.value, player, multiworld)

    # Fairy Library
    fl14 = Region(Regions.FL14.value, player, multiworld)
    fl14Free = Region(Subregions.FL14Free.value, player, multiworld)

    fl15 = Region(Regions.FL15.value, player, multiworld)
    fl15Books = Region(Subregions.FL15Books.value, player, multiworld)
    fl15Quest = Region(Subregions.FL15Quest.value, player, multiworld)
    fl15Red = Region(Subregions.FL15Red.value, player, multiworld)
    fl15Green = Region(Subregions.FL15Green.value, player, multiworld)
    fl15Purple = Region(Subregions.FL15Purple.value, player, multiworld)

    fl16 = Region(Regions.FL16.value, player, multiworld)
    fl16Boss = Region(Subregions.FL16Boss.value, player, multiworld)

    fl18 = Region(Regions.FL18.value, player, multiworld)
    fl18Free = Region(Subregions.FL18Free.value, player, multiworld)

    # Yeti Serengeti
    ys = Region(Hubs.YS.value, player, multiworld)

    bb = Region(Hubs.BB.value, player, multiworld)
    tg = Region(Hubs.TG.value, player, multiworld)
    rh = Region(Hubs.RH.value, player, multiworld)
    bs = Region(Hubs.BS.value, player, multiworld)
    kh = Region(Hubs.KH.value, player, multiworld)
    mm = Region(Hubs.MM.value, player, multiworld)
    cs = Region(Hubs.CS.value, player, multiworld)
    pl = Region(Hubs.PL.value, player, multiworld)
    rc = Region(Hubs.RC.value, player, multiworld)
    cr = Region(Hubs.CR.value, player, multiworld)


    # Locations
    ds4Free.locations += [Spyro3GBALocation(player, loc_name, location_table[loc_name], ds4Free) for loc_name in get_array([0x46,0x4A])]
    ds4Quest.locations += [Spyro3GBALocation(player, loc_name, location_table[loc_name], ds4Quest) for loc_name in get_array([0x45])]
    ds6Free.locations += [Spyro3GBALocation(player, loc_name, location_table[loc_name], ds6Free) for loc_name in get_array([0x43])]
    ds8Free.locations += [Spyro3GBALocation(player, loc_name, location_table[loc_name], ds8Free) for loc_name in get_array([0x49])]
    ds8Green.locations += [Spyro3GBALocation(player, loc_name, location_table[loc_name], ds8Green) for loc_name in get_array([0x44])]
    ds9Free.locations += [Spyro3GBALocation(player, loc_name, location_table[loc_name], ds9Free) for loc_name in get_array([0x48])]
    ds12Boss.locations += [Spyro3GBALocation(player, loc_name, location_table[loc_name], ds12Boss) for loc_name in get_array([0x47])]

    fl14Free.locations += [Spyro3GBALocation(player, loc_name, location_table[loc_name], fl14Free) for loc_name in get_array([0x4D])]
    fl15Books.locations += [Spyro3GBALocation(player, loc_name, location_table[loc_name], fl15Books) for loc_name in get_array([0x4F])]
    fl15Quest.locations += [Spyro3GBALocation(player, loc_name, location_table[loc_name], fl15Quest) for loc_name in get_array([0x4E])]
    fl15Red.locations += [Spyro3GBALocation(player, loc_name, location_table[loc_name], fl15Red) for loc_name in get_array([0x52])]
    fl15Green.locations += [Spyro3GBALocation(player, loc_name, location_table[loc_name], fl15Green) for loc_name in get_array([0x4B])]
    fl15Purple.locations += [Spyro3GBALocation(player, loc_name, location_table[loc_name], fl15Purple) for loc_name in get_array([0x4C])]
    fl16Boss.locations += [Spyro3GBALocation(player, loc_name, location_table[loc_name], fl16Boss) for loc_name in get_array([0x51])]
    fl18Free.locations += [Spyro3GBALocation(player, loc_name, location_table[loc_name], fl18Free) for loc_name in get_array([0x50])]

    ys.locations += [Spyro3GBALocation(player, loc_name, location_table[loc_name], ys) for loc_name in get_array([0x53,0x54,0x55,0x56,0x57,0x58,0x59,0x5A])]
    bb.locations += [Spyro3GBALocation(player, loc_name, location_table[loc_name], bb) for loc_name in get_array([0x5B,0x5C,0x5D,0x5E,0x5F,0x60,0x61,0x62])]
    tg.locations += [Spyro3GBALocation(player, loc_name, location_table[loc_name], tg) for loc_name in get_array([0x63,0x64,0x65,0x66,0x67,0x68,0x69,0x6A])]
    rh.locations += [Spyro3GBALocation(player, loc_name, location_table[loc_name], rh) for loc_name in get_array([0x6B,0x6C,0x6D,0x6E,0x6F,0x70,0x71,0x72])]
    bs.locations += [Spyro3GBALocation(player, loc_name, location_table[loc_name], bs) for loc_name in get_array([0x73,0x74,0x75,0x76,0x77,0x78,0x79,0x7A])]
    kh.locations += [Spyro3GBALocation(player, loc_name, location_table[loc_name], kh) for loc_name in get_array([0x7B,0x7C,0x7D,0x7E,0x7F,0x80,0x81,0x82])]
    mm.locations += [Spyro3GBALocation(player, loc_name, location_table[loc_name], mm) for loc_name in get_array([0x83,0x84,0x85,0x86,0x87,0x88,0x89,0x8A])]
    cs.locations += [Spyro3GBALocation(player, loc_name, location_table[loc_name], cs) for loc_name in get_array([0x8B,0x8C,0x8D,0x8E,0x8F,0x90,0x91,0x92])]
    pl.locations += [Spyro3GBALocation(player, loc_name, location_table[loc_name], pl) for loc_name in get_array([0x93,0x94,0x95,0x96,0x97,0x98,0x99,0x9A])]
    rc.locations += [Spyro3GBALocation(player, loc_name, location_table[loc_name], rc) for loc_name in get_array([0x9B,0x9C,0x9D,0x9E,0x9F,0xA0])]
    cr.locations += [Spyro3GBALocation(player, loc_name, location_table[loc_name], cr) for loc_name in get_array([0xA1,0xA2,0xA3,0xA4,0xA5,0xA6])]


    victory.locations += [Spyro3GBALocation(player, loc_name, location_table[loc_name], victory) for loc_name in
                          get_array([0])]

    regions = [menu, victory]
    regions += [ds4, ds4Free, ds4Quest, ds6, ds6Free, ds8, ds8Free, ds8Green, ds9, ds9Free, ds12, ds12Boss]
    regions += [fl14, fl14Free, fl15, fl15Books, fl15Quest, fl15Red, fl15Green, fl15Purple, fl16, fl16Boss, fl18, fl18Free]

    regions += [ys, bb, tg, rh, bs, kh, mm, cs, pl , rc, cr]

    multiworld.regions.extend(regions)


def connect_regions(world: "Spyro3GBA", source: str, target: str, rule=None):
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
            if int(val) == i + baseid:
                res[key] = val
    return res