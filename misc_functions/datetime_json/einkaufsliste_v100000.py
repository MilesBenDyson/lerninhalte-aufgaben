import json
import datetime
import sys
import os

einkaufsliste = []
datum = datetime.date.today()
# Funktion zum hinzufuegen
def hinzufuegen(liste):
    while True:
        artikel = input("Welchen Artikel möchtest du hinzufügen?\n")
        menge = input("Wieviel davon?\n")
        liste.append({"Artikel": artikel, "Menge": menge})
        print(f"Der Artikel {artikel} wurde hinzugefügt.")
        with open(f"einkaufsliste-{datum}.json", "w", encoding="utf-8") as f:
            json.dump(liste, f, ensure_ascii=False, indent=2)
        abfrage = input("Möchtest du einen weiteren Artikel hinzufügen? j/n\n")
        if abfrage == "j":
            continue
        elif abfrage == "n":
            break
        else:
            print("Eingabe nicht gültig. ")

# funktion zum nummerierten anzeigen
def anzeigen(liste):
    try:
        with open(f"einkaufsliste-{datum}.json", "r", encoding="utf-8") as f:
            liste = json.load(f)
            for i, w in enumerate(liste, start=1):
                print(f"{i}. {w['Artikel']} Anzahl: {w['Menge']}")
    except json.JSONDecodeError:
        print(
            f"Die Datei 'einkaufsliste-{datum}.json' scheint beschädigt zu sein, laden nicht möglich.\nEs wird eine neue Liste erstellt. ")
    except FileNotFoundError:
        print(
            f"Es existiert noch keine Liste mit dem Namen 'einkaufsliste-{datum}.json.\nEs wird eine neue Datei erstellt, wenn du einen Artikel hinzufügen möchtest. ")
#Hauptmenue
while True:
    print("Einkaufslistenprogramm wird geladen...\n--- Hautmenü ---\n\n")
    menue = input("1. Artikel hinzufügen\n2. Einkaufsliste von heute anzeigen\n3. Programm beenden\n4. Liste löschen\n1? 2? 3? 4? - ")

    if menue == "1":
        hinzufuegen(einkaufsliste)
    elif menue == "2":
        anzeigen(einkaufsliste)
        input("\nDrücke Enter um ins Menü zurückzukehren...")
    elif menue == "3":
        print("Programm wird nun beendet.")
        sys.exit()
    elif menue == "4":
        if os.path.exists(f"einkaufsliste-{datum}.json"):
            os.remove(f"einkaufsliste-{datum}.json")
            einkaufsliste.clear()
            print(f"einkaufsliste-{datum}.json wurde gelöscht")
        else:
            print("Die Datei ist nicht vorhanden.")
    else:
        print("Eingabe nicht erwartet, versuche es erneut.")