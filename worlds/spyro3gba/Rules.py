from typing import TYPE_CHECKING
from .Regions import connect_regions
from .Constants import Items, Hubs

if TYPE_CHECKING:
    from . import Spyro3GBAWorld

def set_rules(world: "Spyro3GBAWorld"):
    connect_regions(world, "Menu", Hubs.DS.value, lambda state: True)
    connect_regions(world, Hubs.DS.value, Hubs.FL.value, lambda state: True)
    connect_regions(world, Hubs.DS.value, Hubs.YS.value, lambda state: state.has(Items.FairySpellBook.value, world.player, 1))
    connect_regions(world, Hubs.DS.value, Hubs.BB.value, lambda state: state.has(Items.FairySpellBook.value, world.player, 1))
    connect_regions(world, Hubs.DS.value, Hubs.TG.value, lambda state: state.has(Items.FairySpellBook.value, world.player, 1) and (state.has(Items.YetiLamp.value, world.player, 1) or state.has(Items.SuperBreathMint.value, world.player, 1)))
    connect_regions(world, Hubs.DS.value, Hubs.RH.value, lambda state: state.has(Items.FairySpellBook.value, world.player, 1) and state.has(Items.YetiLamp.value, world.player, 1))
    connect_regions(world, Hubs.DS.value, Hubs.BS.value, lambda state: state.has(Items.IceFairyScroll.value, world.player, 1) and state.has(Items.SuperBreathMint.value, world.player, 1))
    connect_regions(world, Hubs.DS.value, Hubs.KH.value, lambda state: state.has(Items.FairySpellBook.value, world.player, 1) and state.has(Items.HotBananaPepper.value, world.player, 1) and state.has(Items.MagicSpinningTop.value, world.player, 1) and state.has(Items.SuperBreathMint.value, world.player, 1) and state.has(Items.IceFairyScroll.value, world.player, 1))
    connect_regions(world, Hubs.DS.value, Hubs.MM.value, lambda state: state.has(Items.FairySpellBook.value, world.player, 1) and state.has(Items.HotBananaPepper.value, world.player, 1) and state.has(Items.MagicSpinningTop.value, world.player, 1) and state.has(Items.YetiLamp.value, world.player, 1))
    connect_regions(world, Hubs.DS.value, Hubs.CS.value, lambda state: state.has(Items.FairySpellBook.value, world.player, 1) and state.has(Items.HotBananaPepper.value, world.player, 1) and state.has(Items.MagicSpinningTop.value, world.player, 1) and state.has(Items.YetiLamp.value, world.player, 1) and state.has(Items.MiniDynamo.value, world.player, 1))
    connect_regions(world, Hubs.DS.value, Hubs.PL.value, lambda state: state.has(Items.MiniDynamo.value, world.player, 1))
    connect_regions(world, Hubs.PL.value, Hubs.RC.value, lambda state: state.has(Items.MiniDynamo.value, world.player, 1))
    connect_regions(world, Hubs.RC.value, Hubs.CR.value, lambda state: state.has(Items.MiniDynamo.value, world.player, 1) and state.has(Items.KangarooCarving.value, world.player, 1))
    connect_regions(world, Hubs.CR.value, "Victory", lambda state:  state.has(Items.HotBananaPepper.value, world.player, 1) and state.has(Items.IceFairyScroll.value, world.player, 1) and state.has(Items.SuperBreathMint.value, world.player, 1) and state.has(Items.MiniDynamo.value, world.player, 1))

    world.multiworld.completion_condition[world.player] = lambda state: state.has("Victory", world.player, 1)