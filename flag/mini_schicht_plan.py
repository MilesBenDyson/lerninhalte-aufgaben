import json
import os
import sys
from json import JSONDecodeError
import datetime

p = [
  {"name": "Anna", "start": "08:00", "ende": "13:30"},
  {"name": "Ben", "start": "09:30", "ende": "18:00"},
  {"name": "Lisa", "start": "07:45", "ende": "12:15"}
]

# datei erstmal erstellen

datei = 'schicht.json'
#with open(datei, 'w', encoding='utf-8') as f:
    #json.dump(p, f, ensure_ascii=False, indent=2) --> datei wurde erstellt, daher wird die die Funktion nun deaktiviert

if os.path.exists(datei):
    try:
        with open(datei, 'r', encoding='utf-8') as f:
            datei_json = json.load(f)
    except JSONDecodeError:
        print("Die Datei konnte nicht sauber gelesen werden. Vermutlich kein gültiges JSON-Format.\n")
        datei_json = []
        if datei_json == []:
            print("Die Liste ist leer.")

def zeit_rechner(start, ende):
    ende_p = datetime.datetime.strptime(ende, "%H:%M").time()
    start_p = datetime.datetime.strptime(start, "%H:%M").time()
    start_kombi = datetime.datetime.combine(datetime.date.today(), start_p)
    ende_kombi = datetime.datetime.combine(datetime.date.today(), ende_p)
    differenz = ende_kombi - start_kombi
    return differenz.total_seconds()

such_abfrage = input("Welchen Namen suchst du?\n")
gefunden = False
name = None
start = None
ende = None

for n in datei_json:
    if such_abfrage.lower() == n['name'].lower():
        gefunden = True
        name = n['name']
        start = n['start']
        ende = n['ende']
        break



if gefunden:
    print(f"Treffer! Es wurde {name} gefunden. {name} hat um {start} Uhr angefangen und um {ende} Uhr aufgehört.\n")

    stunden = zeit_rechner(start, ende) // 3600
    minuten = (zeit_rechner(start, ende) % 3600) // 60
    print(f"{name} hat {int(stunden)} Stunden und {int(minuten)} Minuten gearbeitet.\n")


else:
    print(f"Tut mir Leid, aber eine Person mit dem Namen {such_abfrage} konnte nicht gefunden werden.\n")
    sys.exit()
