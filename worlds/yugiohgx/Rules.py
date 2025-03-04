from typing import TYPE_CHECKING
from .Regions import connect_regions
from .Strings import Items, Packs, Cards
from .Packs import *

if TYPE_CHECKING:
    from . import YuGiOhGXWorld


def set_rules(world: "YuGiOhGXWorld"):
    if world.options.cardsanity == 0x01:
        connect_regions(world, "Menu", "Slifer", lambda state: True)

        connect_regions(world, "Slifer", "Ra", lambda state: (cardsinsets(GetListOfPacks(state, world)) >= 400 or
                                                              world.options.logic == 0x02))

        connect_regions(world, "Ra", "Obelisk", lambda state:
            (cardsinsets(GetListOfPacks(state, world)) >= 800 or world.options.logic == 0x02)
            and state.has(Items.Timed.value, world.player, 1))

        connect_regions(world, "Obelisk", "Victory",
                        lambda state: state.has(Items.Wins.value, world.player, 1)
                                      and state.has(Items.Timed.value, world.player, 1)
                                      and state.has(Items.Written.value, world.player, 1)
                                      and (cardsinsets(GetListOfPacks(state, world)) == 1200
                                           or cardsinsets(GetListOfPacks(state, world)) == 1199
                                           and world.options.dorothy == 0x02))
    else:
        connect_regions(world, "Menu", "Slifer", lambda state: True)

        connect_regions(world, "Slifer", "Ra",
                        lambda state: getCardCountCardsanity(state, world) >= 400 or world.options.logic == 0x02)

        connect_regions(world, "Ra", "Obelisk", lambda state:
            (getCardCountCardsanity(state,world) >= 800 or world.options.logic == 0x02)
            and state.has(Items.Timed.value, world.player, 1))

        connect_regions(world, "Obelisk", "Victory",
                        lambda state: state.has(Items.Wins.value, world.player, 1)
                                      and state.has(Items.Timed.value, world.player, 1)
                                      and state.has(Items.Written.value, world.player, 1)
                                      and getCardCountCardsanity(state, world) == 1200)

        connect_regions(world, 'Slifer', Packs.Basic1A.value,
                        lambda state: state.has(Packs.Basic1A.value, world.player, 1))
        connect_regions(world, 'Slifer', Packs.Basic1B.value,
                        lambda state: state.has(Packs.Basic1B.value, world.player, 1))
        connect_regions(world, 'Slifer', Packs.Basic2A.value,
                        lambda state: state.has(Packs.Basic2A.value, world.player, 1))
        connect_regions(world, 'Slifer', Packs.Basic2B.value,
                        lambda state: state.has(Packs.Basic2B.value, world.player, 1))
        connect_regions(world, 'Slifer', Packs.Basic3A.value,
                        lambda state: state.has(Packs.Basic3A.value, world.player, 1))
        connect_regions(world, 'Slifer', Packs.Basic3B.value,
                        lambda state: state.has(Packs.Basic3B.value, world.player, 1))
        connect_regions(world, 'Slifer', Packs.Basic4A.value,
                        lambda state: state.has(Packs.Basic4A.value, world.player, 1))
        connect_regions(world, 'Slifer', Packs.Basic4B.value,
                        lambda state: state.has(Packs.Basic4B.value, world.player, 1))
        connect_regions(world, 'Slifer', Packs.Basic1C.value,
                        lambda state: state.has(Packs.Basic1C.value, world.player, 1))
        connect_regions(world, 'Slifer', Packs.Basic2C.value,
                        lambda state: state.has(Packs.Basic2C.value, world.player, 1))
        connect_regions(world, 'Slifer', Packs.Basic3C.value,
                        lambda state: state.has(Packs.Basic3C.value, world.player, 1))
        connect_regions(world, 'Slifer', Packs.Basic4C.value,
                        lambda state: state.has(Packs.Basic4C.value, world.player, 1))
        connect_regions(world, 'Slifer', Packs.EffectMonsters.value,
                        lambda state: state.has(Packs.EffectMonsters.value, world.player, 1))
        connect_regions(world, 'Slifer', Packs.VariousFields.value,
                        lambda state: state.has(Packs.VariousFields.value, world.player, 1))
        connect_regions(world, 'Slifer', Packs.Equipments.value,
                        lambda state: state.has(Packs.Equipments.value, world.player, 1))
        connect_regions(world, 'Slifer', Packs.Fusions.value,
                        lambda state: state.has(Packs.Fusions.value, world.player, 1))
        connect_regions(world, 'Slifer', Packs.Rituals.value,
                        lambda state: state.has(Packs.Rituals.value, world.player, 1))
        connect_regions(world, 'Slifer', Packs.ContinuousEffects.value,
                        lambda state: state.has(Packs.ContinuousEffects.value, world.player, 1))
        connect_regions(world, 'Slifer', Packs.SpellCollection1.value,
                        lambda state: state.has(Packs.SpellCollection1.value, world.player, 1))
        connect_regions(world, 'Slifer', Packs.SpellCollection2.value,
                        lambda state: state.has(Packs.SpellCollection2.value, world.player, 1))
        connect_regions(world, 'Slifer', Packs.TrapCollection1.value,
                        lambda state: state.has(Packs.TrapCollection1.value, world.player, 1))
        connect_regions(world, 'Slifer', Packs.TrapCollection2.value,
                        lambda state: state.has(Packs.TrapCollection2.value, world.player, 1))
        connect_regions(world, 'Slifer', Packs.Expert1.value,
                        lambda state: state.has(Packs.Expert1.value, world.player, 1))
        connect_regions(world, 'Slifer', Packs.Expert2.value,
                        lambda state: state.has(Packs.Expert2.value, world.player, 1))
        connect_regions(world, 'Slifer', Packs.Expert3.value,
                        lambda state: state.has(Packs.Expert3.value, world.player, 1))
        connect_regions(world, 'Slifer', Packs.Expert4.value,
                        lambda state: state.has(Packs.Expert4.value, world.player, 1))
        connect_regions(world, 'Slifer', Packs.PowerDestructions.value,
                        lambda state: state.has(Packs.PowerDestructions.value, world.player, 1))
        connect_regions(world, 'Slifer', Packs.EffectMonstersSpecial.value,
                        lambda state: state.has(Packs.EffectMonstersSpecial.value, world.player, 1))
        connect_regions(world, 'Slifer', Packs.MasterFusions.value,
                        lambda state: state.has(Packs.MasterFusions.value, world.player, 1))
        connect_regions(world, 'Slifer', Packs.SpellSpecial1.value,
                        lambda state: state.has(Packs.SpellSpecial1.value, world.player, 1))
        connect_regions(world, 'Slifer', Packs.SpellSpecial2.value,
                        lambda state: state.has(Packs.SpellSpecial2.value, world.player, 1))
        connect_regions(world, 'Slifer', Packs.TrapSpecial1.value,
                        lambda state: state.has(Packs.TrapSpecial1.value, world.player, 1))
        connect_regions(world, 'Slifer', Packs.TrapSpecial2.value,
                        lambda state: state.has(Packs.TrapSpecial2.value, world.player, 1))
        connect_regions(world, 'Slifer', Packs.TheHero.value,
                        lambda state: state.has(Packs.TheHero.value, world.player, 1))
        connect_regions(world, 'Slifer', Packs.LiveVehicles.value,
                        lambda state: state.has(Packs.LiveVehicles.value, world.player, 1))
        connect_regions(world, 'Slifer', Packs.ResidentsOfTheSea.value,
                        lambda state: state.has(Packs.ResidentsOfTheSea.value, world.player, 1))
        connect_regions(world, 'Slifer', Packs.FairyDance.value,
                        lambda state: state.has(Packs.FairyDance.value, world.player, 1))
        connect_regions(world, 'Slifer', Packs.InsectsNest.value,
                        lambda state: state.has(Packs.InsectsNest.value, world.player, 1))
        connect_regions(world, 'Slifer', Packs.DragonsInFlight.value,
                        lambda state: state.has(Packs.DragonsInFlight.value, world.player, 1))
        connect_regions(world, 'Slifer', Packs.BeastsInFight.value,
                        lambda state: state.has(Packs.BeastsInFight.value, world.player, 1))
        connect_regions(world, 'Slifer', Packs.BeQuick.value,
                        lambda state: state.has(Packs.BeQuick.value, world.player, 1))
        connect_regions(world, 'Slifer', Packs.SpecialWays.value,
                        lambda state: state.has(Packs.SpecialWays.value, world.player, 1))
        connect_regions(world, 'Slifer', Packs.InvitationToTheDark.value,
                        lambda state: state.has(Packs.InvitationToTheDark.value, world.player, 1))
        connect_regions(world, 'Slifer', Packs.Pyrogen.value,
                        lambda state: state.has(Packs.Pyrogen.value, world.player, 1))
        connect_regions(world, 'Slifer', Packs.TheWarriors.value,
                        lambda state: state.has(Packs.TheWarriors.value, world.player, 1))
        connect_regions(world, 'Slifer', Packs.TheMachines.value,
                        lambda state: state.has(Packs.TheMachines.value, world.player, 1))
        connect_regions(world, 'Slifer', Packs.SpellCastersDance.value,
                        lambda state: state.has(Packs.SpellCastersDance.value, world.player, 1))
        connect_regions(world, 'Slifer', Packs.DorothysGift.value,
                        lambda state: state.has(Packs.DorothysGift.value, world.player, 1) or world.options.dorothy == 0x02)

        pack_names = []
        card_names = []
        for pack in Packs:
            pack_names.append(pack.value)
        for card in Cards:
            card_names.append(card.value)
        for x in range(48):
            cards = get_all_packs(world.options.dorothy == 0x01)[x]
            for card in cards:
                connect_regions(world, pack_names[x], card_names[card - 1], lambda state: True)

    world.multiworld.completion_condition[world.player] = lambda state: state.has(Items.Victory.value, world.player, 1)


def cardsinsets(listOfExp):
    cardList = []
    if listOfExp is None:
        return 0
    for exp in listOfExp:
        cardList.extend(exp)

    cardSet = set(cardList)
    return len(cardSet)


def getCardCountCardsanity(state, world):
    count = 0
    for card in Cards:
        if state.has(card.value, world.player, 1):
            count += 1
    return count


def GetListOfPacks(state, world):
    packs = [starterDeck]
    count = 0
    for pack in Packs:
        if state.has(pack.value, world.player, 1):
            packs.append(get_all_packs(world.options.dorothy == 0x01)[count])
        count += 1
    return packs
