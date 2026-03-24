import json

dateiname = 'orders.json'

with open(dateiname, 'r', encoding='utf-8') as f:
    o = json.load(f)

zahlen_str = {'null': 0, 'eins': 1, 'zwei': 2, 'drei': 3, 'vier': 4, 'fünf': 5, 'sechs': 6, 'sieben': 7, 'acht': 8, 'neun': 9, 'zehn': 10}

total = 0

for b in o:
    try:
        anzahl = b['count']
    except KeyError:
      anzahl = 0
    try:
      preis = b['patty_price']
    except KeyError:
      preis = 0

    if anzahl == None:
        anzahl = 0
    if preis == None:
        preis = 0

    if isinstance(anzahl, str):
        for key, value in zahlen_str.items():
            if anzahl.lower() == key.lower():
                anzahl = float(value)
                break

    if isinstance(preis, str):
        for key, value in zahlen_str.items():
            if preis.lower() == key.lower():
                preis = value
                break

    try:
        anzahl, preis = float(anzahl), float(preis)
    except ValueError:
        print(f"{anzahl, preis} kann in keine Zahl umgewandelt werden")
        anzahl = 0
        preis = 0

    try:
        total += anzahl * preis
    except TypeError:
        print(f"{anzahl} ist vom Typ {type(anzahl)} und {preis} vom Typ {type(preis)}. Das kann nicht berechnet werden.")

print(total)


