from typing import TYPE_CHECKING
from .Regions import connect_regions
from .Constants import Items, Hubs, Regions, Subregions

if TYPE_CHECKING:
    from . import Spyro3GBAWorld

def set_rules(world: "Spyro3GBAWorld"):
    connect_regions(world, "Menu", Regions.DS4.value, lambda state: True)

    # Dragon Shores

    connect_regions(world, Regions.DS4.value, Subregions.DS4Free.value, lambda state: True)
    connect_regions(world, Regions.DS4.value, Subregions.DS4Quest.value, lambda state: has_ds_quest(state, world))
    connect_regions(world, Regions.DS4.value, Regions.FL14.value, lambda state: True)
    connect_regions(world, Regions.DS4.value, Regions.BS46.value, lambda state: has_ice_2(state, world))
    connect_regions(world, Regions.DS4.value, Regions.PL68.value, lambda state: has_elec(state, world))
    connect_regions(world, Regions.DS4.value, Regions.DS6.value, lambda state: has_escape(state, world))

    connect_regions(world, Regions.DS6.value, Subregions.DS6Free.value, lambda state: True)
    connect_regions(world, Regions.DS6.value, Regions.YS19.value, lambda state: has_ice_1(state, world))
    connect_regions(world, Regions.DS6.value, Regions.BB30.value, lambda state: has_ice_1(state, world))
    connect_regions(world, Regions.DS6.value, Regions.TG35.value, lambda state: has_lamp(state, world))
    connect_regions(world, Regions.DS6.value, Regions.RH42.value, lambda state: has_lamp(state, world))
    connect_regions(world, Regions.DS6.value, Regions.DS12.value, lambda state: has_fire_2(state, world) and has_wind_2(state, world) and has_lamp(state, world))

    connect_regions(world, Regions.DS12.value, Subregions.DS12Boss.value, lambda state: True)
    connect_regions(world, Regions.DS12.value, Regions.DS8.value, lambda state: True)

    connect_regions(world, Regions.DS8.value, Subregions.DS8Free.value, lambda state: True)
    connect_regions(world, Regions.DS8.value, Subregions.DS8Green.value, lambda state: has_green(state, world))
    connect_regions(world, Regions.DS8.value, Regions.KH51.value, lambda state: has_fire_2(state, world) and has_ice_2(state, world))
    connect_regions(world, Regions.DS8.value, Regions.MM57.value, lambda state: True)
    connect_regions(world, Regions.DS8.value, Regions.CS63.value, lambda state: has_elec(state, world))
    connect_regions(world, Regions.DS8.value, Regions.DS9.value, lambda state: has_lamp(state, world))

    connect_regions(world, Regions.DS9.value, Subregions.DS9Free.value, lambda state: True)

    # Fairy Library

    connect_regions(world, Regions.FL14.value, Subregions.FL14Free.value, lambda state: True)
    connect_regions(world, Regions.FL14.value, Regions.FL15.value, lambda state: True)

    connect_regions(world, Regions.FL15.value, Subregions.FL15Books.value, lambda state: has_ice_1(state, world))
    connect_regions(world, Regions.FL15.value, Subregions.FL15Quest.value, lambda state: has_fl_quest(state, world))
    connect_regions(world, Regions.FL15.value, Subregions.FL15Red.value, lambda state: has_red(state, world))
    connect_regions(world, Regions.FL15.value, Subregions.FL15Green.value, lambda state: has_green(state, world))
    connect_regions(world, Regions.FL15.value, Subregions.FL15Purple.value, lambda state: has_purple(state, world))
    connect_regions(world, Regions.FL15.value, Regions.FL18.value, lambda state: True)
    connect_regions(world, Regions.FL15.value, Regions.FL16.value, lambda state: True)

    connect_regions(world, Regions.FL18.value, Subregions.FL18Free.value, lambda state: True)

    connect_regions(world, Regions.FL16.value, Subregions.FL16Boss.value, lambda state: True)

    # Yeti Serengeti

    connect_regions(world, Regions.YS19.value, Subregions.YS19Free.value, lambda state: True)
    connect_regions(world, Regions.YS19.value, Regions.YS20.value, lambda state: has_lamp(state, world))

    connect_regions(world, Regions.YS20.value, Subregions.YS20Free.value, lambda state: True)
    connect_regions(world, Regions.YS20.value, Subregions.YS20Quest.value, lambda state: has_ys_quest(state, world))
    connect_regions(world, Regions.YS20.value, Subregions.YS20Red.value, lambda state: has_red(state, world))
    connect_regions(world, Regions.YS20.value, Subregions.YS20Purple.value, lambda state: has_purple(state, world))
    connect_regions(world, Regions.YS20.value, Regions.YS27.value, lambda state: True)
    connect_regions(world, Regions.YS20.value, Regions.YS29.value, lambda state: True)

    connect_regions(world, Regions.YS27.value, Subregions.YS27Free.value, lambda state: True)

    connect_regions(world, Regions.YS29.value, Subregions.YS29Free.value, lambda state: True)

    # Byrd Barracks

    connect_regions(world, Regions.BB30.value, Subregions.BB30Free.value, lambda state: True)
    connect_regions(world, Regions.BB30.value, Regions.BB31.value, lambda state: has_ice_2(state, world))

    connect_regions(world, Regions.BB31.value, Subregions.BB31Free.value, lambda state: True)
    connect_regions(world, Regions.BB31.value, Subregions.BB31Red.value, lambda state: has_red(state, world))
    connect_regions(world, Regions.BB31.value, Subregions.BB31Quest.value, lambda state: has_bb_quest(state, world))
    connect_regions(world, Regions.BB31.value, Regions.BB33.value, lambda state: True)

    connect_regions(world, Regions.BB33.value, Subregions.BB33Free.value, lambda state: True)

    # Thieves' Guild

    connect_regions(world, Regions.TG35.value, Subregions.TG35Free.value, lambda state: True)
    connect_regions(world, Regions.TG35.value, Regions.TG36.value, lambda state: True)

    connect_regions(world, Regions.TG36.value, Subregions.TG36Free.value, lambda state: True)
    connect_regions(world, Regions.TG36.value, Subregions.TG36Quest.value, lambda state: has_tg_quest(state, world))
    connect_regions(world, Regions.TG36.value, Subregions.TG36Purple.value, lambda state: has_purple(state, world))
    connect_regions(world, Regions.TG36.value, Regions.TG37.value, lambda state: True)
    connect_regions(world, Regions.TG36.value, Regions.TG39.value, lambda state: True)

    connect_regions(world, Regions.TG37.value, Subregions.TG37Free.value, lambda state: True)

    connect_regions(world, Regions.TG39.value, Subregions.TG39Free.value, lambda state: True)

    # Rabbit Habitat

    connect_regions(world, Regions.RH42.value, Subregions.RH42Free.value, lambda state: True)
    connect_regions(world, Regions.RH42.value, Subregions.RH42Quest.value, lambda state: has_wind_2(state, world) and has_rh_quest(state, world))
    connect_regions(world, Regions.RH42.value, Subregions.RH42Red.value, lambda state: has_wind_2(state, world) and has_red(state, world))
    connect_regions(world, Regions.RH42.value, Subregions.RH42Purple.value, lambda state: has_purple(state, world))
    connect_regions(world, Regions.RH42.value, Subregions.RH42Yellow.value, lambda state: has_wind_2(state, world) and has_yellow(state, world))
    connect_regions(world, Regions.RH42.value, Regions.RH44.value, lambda state: has_wind_2(state, world))

    connect_regions(world, Regions.RH44.value, Subregions.RH44Free.value, lambda state: True)

    # Banana Savannah

    connect_regions(world, Regions.BS46.value, Subregions.BS46Free.value, lambda state: True)
    connect_regions(world, Regions.BS46.value, Regions.BS47.value, lambda state: True)

    connect_regions(world, Regions.BS47.value, Subregions.BS47Free.value, lambda state: True)
    connect_regions(world, Regions.BS47.value, Subregions.BS47Quest.value, lambda state: has_bs_quest(state, world))
    connect_regions(world, Regions.BS47.value, Subregions.BS47Red.value, lambda state: has_red(state, world))
    connect_regions(world, Regions.BS47.value, Subregions.BS47Green.value, lambda state: has_green(state, world))
    connect_regions(world, Regions.BS47.value, Subregions.BS47Targets.value, lambda state: has_fire_2(state, world))
    connect_regions(world, Regions.BS47.value, Regions.BS50.value, lambda state: has_fire_2(state, world))

    connect_regions(world, Regions.BS50.value, Subregions.BS50Free.value, lambda state: True)

    # Kangaroo Hoodoos

    connect_regions(world, Regions.KH51.value, Subregions.KH51Free.value, lambda state: True)
    connect_regions(world, Regions.KH51.value, Regions.KH52.value, lambda state: True)

    connect_regions(world, Regions.KH52.value, Subregions.KH52Red.value, lambda state: has_red(state, world))
    connect_regions(world, Regions.KH52.value, Subregions.KH52Kangaroo.value, lambda state: has_slam(state, world))
    connect_regions(world, Regions.KH52.value, Subregions.KH52Quest.value, lambda state: has_kh_quest(state, world))
    connect_regions(world, Regions.KH52.value, Regions.KH53.value, lambda state: has_lamp(state, world))
    connect_regions(world, Regions.KH52.value, Regions.KH56.value, lambda state: True)

    connect_regions(world, Regions.KH53.value, Subregions.KH53Green.value, lambda state: has_green(state, world))

    connect_regions(world, Regions.KH56.value, Subregions.KH56Free.value, lambda state: True)

    # Moneybags Mansion

    connect_regions(world, Regions.MM57.value, Subregions.MM57Free.value, lambda state: True)
    connect_regions(world, Regions.MM57.value, Regions.MM59.value, lambda state: True)
    connect_regions(world, Regions.MM57.value, Regions.MM60.value, lambda state: True)

    connect_regions(world, Regions.MM59.value, Subregions.MM59Wind.value, lambda state: has_wind_x(state, world))
    connect_regions(world, Regions.MM59.value, Subregions.MM59WindGreen.value, lambda state: has_wind_x(state, world) and has_green(state, world))
    connect_regions(world, Regions.MM59.value, Subregions.MM59Purple.value, lambda state: has_purple(state, world))
    connect_regions(world, Regions.MM59.value, Regions.MM61.value, lambda state: has_wind_x(state, world))

    connect_regions(world, Regions.MM60.value, Subregions.MM60Generator.value, lambda state: has_wind_3(state, world))

    connect_regions(world, Regions.MM61.value, Subregions.MM61Free.value, lambda state: True)

    # Cheetah Spot Spa

    connect_regions(world, Regions.CS63.value, Subregions.CS63Free.value, lambda state: True)
    connect_regions(world, Regions.CS63.value, Regions.CS64.value, lambda state: True)

    connect_regions(world, Regions.CS64.value, Subregions.CS64Free.value, lambda state: True)
    connect_regions(world, Regions.CS64.value, Subregions.CS64Quest.value, lambda state: has_cs_quest(state, world))
    connect_regions(world, Regions.CS64.value, Subregions.CS64Green.value, lambda state: has_green(state, world))
    connect_regions(world, Regions.CS64.value, Subregions.CS64Yellow.value, lambda state: has_yellow(state, world))
    connect_regions(world, Regions.CS64.value, Subregions.CS64Wind.value, lambda state: has_wind_3(state, world))

    # Professor's Secret Lab

    connect_regions(world, Regions.PL68.value, Subregions.PL68Red.value, lambda state: has_red(state, world))
    connect_regions(world, Regions.PL68.value, Subregions.PL68Purple.value, lambda state: has_purple(state, world))
    connect_regions(world, Regions.PL68.value, Regions.PL3.value, lambda state: True)
    connect_regions(world, Regions.PL68.value, Regions.PL69.value, lambda state: True)
    connect_regions(world, Regions.PL68.value, Regions.RC72.value, lambda state: True)

    connect_regions(world, Regions.PL3.value, Subregions.PL3Ice.value, lambda state: has_ice_1(state, world))
    connect_regions(world, Regions.PL3.value, Subregions.PL3IceGreen.value, lambda state: has_ice_1(state, world) and has_green(state, world))
    connect_regions(world, Regions.PL3.value, Subregions.PL3IcePurple.value, lambda state: has_ice_1(state, world) and has_purple(state, world))
    connect_regions(world, Regions.PL3.value, Subregions.PL3IceYellow.value, lambda state: has_ice_1(state, world) and has_yellow(state, world))

    connect_regions(world, Regions.PL69.value, Subregions.PL69Free.value, lambda state: True)

    # Rhynocs n' Clocks

    connect_regions(world, Regions.RC72.value, Subregions.RC72Free.value, lambda state: True)
    connect_regions(world, Regions.RC72.value, Regions.RC73.value, lambda state: True)

    connect_regions(world, Regions.RC73.value, Subregions.RC73Free.value, lambda state: True)
    connect_regions(world, Regions.RC73.value, Subregions.RC73Purple.value, lambda state: has_purple(state, world))
    connect_regions(world, Regions.RC73.value, Subregions.RC73Yellow.value, lambda state: has_yellow(state, world))
    connect_regions(world, Regions.RC73.value, Regions.CR77.value, lambda state: state.has(Items.KangarooCarving.value, world.player, 1))

    # Chateau Ripto

    connect_regions(world, Regions.CR77.value, Subregions.CR77Wind.value, lambda state: has_wind_2(state, world))
    connect_regions(world, Regions.CR77.value, Regions.CR81.value, lambda state: has_wind_2(state, world))
    connect_regions(world, Regions.CR77.value, Regions.CR82.value, lambda state: True)

    connect_regions(world, Regions.CR81.value, Subregions.CR81Free.value, lambda state: True)

    connect_regions(world, Regions.CR82.value, Subregions.CR82Boss.value, lambda state: has_all_breath(state, world))
    connect_regions(world, Regions.CR82.value, "Victory", lambda state:  has_all_breath(state, world))

    world.multiworld.completion_condition[world.player] = lambda state: state.has("Victory", world.player, 1)

