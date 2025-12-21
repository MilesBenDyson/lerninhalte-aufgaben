'''🔥 Aufgabe 3 – Flags in echter JSON-Datei + Fehlerbehandlung'''

import json
import sys
from json import JSONDecodeError
import os


personen = [
    {"name": "Alex", "level": 5},
    {"name": "Ben", "level": 12},
    {"name": "Lina", "level": 3},
    {"name": "August", "level": 6}
]
# json-datei erstellen, nach dem ersten Durchlauf, wird die Codezeile deaktiviert:
#erster Durchlauf erfolgt
#with open('personen.json', 'w', encoding='utf-8') as f:
    #json.dump(personen, f, ensure_ascii=False, indent=2)

dateipfad = "personen.json"

if os.path.exists(dateipfad):
    try:
        with open(dateipfad, 'r', encoding='utf-8') as f:
            json_personen = json.load(f)
    except JSONDecodeError:
        print("Die Datei scheint beschädigt zu sein und kann nicht geladen werden. ")
        json_personen = []
    except Exception:
        print("Unbekannter Fehler, Datei kann nicht geladen werden.")
        json_personen = []

    if not isinstance(json_personen, list):
        print("Achtung. Die Datei wurde gefunden, aber es ist keine gültige Liste.")
        json_personen = []
else:
    print("Die Datei existiert nicht. Programm wird beendet... ... ...")


if json_personen:
    abfrage_1 = input("Welchen Anfangsbuchstaben möchtest du suchen?\n")
    abfrage_level = input("Welches Level soll er mindestens haben?\n")

    gefunden = False
    ergebnis = None

    print(f"Okay, ich suche einen Namen mit dem Anfangsbuchstaben {abfrage_1} und der ein höheres Level als {abfrage_level} hat...\n")

    for n in json_personen:
        if n['name'].lower().startswith(abfrage_1.lower()) and n['level'] > int(abfrage_level):
            gefunden = True
            ergebnis = n
            break
    if gefunden:
        print(f"Treffer! Ich habe eine Person gefunden, die deinen Kriterien entspricht:\nName der mit '{abfrage_1}' anfängt und ein höheres Level als '{abfrage_level}' hat:\n\n{ergebnis} ")
    else:
        print("Kein Eintrag entsprechend deinen Kriterien gefunden. ")
        sys.exit()


else:
    print("Die Liste ist leer.")