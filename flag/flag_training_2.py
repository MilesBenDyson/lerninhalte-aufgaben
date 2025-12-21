'''🔥 Aufgabe 2 – Flags in Listen von Dictionaries'''

personen = [
    {"name": "Alex", "level": 5},
    {"name": "Ben", "level": 12},
    {"name": "Lina", "level": 3},
    {"name": "August", "level": 6}
]

gefunden = False
name = None

abfrage_1 = input("Welchen Anfangsbuchstaben möchtest du nutzen?\n")

print(f"Danke, ich suche einen Namen, der mit {abfrage_1} beginnt und ein höheres Level als 4 hat\n... ... ...\n... ... ...\n... ... ...")

for p in personen:
    if p['name'].lower().startswith(f'{abfrage_1.lower()}') and p['level'] > 4:
        gefunden = True
        name = p
        break

if gefunden:
    print(f"Treffer! Es wurde folgende Person mit dem Anfangsbuchstaben {abfrage_1} und einem höheren Level als 4 gefunden:\n\n{name}")

else:
    print("Tut mir Leid, die Suche verlief ohne Treffer.")