def has_ice_1(state, world):
    return state.has(Items.IceFairyScroll.value, world.player, 1)

def has_ice_2(state, world):
    return has_ice_1(state, world) and state.has(Items.SuperBreathMint.value, world.player, 1)

def has_fire_2(state, world):
    return state.has(Items.HotBananaPepper.value, world.player, 1)

def has_wind_2(state, world):
    return state.has(Items.MagicSpinningTop.value, world.player, 1)

def has_wind_3(state, world):
    return has_wind_2(state, world) and state.has(Items.MiniDynamo.value, world.player, 1)

def has_wind_x(state, world):
    return has_wind_2(state, world) or state.has(Items.MiniDynamo.value, world.player, 1)

def has_elec(state, world):
    return state.has(Items.MiniDynamo.value, world.player, 1)

def has_all_breath(state, world):
    return has_ice_2(state, world) and has_fire_2(state, world) and has_wind_2(state, world)

def has_red(state, world):
    return state.has(Items.LeftHalfOfTheRedChestKey.value, world.player, 1) and state.has(Items.RightHalfOfTheRedChestKey.value, world.player, 1)

def has_green(state, world):
    return state.has(Items.LeftHalfoftheGreenChestKey.value, world.player, 1) and state.has(Items.RightHalfOfTheGreenChestKey.value, world.player, 1)

