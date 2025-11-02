import json
import datetime

import os

# erstmal eine json datei erstellen 'aufgaben.json

aufgabenliste = [
    {"titel": "Milch kaufen", "datum": "29.06.2025"},
    {"titel": "Brot kaufen", "datum": "30.06.2025"},
    {"titel": "Pfand wegbringen", "datum": "01.07.2025"},
    {"titel": "Kuchen backen", "datum": "04.07.2025"}
]

try:
    with open("aufgaben.json", "x") as f:
        json.dump(aufgabenliste, f, indent=2, ensure_ascii=False)

except FileExistsError:
    print("Datei gefunden, drücke Enter zum laden ")
    input("")

# aufgabenliste wird eingelesen
with open("aufgaben.json", "r") as f:
    inhalt = json.load(f)

# heute definieren
heute = datetime.date.today()

print("Deine  Aufgaben heute und die nächsten zwei Tage:\n")
for eintrag in inhalt:
    # Datum-Strin in echtes Datum umwandeln
    datum_text = eintrag["datum"]
    datum_objekt = datetime.datetime.strptime(datum_text, "%d.%m.%Y").date()

    # Aufgaben heute und die nächsten zwei Tage fidnen
    if datum_objekt == heute or datum_objekt == heute + datetime.timedelta(days=1) or datum_objekt == heute + datetime.timedelta(days=2):
        print(f"- [{datum_text}] {eintrag['titel']}")

