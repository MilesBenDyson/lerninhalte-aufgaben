"""Aufgabe: Einkaufsliste mit Speicherfunktion

Du sollst dein Einkaufslisten-Programm so erweitern, dass:
Neue Artikel hinzufügen
Der Nutzer gibt über input() Artikel ein, die der Liste hinzugefügt werden.
Wenn der Nutzer "stop" eingibt, endet die Eingabe.
Anzeige sortiert & nummeriert
Am Ende soll die Liste alphabetisch sortiert und mit Nummern ausgegeben werden.
JSON-Speicherung
Die finale Liste soll in einer JSON-Datei gespeichert werden (z. B. einkauf.json).
Achte darauf, dass sie als Liste gespeichert wird, nicht als String.
JSON-Laden
Wenn bereits eine einkauf.json existiert, soll dein Programm diese Liste beim Start laden und die neuen Artikel dort ergänzen.
Extra-Challenge (optional)
Baue eine Funktion, die beim Start überprüft, ob doppelte Einträge in der Liste vorkommen, und diese entfernt.
Gib dabei eine Meldung aus, welche Duplikate entfernt wurden."""

import json
import sys

einkaufsliste = []

    # 1.
print("Hallo, gib bitte die Artikel ein, die du heute einkaufen möchtest. Gib 'stop' ein, wenn du fertig bist.\n")
while True:
    eingabe = input("")
    if eingabe.lower() == "stop":
        break
    else:
        einkaufsliste.append(eingabe)
# 2.
for i, w in enumerate(sorted(einkaufsliste), start=1):
    print(f"{i}. {w}")
# 3. / 4.
try:
    with open("einkauf.json", "r", encoding="utf-8") as f:
        file = json.load(f)
    einkaufsliste.extend(file)

except FileNotFoundError:

    einkaufsliste = sorted(einkaufsliste)
    with open("einkauf.json", "w", encoding="utf-8") as f:
        json.dump(einkaufsliste, f, ensure_ascii=False, indent=2)

# 5.
bereinigte_liste = []

def dublette(liste1, liste2):
    for i in liste1:
        if i not in liste2:
            liste2.append(i)

dublette(einkaufsliste, bereinigte_liste)

print(bereinigte_liste)