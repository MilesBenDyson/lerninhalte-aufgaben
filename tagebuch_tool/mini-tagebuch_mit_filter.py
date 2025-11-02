"""🧩 Aufgabe: „Mini-Tagebuch mit Filterfunktion“

Erstelle ein Programm, das Notizen (z. B. Gedanken oder Ereignisse) mit Datum und Uhrzeit speichert und sie anschließend nach Tag oder Schlüsselwort anzeigen kann. """

import datetime
import json
import os
import sys


# prüfen ob datei vorhanden ist
if os.path.exists("notizen.json"):
    print(f"Datei 'notizen.json' wurde gefunden und wird nun geladen ...")
    with open("notizen.json", "r", encoding='utf-8') as f:
        eintrag_liste = json.load(f)

else:
    print("Es wurde noch keine Datei angelegt. Es wird eine neue Datei erstellt.")
    eintrag_liste = []


# aktuelles datum holen
def datum_aktuell():
    d = datetime.date.today()
    return d.strftime("%d.%m.%Y")

# aktuelle uhrzeit holen
def uhrzeit_aktuell():
    z = datetime.datetime.now().time()
    return z.strftime("%H:%M Uhr")


# hauptmenue und auswahl
while True:
    print("1. Neue Notiz eintragen\n2. Notizen anzeigen\n3. Beenden")
    auswahl_1 = input("Wähle aus (1/2/3) oder drücke 'q' zum beenden\n")
    if auswahl_1 == "1":
        while True:
            eintrag = input("Schreibe nun deinen Eintrag:\n")
            eintrag_liste.append({'notiz': eintrag, 'datum': datum_aktuell(), 'uhrzeit': uhrzeit_aktuell()})
            with open('notizen.json', 'w', encoding='utf-8') as f:
                json.dump(eintrag_liste, f, ensure_ascii=False, indent=2)
                auswahl_eintrag = input("Möchtest du eine weitere Notiz schreiben? (j/n)")
                if auswahl_eintrag == "j":
                    continue
                elif auswahl_eintrag == "n":
                    break
                else:
                    print("Eingabe ungültig.")
                    break
    # Anzeigen Menü
    elif auswahl_1 == "2":

        while True:
            print("1. ALLE Notizen anzeigen\n2. Nach Datum filtern (Format: TT.MM.YYYY)\n3. Nach Stichwort suchen")
            auswahl_2 = input("Welche Option möchtest du nutzen? (1/2/3), drücke 'z' wenn du zum Hauptmenü zurück möchtest.\n")
            if auswahl_2 == "1":
                if eintrag_liste:
                    for i in eintrag_liste:
                            print(i['datum'], i['uhrzeit'], "Uhr:", i['notiz'])
                else:
                    print("Noch kein Eintrag vorhanden.")
            elif auswahl_2 == "2":
            # auswahl 2: datum_filter
                datum_filter = input("Gib das Datum (dd.mm.yyyy) ein, nachdem du suchen möchtest.\n")
                gefunden = False
                for i in eintrag_liste:
                    if i['datum'] == datum_filter:
                        print(i['datum'], i['uhrzeit'], "Uhr:", i['notiz'])
                        gefunden = True
                if not gefunden:
                    print(f"Es wurde kein Eintrag mit dem Datum {datum_filter} gefunden.")
            # stichwort_filter
            elif auswahl_2 == "3":
                gefunden = False
                wort_filter = input("Gib das Stichwort ein, nachdem du filtern möchtest:\n")
                for i in eintrag_liste:
                    if wort_filter.lower() in i['notiz'].lower():
                        print(i['datum'], i['uhrzeit'], "Uhr:", i['notiz'])
                        gefunden = True
                if not gefunden:
                    print("Keinen passenden Treffer gefunden.")
            elif auswahl_2 == "z":
                break
            else:
                print("Deine Eingabe ist leider ungültig, bitte versuche es erneut...")
    elif auswahl_1 == "3":
        sys.exit()
    elif auswahl_1 == "q":
        sys.exit()
    else:
        print("Deine Eingabe ist ungültig, bitte versuche es erneut...")







