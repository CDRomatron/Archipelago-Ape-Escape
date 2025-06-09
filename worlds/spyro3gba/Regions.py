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
    ys19 = Region(Regions.YS19.value, player, multiworld)
    ys19Free = Region(Subregions.YS19Free.value, player, multiworld)

    ys20 = Region(Regions.YS20.value, player, multiworld)
    ys20Free = Region(Subregions.YS20Free.value, player, multiworld)
    ys20Quest = Region(Subregions.YS20Quest.value, player, multiworld)
    ys20Red = Region(Subregions.YS20Red.value, player, multiworld)
    ys20Purple = Region(Subregions.YS20Purple.value, player, multiworld)

    ys27 = Region(Regions.YS27.value, player, multiworld)
    ys27Free = Region(Subregions.YS27Free.value, player, multiworld)

    ys29 = Region(Regions.YS29.value, player, multiworld)
    ys29Free = Region(Subregions.YS29Free.value, player, multiworld)

    # Byrd Barracks

    bb30 = Region(Regions.BB30.value, player, multiworld)
    bb30Free = Region(Subregions.BB30Free.value, player, multiworld)

    bb31 = Region(Regions.BB31.value, player, multiworld)
    bb31Free = Region(Subregions.BB31Free.value, player, multiworld)
    bb31Red = Region(Subregions.BB31Red.value, player, multiworld)
    bb31Quest = Region(Subregions.BB31Quest.value, player, multiworld)

    bb33 = Region(Regions.BB33.value, player, multiworld)
    bb33Free = Region(Subregions.BB33Free.value, player, multiworld)

    # Thieves' Guild

    tg35 = Region(Regions.TG35.value, player, multiworld)
    tg35Free = Region(Subregions.TG35Free.value, player, multiworld)

    tg36 = Region(Regions.TG36.value, player, multiworld)
    tg36Free = Region(Subregions.TG36Free.value, player, multiworld)
    tg36Quest = Region(Subregions.TG36Quest.value, player, multiworld)
    tg36Purple = Region(Subregions.TG36Purple.value, player, multiworld)

    tg37 = Region(Regions.TG37.value, player, multiworld)
    tg37Free = Region(Subregions.TG37Free.value, player, multiworld)

    tg39 = Region(Regions.TG39.value, player, multiworld)
    tg39Free = Region(Subregions.TG39Free.value, player, multiworld)

    # Rabbit Habitat

    rh42 = Region(Regions.RH42.value, player, multiworld)
    rh42Free = Region(Subregions.RH42Free.value, player, multiworld)
    rh42Quest = Region(Subregions.RH42Quest.value, player, multiworld)
    rh42Red = Region(Subregions.RH42Red.value, player, multiworld)
    rh42Purple = Region(Subregions.RH42Purple.value, player, multiworld)
    rh42Yellow = Region(Subregions.RH42Yellow.value, player, multiworld)

    rh44 = Region(Regions.RH44.value, player, multiworld)
    rh44Free = Region(Subregions.RH44Free.value, player, multiworld)

    # Banana Savannah

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

    ys19Free.locations += [Spyro3GBALocation(player, loc_name, location_table[loc_name], ys19Free) for loc_name in get_array([0x54])]
    ys20Free.locations += [Spyro3GBALocation(player, loc_name, location_table[loc_name], ys20Free) for loc_name in get_array([0x53])]
    ys20Quest.locations += [Spyro3GBALocation(player, loc_name, location_table[loc_name], ys20Quest) for loc_name in get_array([0x56])]
    ys20Red.locations += [Spyro3GBALocation(player, loc_name, location_table[loc_name], ys20Red) for loc_name in get_array([0x55,0x59])]
    ys20Purple.locations += [Spyro3GBALocation(player, loc_name, location_table[loc_name], ys20Purple) for loc_name in get_array([0x5A])]
    ys27Free.locations += [Spyro3GBALocation(player, loc_name, location_table[loc_name], ys27Free) for loc_name in get_array([0x58])]
    ys29Free.locations += [Spyro3GBALocation(player, loc_name, location_table[loc_name], ys29Free) for loc_name in get_array([0x57])]

    bb30Free.locations += [Spyro3GBALocation(player, loc_name, location_table[loc_name], bb30Free) for loc_name in get_array([0x5C])]
    bb31Free.locations += [Spyro3GBALocation(player, loc_name, location_table[loc_name], bb31Free) for loc_name in get_array([0x5B,0x5E,0x60,0x61])]
    bb31Red.locations += [Spyro3GBALocation(player, loc_name, location_table[loc_name], bb31Red) for loc_name in get_array([0x62])]
    bb31Quest.locations += [Spyro3GBALocation(player, loc_name, location_table[loc_name], bb31Quest) for loc_name in get_array([0x5D])]
    bb33Free.locations += [Spyro3GBALocation(player, loc_name, location_table[loc_name], bb33Free) for loc_name in get_array([0x5F])]

    tg35Free.locations += [Spyro3GBALocation(player, loc_name, location_table[loc_name], tg35Free) for loc_name in get_array([0x64])]
    tg36Free.locations += [Spyro3GBALocation(player, loc_name, location_table[loc_name], tg36Free) for loc_name in get_array([0x68,0x69,0x6A])]
    tg36Quest.locations += [Spyro3GBALocation(player, loc_name, location_table[loc_name], tg36Quest) for loc_name in get_array([0x65])]
    tg36Purple.locations += [Spyro3GBALocation(player, loc_name, location_table[loc_name], tg36Purple) for loc_name in get_array([0x63])]
    tg37Free.locations += [Spyro3GBALocation(player, loc_name, location_table[loc_name], tg37Free) for loc_name in get_array([0x66])]
    tg39Free.locations += [Spyro3GBALocation(player, loc_name, location_table[loc_name], tg39Free) for loc_name in get_array([0x67])]

    rh42Free.locations += [Spyro3GBALocation(player, loc_name, location_table[loc_name], rh42Free) for loc_name in get_array([0x6C,0x6F])]
    rh42Quest.locations += [Spyro3GBALocation(player, loc_name, location_table[loc_name], rh42Quest) for loc_name in get_array([0x6D])]
    rh42Red.locations += [Spyro3GBALocation(player, loc_name, location_table[loc_name], rh42Red) for loc_name in get_array([0x70,0x71])]
    rh42Purple.locations += [Spyro3GBALocation(player, loc_name, location_table[loc_name], rh42Purple) for loc_name in get_array([0x6B])]
    rh42Yellow.locations += [Spyro3GBALocation(player, loc_name, location_table[loc_name], rh42Yellow) for loc_name in get_array([0x72])]
    rh44Free.locations += [Spyro3GBALocation(player, loc_name, location_table[loc_name], rh44Free) for loc_name in get_array([0x6E])]

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
    regions += [ys19, ys19Free, ys20, ys20Free, ys20Quest, ys20Red, ys20Purple, ys27, ys27Free, ys29, ys29Free]
    regions += [bb30, bb30Free, bb31, bb31Free, bb31Red, bb31Quest, bb33, bb33Free]
    regions += [tg35, tg35Free, tg36, tg36Free, tg36Quest, tg36Purple, tg37, tg37Free, tg39, tg39Free]
    regions += [rh42, rh42Free, rh42Quest, rh42Red, rh42Purple, rh42Yellow, rh44, rh44Free]

    regions += [bs, kh, mm, cs, pl, rc, cr]

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