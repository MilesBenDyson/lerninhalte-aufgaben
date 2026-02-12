'''TEIL A – Analyse & Indexing (15 Punkte)

Gegeben:

text = "ProgrammierenMachtStark2026"'''

'''A1

Gib aus:

print(text[0:11])
print(text[-4:])
print(text[::3])
print(text[::-1][0:6])'''

'''Meine Antwort:
Programmier
2026
oaieata26
6202kr
'''

'''A2

Erkläre kurz:

Was macht dieser Code?

a, *b, c = [10,20,30,40,50]'''

'''Meine Antwort:
Das ist eine Mehrfachzuweisung.  a ist in diesem Fall die erste Zahl, c die letzte. *b hat alle Zahlen in der Mitte.
'''

'''💻 TEIL B – JSON-Verarbeitung (25 Punkte)

Gegeben:'''

daten = '''
[
  {"name":"Anna","stunden":6,"fach":"Mathe"},
  {"name":"Ben","stunden":4,"fach":"Deutsch"},
  {"name":"Chris","stunden":8,"fach":"Mathe"},
  {"name":"Dora","stunden":5,"fach":"Englisch"},
  {"name":"Eli","stunden":7,"fach":"Mathe"},
  {"name":"Fynn","stunden":3,"fach":"Deutsch"}
]
'''

'''B1

Lade die Daten.'''

'''Meine Antwort:'''
import json

daten_p = json.loads(daten)

'''B2

Gib alle Personen aus, die:

mehr als 5 Stunden haben

UND Mathe belegen

Format:

Name: Chris (8h)'''

'''Meine Antwort:'''

for d in daten_p:
    name = d['name']
    stunden = d['stunden']
    fach = d['fach']
    if stunden > 5 and fach.lower() == 'mathe':
        print(f"Name: {name} ({stunden}h)")

'''B3
Erstelle eine Liste mit allen Namen, die weniger als 5 Stunden haben.'''

'''Meine Antwort:'''
weniger_5 = [n['name'] for n in daten_p if n['stunden'] < 5]

'''🔍 TEIL C – datetime & Zeitrechnung (25 Punkte)

Gegeben:'''

zeiten = [
  "07:45",
  "08:30",
  "09:10",
  "11:55",
  "13:20",
  "15:00"
]

'''C1

Wandle alle Zeiten in datetime um.'''

'''Meine Antwort:'''
from datetime import  datetime
zeiten_parse = [datetime.strptime(z, "%H:%M") for z in zeiten]

'''C2

Berechne die Gesamtdauer zwischen:

erste Zeit und letzte Zeit
(in Minuten)'''

'''Meine Antwort:'''

differenz = zeiten_parse[-1] - zeiten_parse[0]
differenz_minuten = differenz.total_seconds() // 60
print(f"Die Gesamtdauer zwischen der ersten und der letzten Zeit beträgt {int(differenz_minuten)} Minuten.")

'''C3

Finde die erste Zeit nach 09:00
→ mit Flag + break.'''

'''Meine Antwort:'''

grenze = datetime.strptime("9:00", "%H:%M")
erste_zeit = None
gefunden = False
for z in zeiten_parse:
    if z > grenze:
        gefunden = True
        erste_zeit = z.time()
        break
if gefunden:
    print(f"Die erste Zeit nach {grenze.time()} ist {erste_zeit}.")

'''🧠 TEIL D – Logik & Datenverarbeitung (20 Punkte)

Gegeben:'''

werte = [12,45,67,23,89,34,55,91,10,48]

'''D1

Zähle, wie viele Werte:

größer als 50

UND kleiner als 90 sind'''

'''Meine Antwort:'''

count = 0
for w in werte:
    if w > 50 and w < 90:
        count += 1
print(count)

'''D2
Finde den ersten Wert über 80
(Flag benutzen)'''

'''Meine Antwort:'''
wert_80 = None
flag = False
for w in werte:
    if w > 80:
        flag = True
        wert_80 = w
        break
if flag:
    print(f"Der erste Wert über 80 ist {wert_80}")

'''D3

Berechne den Durchschnitt aller Werte.'''

'''Meine Antwort:'''
summe_werte = 0
anzahl_werte = 0

for w in werte:
    summe_werte += w
    anzahl_werte += 1
durchschnitt = summe_werte / anzahl_werte
print(f"Der Durchschnitt aller Werte lautet {durchschnitt}.")

'''🧯 TEIL E – Debugging & Verständnis (15 Punkte)

Dieser Code soll alle Namen ausgeben, die älter als 30 sind:

import json

daten = '''
[
  {"name":"Anna","alter":28},
  {"name":"Ben","alter":36},
  {"name":"Chris","alter":22},
  {"name":"Dora","alter":41}
]
'''

obj = json.loads

for p in obj:
    if p["alter"] > 30
        print(p["name"])

Aufgabe:

1️⃣ Finde alle Fehler
2️⃣ Korrigiere den Code komplett'''

'''Meine Antwort:
Fehler 1: json.loads fehlen die Klammern und der dazugehörige Wert (daten).
Fehler 2: nach if ... 30 fehlt der Doppelpunkt

Korrektur:
obj = json.loads(daten)

for p in obj:
    if p["alter"] > 30:
        print(p["name"])


'''