def has_purple(state, world):
    return state.has(Items.LeftHalfOfThePurpleChestKey.value, world.player, 1) and state.has(Items.RightHalfOfThePurpleChestKey.value, world.player, 1)

def has_yellow(state, world):
    return state.has(Items.LeftHalfOfTheYellowChestKey.value, world.player, 1) and state.has(Items.RightHalfOfTheYellowChestKey.value, world.player, 1)

def has_lamp(state, world):
    return state.has(Items.YetiLamp.value, world.player, 1)

def has_slam(state, world):
    return state.has(Items.KangarooCarving.value, world.player, 1)

def has_escape(state, world):
    return state.has(Items.FairySpellBook.value, world.player, 1)

def has_ds_quest(state, world):
    return state.has(Items.SpyroActionFigure.value, world.player, 1) and state.has(Items.RiptoActionFigure.value, world.player, 1) and state.has(Items.BiancaActionFigure.value, world.player, 1) and state.has(Items.HunterActionFigure.value, world.player, 1) and state.has(Items.SheliaActionFigure.value, world.player, 1) and state.has(Items.SgtByrdActionFigure.value, world.player, 1) and state.has(Items.Agent9ActionFigure.value, world.player, 1)

def has_fl_quest(state, world):
    return state.has(Items.ExtensoGripAttachment.value, world.player, 1) and state.has(Items.BookBGoneStorageUnit.value, world.player, 1) and state.has(Items.NoSneezeDustingArmature.value, world.player, 1) and state.has(Items.EyeSpyBindingScanner.value, world.player, 1) and state.has(Items.QuickNQuietMotivatorUnit.value, world.player, 1) and state.has(Items.SupRSmartSortingModule.value, world.player, 1) and state.has(Items.DustyUserManual.value, world.player, 1)

