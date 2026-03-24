import json
import datetime

def jetzt():
    jetzt_dt = datetime.datetime.now()
    return jetzt_dt.strftime("am %d.%m.%Y um %H:%M Uhr")

filme = [{"Titel": "Terminator 2", "hinzugefügt am": jetzt(), "Bewertung": ""}, {"Titel": "Rockstar", "hinzugefügt am": jetzt(), "Bewertung": "" }, {"Titel": "Police Academy", "hinzugefügt am": jetzt(), "Bewertung": ""} ]

def nummerieren(liste):
    for i, w in enumerate(liste, start=1):
        print(f"{i}. {w['Titel']} ({w['hinzugefügt am']}) {w['Bewertung']}")

with open("filme.json", "w", encoding="utf-8") as f:
    json.dump(filme, f, ensure_ascii=False, indent=5)

with open("filme.json", "r", encoding="utf-8") as f:
    file = json.load(f)

print("Hallo, willkommen zur Filmbewertung. Hier ist eine Liste der Top-3 Filme.\n")
nummerieren(file)

bewerten1 = input(f"Wie bewertest du {filme[0]['Titel']} (*-*****)?")
bewerten2 = input(f"Wie bewertest du {filme[1]['Titel']} (*-*****)?")
bewerten3 = input(f"Wie bewertest du {filme[2]['Titel']} (*-*****)?")

filme[0]["Bewertung"] = bewerten1
filme[1]["Bewertung"] = bewerten2
filme[2]["Bewertung"] = bewerten3

with open("filme.json", "w", encoding="utf-8") as f:
    json.dump(filme, f, ensure_ascii=False, indent=2)

with open("filme.json", "r", encoding="utf-8") as f:
    file = json.load(f)

nummerieren(file)