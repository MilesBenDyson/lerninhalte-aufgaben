import json
import os
from json import JSONDecodeError
import string
pw = ['alexander', 'abms4088214', 'Abms409922!', 'r2j3rfu98ewdfr93429§)§(', '12345', 'ASJHDFH']

with open('pw2.json', 'w', encoding='utf-8') as f:
    json.dump(pw, f, ensure_ascii=False, indent=2)

if os.path.exists('pw2.json'):

    try:
        with open('pw2.json', 'r', encoding='utf-8') as f:
            pw_py = json.load(f)
    except ValueError:
        print("Das ist keine JSON-Datei")
        pw_py = []
    except JSONDecodeError:
        print("Die Datei konnte nicht gelesen werden.")
        pw_py = []

    if not pw_py:
        print("Die Liste ist leer, es können keine Passwörter getestet werden.")

ergebnisse = []

for p in pw_py:
    zeichenmenge = 0

    zeichen = []
    flag = False
    pawo = p
    laenge = len(p)
    zeichen.append(f'{laenge} Zeichen lang')
    if any(z.isupper() for z in p):
       zeichen.append("Großbuchtaben: ja")
       zeichenmenge += 26
    else:
        zeichen.append("Großbuchstaben: nein")
    if any(z.islower() for z in p):
        zeichen.append("Kleinbuchstaben: ja")
        zeichenmenge += 26
    else:
        zeichen.append("Kleinbuchstaben: nein")
    if any(s in string.punctuation for s in p):
        flag = True
    if flag:
        zeichen.append("Sonderzeichen: ja")
        zeichenmenge += len(string.punctuation)
    else:
        zeichen.append("Sonderzeichen: nein")
    if any(z.isdigit() for z in p):
        zeichen.append("Zahl: ja")
        zeichenmenge += 10
    else:
        zeichen.append("Zahl: nein")
    moegliche_kombis = zeichenmenge ** laenge
    zeit_sek = moegliche_kombis // 100000000
    stu = (zeit_sek % (3600*24)) // 3600
    minu = (zeit_sek % 3600) // 60
    tage = zeit_sek // (24*3600)
    gesamtzeit = f"{tage} Tage, {stu} Stunden und {minu} Minuten"
    bewertung = None
    if tage >= 1 and tage < 3:
        bewertung = "Das Passwort ist mittelstark"
    elif tage < 1:
        bewertung = "Das Passwort ist schwach"
    else:
        bewertung = "Das Passwort ist stark"

    p_set = {'Passwort': pawo, "Eigenschaften": zeichen, "Zeichenmenge": zeichenmenge, "Mögliche Kombis": moegliche_kombis, "Zeit für Versuche": gesamtzeit, 'Bewertung': bewertung}

    ergebnisse.append(p_set)
print(ergebnisse)






