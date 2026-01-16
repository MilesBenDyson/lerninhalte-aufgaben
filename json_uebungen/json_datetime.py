import json
import datetime
import os
from json import JSONDecodeError

datei_pfad = 'logbuch.json'
logbuch = []

def write_list(datei, new):
    with open(datei, 'w', encoding='utf-8') as f:
        json.dump(new, f, ensure_ascii=False, indent=2)

def load_list(datei):
    with open(datei, 'r', encoding='utf-8') as f:
        logbuch = json.load(f)
        return logbuch


if os.path.exists(datei_pfad):
    try:
        logbuch = load_list(datei_pfad)
        print(f"{datei_pfad} wurde geladen\n...")
    except JSONDecodeError:
        print(f"Die Datei {datei_pfad} wurde zwar gefunden, kann aber nicht geladen werden. Es wird eine neue Datei erstellt.")
        logbuch = []
else:
    print(f"Keine Datei vorhanden, es wird eine neue erstellt.")
    logbuch = []

while True:
    text_input = input("Gib deinen Eintrag ein. Beenden mit 'q'.")
    if text_input != 'q':
        zeit = datetime.datetime.now().time()
        zeitstempel = zeit.strftime("%H:%M")
        logbuch.append({'eintrag': text_input, 'zeitpunkt': zeitstempel})
        write_list(datei_pfad, logbuch)
    else:
        print("Eingabe wird nun beendet.")
        break

def suche(liste, suchwort):
    treffer = []
    for i in liste:
        if suchwort == i['eintrag']:
            treffer.append(i)
    return treffer

suchfrage = input("Wonach möchtest du suchen?")
treffer = []
while True:
    if suchfrage:
        treffer = suche(logbuch, suchfrage)
        break
    else:
        print("Du musst mindestens ein Zeichen eingeben.")
print(treffer)