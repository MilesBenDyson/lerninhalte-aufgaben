"""Aufgabe: „Filmarchiv mit Uhrzeit“

Ziel:
Du erstellst ein kleines Programm, das eine Liste deiner Lieblingsfilme sammelt, mit Uhrzeit speichert und in einer JSON-Datei sichert.
Schritte:
Beim Start prüft das Programm, ob schon eine filme.json existiert.
Falls ja → lade die vorhandene Liste.
Falls nein → starte mit einer leeren Liste.
Frage den Nutzer nach neuen Filmeingaben (input).
Mit "stop" wird die Eingabe beendet.
Jeder neue Film soll als Dictionary gespeichert werden:

{"titel": "Filmname", "hinzugefügt_um": "2025-09-13 09:30"}

Am Ende:
speichere die gesamte Liste in filme.json.
gib die Filme nummeriert und mit Uhrzeit sortiert nach Titel aus."""


import json
import datetime

filmkiste = []

def abfrage():
    while True:
        abfrage = input("Nenne mir deine Lieblingsfilme. Wenn du nur Enter drückst ohne Text beendest du die Eingabe.\n")
        if abfrage == "":
            break
        else:
            zeitstempel = (datetime.datetime.now().strftime("%d.%m.%Y %H:%M Uhr"))
            filmkiste.append({"titel": abfrage, "hinzugefügt_um": zeitstempel})
def sortieren():
    titel_liste = [film["titel"] for film in filmkiste]
    titel_liste.sort()
    for i, titel in enumerate(titel_liste, start=1):
        for film in filmkiste:
            if film["titel"] == titel:
                print(f"{i}. {film['titel']} ({film['hinzugefügt_um']})")

try:
    with open("filme.json", "r", encoding="utf-8") as f:
        file = json.load(f)
        filmkiste = file
        print(f"Deine Filmliste bisher: {filmkiste}")
    abfrage()
    with open("filme.json", "w", encoding="utf-8") as f:
        json.dump(filmkiste, f, ensure_ascii=False, indent=2)
    sortieren()
except FileNotFoundError:
    abfrage()
    with open("filme.json", "w", encoding="utf-8") as f:
        json.dump(filmkiste, f, ensure_ascii=False, indent=2)
    sortieren()
