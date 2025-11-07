'''🧩 Aufgabe: Aufgaben-Manager mit Kategorien

Erstelle ein Python-Programm namens aufgaben_manager.py, das Aufgaben speichert — aber diesmal nach Kategorie sortiert.'''

import json
import os
import datetime
import sys

# dateinamen einer variablen zuweisen
tasks = "aufgaben.json"

# prüfen ob eine json datei existiert & try falls beschädigt
if os.path.exists(tasks):
    with open(tasks, "r", encoding='utf-8') as f:
        try:
            liste = json.load(f)

        except JSONDecodeError:
            print("Datei ist beschädigt, es wird eine neue Datei erstellt ...")
            liste = []

# falls noch keine datei existiert
else:
    liste = []

# funktionen definieren:
# aktuelle uhrzeit
def zeit():
    z = datetime.datetime.now().time()
    return z.strftime("%H:%M Uhr")
# aktuelles datum
def datum():
    d = datetime.date.today()
    return d.strftime("%d.%m.%Y")
def hinzu(d, z, a, k):
    return {'datum': d, 'uhrzeit': z, 'aufgabe': a, 'kategorie': k}

# start des programms
print("Hallo AufgaBEN-Meister, wähle aus:\n")
# while true für auswahl arbeit - privat - sonstiges - anzeigen - beenden
while True:
    auswahl = input("1. Arbeit\n2. Privat\n3. Sonstiges\n4. Aufgaben anzeigen\n5. Programm beenden\n Wähle 1/2/3/4/5?\n")
    # arbeit 1
    # aufgabe arbeit hinzufügen
    if auswahl == "1":
        # while true für weiter/fertig später
        while True:
            a_hinzu = input("Welche Aufgabe möchtest du hinzufügen?\n")
            liste.append(hinzu(datum(), zeit(), a_hinzu, 'arbeit'))
            print(f"{a_hinzu} wurde deiner Liste hinzugefügt.")
            auswahl_2 = input("Möchtest du eine weitere Aufgabe hinzufügen? j/n\n")
            # weiter
            if auswahl_2 == "j":
                continue
            # fertig
            elif auswahl_2 == "n":
                break
                # ungültige eingabe
            else:
                print("Ungültige Eingabe. Versuche es erneut ... du gelangst nun zum Hauptmenü. ")
                break
    # privat 2
    # aufgabe privat hinzufügen
    elif auswahl == "2":
        # while true auswahl für weiter/fertig später
        while True:
            p_hinzu = input("Welche Aufgabe möchtest du bei 'PRIVAT' hinzufügen?\n")
            liste.append(hinzu(datum(), zeit(), p_hinzu, 'privat'))
            print(f"{p_hinzu} wurde deiner Liste hinzugefügt. ")
            auswahl_2 = input("Möchtest du noch etwas hinzufügen? (j/n)\n")
            # weiter
            if auswahl_2 == "j":
                continue
            # fertig
            elif auswahl_2 == "n":
                break
            # ungültige eingabe
            else:
                print("Eingabe ungültig. Versuche es erneut ... du gelangst nun zum Hauptmenü.")
                break
    # sonstiges 3
    elif auswahl == "3":
        while True:
    # aufgabe sonstiges hinzufügen
            s_hinzu = input("Welche Aufgabe möchtest du bei 'SONSTIGES' hinzufügen?\n")
            liste.append(hinzu(datum(), zeit(), s_hinzu, 'sonstiges'))
            print(f"{s_hinzu} wurde deiner Liste hinzugefügt. ")
            # while true auswahl weiter/fertig
            auswahl_2 = input("Möchtest du noch etwas hinzufügen?\nj/n")
            # weiter
            if auswahl_2 == "j":
                continue
            # fertig
            elif auswahl_2 == "n":
                break
            # ungültige eingabe
            else:
                print("Eingabe ungültig. Versuche es erneut ... du gelangst nun zum Hauptmenü.")
                break
    # anzeigen 4
    elif auswahl == "4":
        print(liste, "Drücke Enter")
        input()

    # beenden 5
    elif auswahl == "5":
        print("Vielen Dank, das Programm wird nun beendet ...")
        sys.exit()

    # falsche eingabe
    else:
        print("Tut mir Leid, deine Eingabe war ungültig. Du gelangst zum Hauptmenü ...")
        continue

'''🔧 Fehler und Verbesserungen

Encoding-Tippfehler:

with open(tasks, "r", encoding='ztf-8') as f:


→ muss heißen:

with open(tasks, "r", encoding='utf-8') as f:


JSONDecodeError importieren:
Du verwendest JSONDecodeError, musst es aber noch importieren:

from json import JSONDecodeError


Initiale Struktur:
Du hast aktuell liste = [], aber eigentlich soll die Datei kategoriebasiert aufgebaut sein.
Entweder du änderst es auf:

liste = {"arbeit": [], "privat": [], "sonstiges": []}


oder du lässt dein jetziges System so und sortierst erst bei der Anzeige nach Kategorie (siehe Punkt 5).

Daten speichern:
Nach jeder Änderung (z. B. nach einer neuen Aufgabe) solltest du die Datei neu speichern:

with open(tasks, "w", encoding='utf-8') as f:
    json.dump(liste, f, ensure_ascii=False, indent=2)


→ Das kann direkt nach jedem append() passieren, also innerhalb der jeweiligen Kategorie-Blöcke.

Schönere Anzeige:
Aktuell zeigt print(liste, "Drücke Enter") einfach den Roh-JSON an.
Besser:

kategorien = ["arbeit", "privat", "sonstiges"]
for k in kategorien:
    print(f"\n[{k.upper()}]")
    for eintrag in liste:
        if eintrag['kategorie'] == k:
            print(f"  - ({eintrag['datum']}, {eintrag['uhrzeit']}) {eintrag['aufgabe']}")
input("\nDrücke Enter, um zum Menü zurückzukehren...")'''