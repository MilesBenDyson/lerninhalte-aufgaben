import datetime
import json
import sys



filmkiste = []

# Funktion Titel hinzufügen
def sammeln(liste):
    while True:
        titel = input("Nenne mir den Titel:\n")
        genre = input("Nenne mir das Genre:\n")
        bewertung = input("Wie bewertest du den Film? Verteile * (1-5):\n")
        hinzugefuegt_am = (datetime.datetime.now()).strftime("%d.%m.%Y um %H:%M:%S Uhr")
        liste.append({f"Titel": titel, "Genre": genre, "Bewertung": bewertung, "Hinzugefügt am": hinzugefuegt_am})
        # speichern json datei
        with open("filmkiste2.json", "w", encoding="utf-8") as f:
            json.dump(filmkiste, f, ensure_ascii=False, indent=2)
        abfrage = input("Möchtest du noch mehr hinzufügen?(j/n):\n")
        if abfrage == "j":
            continue
        elif abfrage == "n":
            break
        else:
            print("Eingabe nicht klar. ")
            break

# Funktion nummerierte Anzeige
def nummerieren(liste):
    for i, w in enumerate(liste, start=1):
        print(f"{i}. {w['Titel']} ({w['Genre']}) - Bewertung: {w['Bewertung']} - wurde hinzugefügt am {w['Hinzugefügt am']}")







# hauptmenü
while True:
    print("Hallo, was möchtest du tun?\n")
    abfrage = input("1. Film(e) sammeln\n2. Filme nummeriert ausgeben\n3. Programm beenden\n1, 2, 3:\n")
    if abfrage == "1":
        sammeln(filmkiste)

    elif abfrage == "2":
        try:
            # laden json datei
            with open("filmkiste2.json", "r", encoding="utf-8") as f:
                filme = json.load(f)
                filmkiste = filme
                nummerieren(filmkiste)
        except json.JSONDecodeError:
            print("Datei ist beschädigt.")
        except FileNotFoundError:
            print("Es ist noch keine Liste vorhanden.")


    elif abfrage == "3":
        print("Das Programm wird beendet...")
        sys.exit()
    else:
        print("Eingabe ungültig.")
        break

