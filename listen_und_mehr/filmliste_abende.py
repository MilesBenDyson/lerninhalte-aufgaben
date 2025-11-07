import json
import datetime

filmliste = [
  {"Titel": "Matrix", "Datum": "2025-10-05"},
  {"Titel": "Herr der Ringe", "Datum": "2025-10-12"},
  {"Titel": "Star Wars", "Datum": "2025-10-20"}
]

with open("filmtopf.json", "w", encoding='utf-8') as f:
    json.dump(filmliste, f, ensure_ascii=False, indent=2)

with open("filmtopf.json", "r", encoding='utf-8') as f:
    filme = json.load(f)

for w in filme:
    try:
        w['Datum'] = datetime.datetime.strptime(w['Datum'], '%Y-%m-%d').date()
        date_datum = w['Datum']
    except ValueError:
        print("Kein gültiges Datumsformat.")

heute = datetime.date.today()

zukunft = [w for w in filme if w['Datum'] > heute]
zukunft.sort(key=lambda x: x['Datum'])

if zukunft:
    naechster = zukunft[0]
titel_zukunft = ' , '.join([f['Titel'] for f in zukunft])
print(f"Der nächste Filmabend ist {naechster['Titel']} am {datetime.datetime.strftime(naechster['Datum'], '%d.%m.%Y')}. Zukünftige Filmabende: {titel_zukunft}")