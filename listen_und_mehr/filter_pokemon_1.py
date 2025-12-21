'''Guten Morgen, Ben! 😄☕
Na, bereit für die Pokémon-Filter-Challenge? 🔥🎮

Heute steht auf dem Trainingsplan:
🧩 Filtern, Gruppieren & Denken wie ein Pokédex!'''

import sys

pokemon = [
    {"name": "Glurak", "typ": "Feuer", "region": "Kanto"},
    {"name": "Turtok", "typ": "Wasser", "region": "Kanto"},
    {"name": "Bisaflor", "typ": "Pflanze", "region": "Kanto"},
    {"name": "Pikachu", "typ": "Elektro", "region": "Kanto"},
    {"name": "Feurigel", "typ": "Feuer", "region": "Johto"},
    {"name": "Impergator", "typ": "Wasser", "region": "Johto"},
    {"name": "Meganie", "typ": "Pflanze", "region": "Johto"},
    {"name": "Endivie", "typ": "Pflanze", "region": "Johto"},
    {"name": "Panferno", "typ": "Feuer", "region": "Sinnoh"},
    {"name": "Plinfa", "typ": "Wasser", "region": "Sinnoh"},
    {"name": "Chelterrar", "typ": "Pflanze", "region": "Sinnoh"},
    {"name": "Voltenso", "typ": "Elektro", "region": "Hoenn"},
    {"name": "Lohgock", "typ": "Feuer", "region": "Hoenn"},
    {"name": "Sumpex", "typ": "Wasser", "region": "Hoenn"}
]

abfrage_typ = input("Welchen Typ möchtest du filtern?")


typ = []
regionen = []
for i in pokemon:
    if abfrage_typ.lower() == i['typ'].lower():
        typ.append(i['name'])

if typ:
    print(f"Pokemon vom Typ '{abfrage_typ.capitalize()}' sind:\n{', '.join(typ)}.")
else:
    print(f"{abfrage_typ} ist kein gespeicherter Typ...")

abfrage_region = input("Möchtest du nun auch nach Region filtern? (j/n)")
if abfrage_region == "n":
    print("Danke, dann wird das Programm nun beendet... ")
    sys.exit()
elif abfrage_region == "j":
    for r in pokemon:
        if r['region'] not in regionen:
            regionen.append(r['region'])
    abfrage_region_2 = input(f"Welche Region soll zusätzlich zum Typ gefiltert werden?\n {'\n '.join(regionen)}")

    treffer = []
    for p in pokemon:
        if abfrage_region_2.lower() == p['region'].lower() and abfrage_typ.lower() == p['typ'].lower():
            treffer.append(p['name'])
    if treffer:
        print(f"In {abfrage_region_2.capitalize()} sind folgende Pokemon vom Typ {abfrage_typ.capitalize()}:\n{'\n'.join(treffer)}")




