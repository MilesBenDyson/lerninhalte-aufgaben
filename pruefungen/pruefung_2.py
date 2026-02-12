'''TEIL A

A1
Was ist die Ausgabe?

zahlen = [2, 5, 8, 11, 14]

print(zahlen[1:4])
print(zahlen[-2:])
print(zahlen[::-2])


Meine Antwort:
5 8 11
11 14
11 5

A2
Warum ist dieser Code falsch?

text = "Python"

print(text[10])


✍️ Kurz erklären:

Meine Antwort:
Der Code ist falsch, weil text keine 11 Zeichen hat

Teil B
'''

import json

daten = '''
[
  {"task":"Lernen","dauer":45,"fertig":true},
  {"task":"Einkaufen","dauer":30,"fertig":false},
  {"task":"Sport","dauer":60,"fertig":true},
  {"task":"Putzen","dauer":40,"fertig":false},
  {"task":"Lesen","dauer":25,"fertig":true}
]
'''
'''B1
Lade die Daten.
'''

daten_p = json.loads(daten)

'''B2
Gib alle nicht fertigen Tasks aus, die länger als 30 Minuten dauern.
'''

for d in daten_p:
    task = d['task']
    dauer = d['dauer']
    fertig = d['fertig']
    if dauer > 30:
        print(f"Task: {task} ({dauer} min)")

'''Teil C'''
zeiten = ["08:10","09:45","10:30","12:15","14:00"]
'''C1
Wandle alle Zeiten in datetime um.
'''

from datetime import datetime
zeiten_datetime = [datetime.strptime(z, "%H:%M") for z in zeiten]

'''C2
Finde die erste Zeit nach 10:00
(Flag + break benutzen!)
'''

gesucht = datetime.strptime("10:00", "%H:%M")
gefunden = False
zeit_gefunden = None

for z in zeiten_datetime:
    if z > gesucht:
        gefunden = True
        zeit_gefunden = z
        break
if gefunden:
    print(f"Erste Zeit nach {gesucht.time()}: {zeit_gefunden.time()}")

'''Teil D
Dieser Code soll zählen, wie viele Werte > 50 sind:

werte = [20,55,60,10,80,45]

count = 0

for w in werte:
    if w > 50
        count + 1

print(count)'''

'''Meine Antwort:
Fehler 1:
bei count fehlt die Klammer. Richtig wäre count += 1
'''



'''🏁 GESAMTERGEBNIS
Teil	Punkte
A	8 / 10
B	15 / 25
C	25 / 25
D	10 / 20

➡️ Gesamt: 58 / 80 ≈ 72 %

Umgerechnet: Note 2 (gut) 👍💙

Unter Stress: Sehr ordentlich.'''
