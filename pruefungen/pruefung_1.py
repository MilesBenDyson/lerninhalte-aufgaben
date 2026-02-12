'''
Teil A
A1
Was gibt dieser Code aus?'''

'''Meine Antwort:
Pruefung
2026
6202gnufeurP
'''

'''A2
Was ist der Unterschied?

len(liste)
vs.
liste.len()

✍️ Kurz erklären:
'''
'''Meine Antwort:
len(liste) gibt die Anzahl der Zeichen aus
'''

'''Teil B
B1
Lade die Daten in eine Python-Liste.
'''
'''Meine Antwort:'''
import json

daten = '''
[
    {"name": "Anna", "alter": 30, "stadt": "Köln"},
    {"name": "Ben", "alter": 36, "stadt": "Neuss"},
    {"name": "Chris", "alter": 22, "stadt": "Düsseldorf"},
    {"name": "Dora", "alter": 41, "stadt": "Krefeld"},
    {"name": "Eli", "alter": 29, "stadt": "Neuss"}
]
'''

daten_p = json.loads(daten)

'''B2
Gib alle Personen aus:

👉 älter als 30
👉 nicht aus Köln

Format:

Name (Alter) aus Stadt
'''

for n in daten_p:
    name = n['name']
    alter = n['alter']
    stadt = n['stadt']
    if alter > 30 and stadt.lower() != 'koeln':
        print(f"{name} ({alter}) aus {stadt}.")

'''Teil C
Schreibe ein Programm, das:

in einer Liste nach einem Namen sucht

ein Flag benutzt

abbricht, wenn gefunden
'''

namen = ["Anna", "Ben", "Chris", "Dora", "Eli"]
gesucht = "Dora"

gefunden = False

for n in namen:
    if gesucht == n:
        gefunden = True
        break
if gefunden:
    print(f"{gesucht} wurde gefunden.")
else:
    print(f"{gesucht} wurde nicht gefunden.")

'''Teil D'''
from datetime import datetime
start = "08:15"
ende = "12:45"

'''D1
Wandle beide Zeiten in datetime-Objekte um.
'''

start_d = datetime.strptime(start, "%H:%M")
ende_d = datetime.strptime(ende, "%H:%M")

'''D2
Berechne, wie viele Minuten dazwischen liegen.
'''

differenz = ende_d - start_d
differenz_sekunden = differenz.total_seconds()
differenz_minuten = differenz_sekunden // 60

print(f"Arbeitszeit: {int(differenz_minuten)} Minuten.")

'''Bonus
Fehler finden

Was ist hier falsch?

daten = '{"name":"Ben","alter":36}'

obj = json.loads

print(obj["name"])
'''

'''Meine Antwort:
Die Variable obj wird nicht richtig zugewiesen, da bei json.loads die Daten fehlen und die Klammer dazu. Dadurch kann das JSON Objekt nicht als String in Python geladen werden.
Richtig wäre:
'''
daten = '{"name":"Ben","alter":36}'

obj = json.loads(daten)

print(obj["name"])

