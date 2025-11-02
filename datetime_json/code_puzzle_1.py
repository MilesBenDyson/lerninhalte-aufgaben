"""Yes Ben, genau das ist mein Stil! 🔧🧠
Wir bauen ein Tool wie ein geheimes Code-Puzzle – du kennst das Ziel nicht, aber jeder Schritt bringt uns näher. Und alles bleibt schön kompakt.
Bereit? Dann legen wir los:

🧩 Puzzle-Stück 1:

Erstelle eine Funktion, die den Nutzer nach einem Datum fragt.
Das Datum soll im Format TT.MM.JJ eingegeben werden und als datetime.date zurückgegeben werden."""

# Puzzlestück 1
import datetime


def abfragen_datum():
    while True:
        eingabe = input("Hey Cowboy! Welches Datum haben wir heute? Datum (TT.MM.JJ):    ")
        try:
            return datetime.datetime.strptime(eingabe, "%d.%m.%y").date()

        except ValueError:
            print("Oh, Deine Eingabe scheint ungültig zu sein, bitte versuche es erneut. ")
            continue
# Puzzlestück 2
def abfragen_uhrzeit():
    while True:
        try:
            eingabe = input("Jetzt sag doch bitte, wie spät es in Deiner Prärie ist?\nUhrzeit (hh:mm):    ")
            return datetime.datetime.strptime(eingabe, "%H:%M").time()
        except ValueError:
            print(f"Da brat mir doch einer 'nen Storch! Scheinbar ist Dir etwas Sand in die Augen geweht.\n{eingabe} kenne ich in dieser Gegend nicht. Bitte versuche es nochmal. ")

# Puzzlestück 3

def abfragen_zeitpunkt():
    datum = abfragen_datum()
    uhrzeit = abfragen_uhrzeit()
    return datetime.datetime.combine(datum, uhrzeit)

# Puzzlestück 4 / Puzzlestück 6
import json

def notiz_speichern():
    zeitpunkt = abfragen_zeitpunkt()
    notiz = input("Was möchtest Du Dir merken, Cowboy? Vielleicht einen neuen Steckbrief? ")
    neuer_eintrag = {"zeitpunkt": str(zeitpunkt), "notiz": notiz}
    try:
        with open("steckbrief.json", "r", encoding="utf-8") as f:
            file = json.load(f)
        if isinstance (file, dict):
            file = [file]


    except FileNotFoundError:
        file = []
    file.append(neuer_eintrag)

    with open("steckbrief.json", "w", encoding="utf-8") as f:
        json.dump(file, f, ensure_ascii=False, indent=2)
    print("Neuer Steckbrief wurde im Register des Wilden Westens vermerkt. ")

notiz_speichern()

# Puzzlestück 5
def zeige_steckbrief():
    try:
        with open("steckbrief.json", "r", encoding="utf-8") as f:
            file = json.load(f)
        print("\n Steckbrief des Wilden Westens")

        if isinstance(file, dict):
            file = [file]
        for i, w in enumerate(file, start=1):
            print(f"{i}. {w['zeitpunkt']}:")
            print(f"{w['notiz']}\n")

    except FileNotFoundError:
        print("Tut mir Leid, aber die Datei schien in den Weiten des Westens verloren gegangen zu sein. ")

zeige_steckbrief()