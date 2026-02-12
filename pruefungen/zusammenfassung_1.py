import json
from datetime import datetime
# 1
name = input("Wie heißt du?\nName:    ")
while True:
    try:
        stunden = int(input("Wieviele Stunden hast du gearbeitet?\n    "))
        minuten = int(input("Wieviele Restminuten?\nMinuten:    "))
        lohn = int(input("Wie hoch ist dein Stundenlohn?\nStundenlohn:    "))
        break
    except ValueError:
        frage_1 = input("Bitte gib bei Zeiten und Lohn nur Zahlen ein. Möchtest du fortfahren?\n(j/n)")
        if frage_1 == "j":
            continue
        else:
            print("Programm wird beendet ... ... ...")
            break

zeit = (stunden * 60 + minuten) / 60
umsatz = zeit * lohn

print(f"{name[0].upper()}{name[1:].lower()} hat {zeit} Stunden gearbeitet und {umsatz:.2f} € verdient.")

# 2
zahlen = [4, 9, 12, 3, 18, 7, 21]

count_10 = 0

for z in zahlen:
    if z > 10:
        count_10 += 1
        gerade_zahlen = [z for z in zahlen if z / 2 == int(z / 2) ]

print(count_10, gerade_zahlen)


# 3
text = "PythonIstStark2026"

print(f"{text[0:6]}\n{text[9:14]}\n{text[::-1]}\n{text[::2]}")


# 4
namen = ["Anna","Ben","Chris","Dora","Eli"]

suche = "Dora"

treffer = False

for n in namen:
    if n == suche:
        treffer = True
        break
if treffer:
    print(f"{suche} wurde gefunden.")
else:
    print(f"{suche} wurde nicht gefunden.")

# 5
zahlen = [3, 6, 9, 12, 15, 18, 21]

mehr_10 = [z * 2 for z in zahlen if z > 10]
print(mehr_10)

# 6
text = "Programmieren"
laenge = 10
if (w := len(text)) > laenge:
    print(w)'''
'''

# 7
satz = "  Hallo Coach ich lerne Python  "

print(f"{satz.upper()}")

# 8
daten = '''
[
 {"name":"alpha","ok":true},
 {"name":"beta","ok":false},
 {"name":"gamma","ok":true}
]
'''


p_daten = json.loads(daten)

ok_true = [d['name'] for d in p_daten if d['ok']]
print(ok_true)


# 9
jetzt = datetime.now()
heute = jetzt.date()
start = "06:30"
start_parse = datetime.strptime(start, "%H:%M").time()
heute_start = datetime.combine(heute, start_parse)

stunden_verstrichen = (jetzt - heute_start).total_seconds() / 3600

print(f"Seit {start} Uhr sind bis jetzt {stunden_verstrichen:.2f} Stunden vergangen.")

# 10
def stunden_zu_minuten(stunden):
    return int(stunden * 60)



# 11
liste = []

while True:
    try:
        wahl = int(input("1 = Zahl eingeben\n2 = Liste anzeigen\n3 = Beenden\n"))

        if wahl == 1:
            eingabe = int(input("Bitte gib eine Zahl ein.\n"))
        elif wahl == 2:
            print(liste)
        elif wahl == 3:
            print("Programm wird beendet")
            break
        else:
            print("Ungültige Eingabe.")
            continue
    except ValueError:
        print("Du darfst nur eine Zahl eingeben.")
        continue

# 12
daten = '{"a":1}'
obj = json.loads

print(obj["a"])

'''Meine Antwort: daten ist hier kein gültiges json Format. Es fehlen die [] '''