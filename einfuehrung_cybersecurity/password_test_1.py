'''Passwortstärke analysierst (Phase 1)

eine Mini-Brute-Force-Simulation vorbereitest

und JSON einbaust'''

import json
import sys
import os
passwords = [
    "1234567",
    "Passwort!",
    "pASSword1"
]

# datei erstellen:
dateiname = "pw.json"
#with open(dateiname, 'w', encoding='utf-8') as f:
    #json.dump(passwords, f, ensure_ascii=False, indent=2)
# datei wurde erstellt, 'open write' wird deaktiviert
python_file = []
if os.path.exists(dateiname):
    try:
        with open(dateiname, 'r', encoding='utf-8') as f:
            python_file = json.load(f)
            print(f"{dateiname} wurde geladen.")
    except json.JSONDecodeError:
        if not python_file:
            print("Die Liste ist leer.")
        else:
            print("Die Datei kann nicht als JSON-Datei gelesen werden.")

pw_ks_kg = []
pw_nz = []
pw_a = []


report = []

for i in python_file:
    laenge = False
    zahl = False
    kb = False
    gb = False
    sz = False
    sz_def = ["!","\\","§","$","%","&","/","(",")","=","?","´","+","*","-", "'", "^"]
    einschaetzung = None
    count = 0
    if len(i) >= 8:
        laenge = True
        count += 1
    if any(b.isdigit() for b in i):
        zahl = True
        count += 1
    if any(b.islower() for b in i):
        kb = True
        count += 1
    if any(b.isupper() for b in i):
        gb = True
        count += 1
    for s in sz_def:
        if s in i:
            sz = True
            count += 1
            break
    if count == 5:
        einschaetzung = "sehr gut"
    elif count > 3 and count < 5:
        einschaetzung = "gut"
    elif count < 3:
        einschaetzung = "schlecht"


    report.append({'passwort': i, 'laenge': laenge, 'zahlen': zahl, 'grossbuchstabe': gb, 'kleinbuchstaben': kb, 'sonderzeichen': sz, 'einschätzung': einschaetzung})

with open('report_1.json', 'w', encoding='utf-8') as f:
    json.dump(report, f, ensure_ascii=False, indent=2)

with open('report_1.json', 'r', encoding='utf-8') as f:
    repo = json.load(f)
print(repo)

for p in repo:
    if (p['grossbuchstabe'] or p['sonderzeichen']) != True:
        print(f"{p['passwort']} könnte mit einer einfachen Brute-Force Attacke aus [a-z0-9] geknackt werden.")
    if p['passwort'].isdigit():
        print(f"{p['passwort']} könnte super leicht mit einer Brute-Force Attacke geknackt werden.")
    if p['einschätzung'] == 'sehr gut':
        print(f"{p['passwort']} ist ein starkes Passwort. Das wird schwerer mit einer Brute-Force Attacke zu hacken sein.")



