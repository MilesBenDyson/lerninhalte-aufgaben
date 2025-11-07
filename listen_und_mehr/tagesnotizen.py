import json
import datetime
import os

if os.path.exists("tagebuch.json"):
    with open("tagebuch.json", "r", encoding='utf-8') as f:
        tagebuch = json.load(f)

else:
    tagebuch = {}

datum_heute = datetime.date.today()
datum_heute_str = datum_heute.strftime("%d.%m.%Y")

if datum_heute_str not in tagebuch:
    tagebuch[datum_heute_str] = []

abfrage = input("Was ist heute passiert?")

jetzt = datetime.datetime.now()
jetzt_str = jetzt.strftime("%d.%m.%Y %H:%M")

def einfuegen(liste, notiz, zeitpunkt):
    liste.append({"Notiz": notiz, "Zeitpunkt": zeitpunkt})

einfuegen(tagebuch[datum_heute_str], abfrage, jetzt_str)

with open("tagebuch.json", "w", encoding='utf-8') as f:
    json.dump(tagebuch, f, ensure_ascii=False, indent=2)

with open("tagebuch.json", "r", encoding='utf-8') as f:
    file = json.load(f)

print(file)


