import json

while True:
    try:
        eingabe = input("Wieviele Krabbenburger soll ich machen?")
        patties = int(eingabe)
        break
    except ValueError:
        print(f"Bitte gib mir eine Anzahl Patrick! {eingabe} ist doch keine Zahl!")

bestellung = []

bestellung.append({'anzahl': patties, 'koch': 'Spongebob'})
dateiname = 'krosse_krabbe.json'
with open(dateiname, 'w', encoding='utf-8') as f:
    json.dump(bestellung, f, ensure_ascii=False, indent=2)



