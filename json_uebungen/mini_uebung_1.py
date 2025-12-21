import json
import sys
import os
from json import JSONDecodeError



notiz = "C:\\Users\\bensc\\Desktop\\IT\\Python\\lerninhalte-aufgaben-uebungen\\json_uebungen\\notiz_1.json"


n = []

if os.path.exists(notiz):
    try:
        with open(notiz, 'r', encoding='utf-8') as f:
            n = json.load(f)

    except JSONDecodeError:
        print("Die Datei kann nicht gelesen werden. Es wird eine neue Datei geschrieben. ")
        n = []

else:
    print("Keine Datei vorhanden.\n")

if not isinstance(n, list):
    print("WARNUNG: Die Datei enthält kein gültiges Listenformat. Neue Liste wird erstellt.")
    n = []

# textmenü
while True:
    textmenue = input("1. Notiz laden\n2. Notiz schreiben\n3. Beenden\n")


    if textmenue == "1":
        print(n)

    elif textmenue == "2":
        while True:
            thema = input("Gib das Thema an, für was du eine Notiz machen möchtest.\n")
            notiz_eingabe = input("Danke, welche Notiz soll ich speichern?\n")
            neue_notiz = {'thema': thema, 'notiz': notiz_eingabe}
            n.append(neue_notiz)
            with open(notiz, 'w', encoding='utf-8') as f:
                json.dump(n, f, ensure_ascii=False, indent=2)
            abfrage_1 = input("Aufgabe hinzufügen oder zum Hauptmenü zurück?(h/z)\n")
            if abfrage_1 == "h":
                continue
            elif abfrage_1 == "z":
                break
            else:
                print("Falsche Eingabe, zur Strafe wird das Programm beendet ... ... ...")
                sys.exit()

    elif textmenue == "3":
        print("Tja, dann halt nicht. Programm wird beendet... ... ...\n")
        sys.exit()
    else:
        print("Eingabe ungültig. Versuche es ereneut.")