def has_ys_quest(state, world):
    return state.has(Items.YetiHairClimbingRope.value, world.player, 1) and state.has(Items.LuckyClimbingHat.value, world.player, 1) and state.has(Items.BigLeftClimbingShoe.value, world.player, 1) and state.has(Items.AnotherLeftClimbingShoe.value, world.player, 1) and state.has(Items.HugeLeftClimbingGlove.value, world.player, 1) and state.has(Items.HugeRightClimbingGlove.value, world.player, 1) and state.has(Items.EnormousMountaineersAxe.value, world.player, 1)

def has_bb_quest(state, world):
    return state.has(Items.MedalOfLiberation.value, world.player, 1) and state.has(Items.TheArcticCross.value, world.player, 1) and state.has(Items.HerosHeartMedal.value, world.player, 1) and state.has(Items.MedalOfHonor.value, world.player, 1) and state.has(Items.VictoryMedal.value, world.player, 1) and state.has(Items.MilitaryCross.value, world.player, 1) and state.has(Items.TheOrderOfMerit.value, world.player, 1)

def has_tg_quest(state, world):
    return state.has(Items.MastersStethoscope.value, world.player, 1) and state.has(Items.MastersNailFile.value, world.player, 1) and state.has(Items.MastersHandDrill.value, world.player, 1) and state.has(Items.MastersCrowbar.value, world.player, 1) and state.has(Items.MastersSledgehammer.value, world.player, 1) and state.has(Items.MastersFuse.value, world.player, 1) and state.has(Items.MastersExplosives.value, world.player, 1)

