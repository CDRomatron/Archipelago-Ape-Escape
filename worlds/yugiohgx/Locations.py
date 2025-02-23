from typing import Optional, Dict, Set
from BaseClasses import Location
from worlds.yugiohgx.Strings import Cards, Duelists, gamename

base_location_id = 129000000


class YugiohGXLocation(Location):
    game: str = gamename


duel_location_table = {}

duelist_list = []
for x in Duelists:
    duelist_list.append(x.value)

for x in range(18):
    for y in range(10):
        duel_location_table[duelist_list[x]+' Win ' + str(y+1)] = (1001+y+(x*10))

card_location_table = {}

card_list = []
for x in Cards:
    card_list.append(x.value)

for x in range(1200):
    card_location_table[card_list[x]] = (10001+x)


location_table = {
    "Victory": 0
}

location_table.update(duel_location_table)
location_table.update(card_location_table)
