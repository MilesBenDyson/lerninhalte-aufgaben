import json
import datetime
import os
import sys


def anzeige(liste):
    for i, w in enumerate(liste, start=1):
        print(f"{i}. {w['Titel']}")

try:
    with open("filmkiste.json", "r", encoding="utf-8") as f:
        file = json.load(f)
        filmkiste = file
    print(f"Liste wurde geladen:\n ")
    anzeige(filmkiste)

except FileNotFoundError:
    print("Noch keine Datei vorhanden. ")
    filmkiste = []

except json.JSONDecodeError:
    while True:
        user = input("-filmkiste.json- gefunden, Datei ist aber beschädigt. Soll die Datei gelöscht werden?\nj/n    ")
        if user.lower() == "j":
            os.remove("filmkiste.json")
            break
        elif user.lower() == "n":
            print("Laden der Datei nicht möglich. Das Programm wird beendet, damit die Datei nicht überschrieben wird. ")
            sys.exit()
        else:
            print("Eingabe ungültig. ")
    filmkiste = []

def date():
    return datetime.datetime.now()

def hinzu(liste, titel, genre, zeitpunkt):
    liste.append({"Titel": titel, "Genre": genre, "Zeitpunkt": zeitpunkt.strftime("%d.%m.%Y %H:%M Uhr")})

while True:
    titel = input("Hey Filmfreund, welchen Film sollen wir deiner Sammlung hinzufügen?\nNenne mir einen Titel: ")
    genre = input("Danke! Zu welchem Genre gehört der Film? ")
    print(f"{genre}? Das klingt interessant! Dann halten wir noch das Datum und die Uhrzeit fest:\n{date().strftime('%d.%m.%Y %H:%M Uhr')}")
    hinzu(filmkiste, titel, genre, date())
    abfrage = input("Möchtest du noch mehr eingeben? Dann drücke einfach ENTER. Wenn nicht, nutze eine beliebige andere Eingabe\n")
    if abfrage == "":
        continue
    else:
        break


with open("filmkiste.json", "w", encoding="utf-8") as f:
    json.dump(filmkiste, f, ensure_ascii=False, indent=4)

with open("filmkiste.json", "r", encoding="utf-8") as f:
    file = json.load(f)

print(file)