def has_rh_quest(state, world):
    return state.has(Items.DragonStar.value, world.player, 1) and state.has(Items.YetiLettuce.value, world.player, 1) and state.has(Items.SnowLily.value, world.player, 1) and state.has(Items.ApeGrapes.value, world.player, 1) and state.has(Items.RoosRose.value, world.player, 1) and state.has(Items.MoneyTree.value, world.player, 1) and state.has(Items.SunspotBloom.value, world.player, 1)

def has_bs_quest(state, world):
    return state.has(Items.BananaRipeningAgent.value, world.player, 1) and state.has(Items.MagicBananaDust.value, world.player, 1) and state.has(Items.FlavorBooster.value, world.player, 1) and state.has(Items.SoilStabilizer.value, world.player, 1) and state.has(Items.PeelStrengthener.value, world.player, 1) and state.has(Items.BananaGroGrowth.value, world.player, 1) and state.has(Items.YellowDye5.value, world.player, 1)

def has_kh_quest(state, world):
    return state.has(Items.TheRooZettaStone.value, world.player, 1) and state.has(Items.KangarooHistory.value, world.player, 1) and state.has(Items.TheRooJewel.value, world.player, 1) and state.has(Items.Digeridoodle.value, world.player, 1) and state.has(Items.AncientTravelBrochure.value, world.player, 1) and state.has(Items.CeremonialBoomerang.value, world.player, 1) and state.has(Items.RooPottery.value, world.player, 1)

def has_cs_quest(state, world):
    return state.has(Items.HypnoticLightOrgan.value, world.player, 1) and state.has(Items.TotallyRetroUniform.value, world.player, 1) and state.has(Items.HipNeonTrophy.value, world.player, 1) and state.has(Items.WayCoolLavaLamp.value, world.player, 1) and state.has(Items.GroovyPainting.value, world.player, 1) and state.has(Items.WildSnowboard.value, world.player, 1) and state.has(Items.AwesomeDragonflyWing.value, world.player, 1)
