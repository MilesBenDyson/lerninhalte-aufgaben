import json
import hashlib
import string
import datetime
import random
import os

#Nutzerabfrage
nutzer = None
nutzer_flag = False
pw_nutzer = None
pw_flag = False
while True:
    new_log = input("Gib deinen Nutzernamen ein\n:    ")
    if new_log == "":
        print("Gib bitte mindestens ein Zeichen ein")
    else:
        nutzer = new_log
        nutzer_flag = True
        print(f"Danke, dein Nutzername lautet {new_log}.")
        while True:
            new_pw = input("Gib bitte dein Passwort ein\n:    ") #noch simpel gehalten
            if new_pw == "":
                print("Gib mindestens ein Zeichen ein")
            else:
                pw_nutzer = new_pw
                pw_flag = True
                print("Dein Passwort wurde gespeichert")
                break
    if nutzer_flag and pw_flag:
        break


zeichen_salt = string.ascii_lowercase + string.digits
salt = ""
for i in range(16):
    salt += random.choice(zeichen_salt)

def hasher(passwort, salt):
    kombi = passwort + salt
    b = kombi.encode('utf-8')
    h = hashlib.sha256(b)
    hexen = h.hexdigest()
    return hexen

hash_user = hasher(pw_nutzer, salt)

login_data = {'nutzername': nutzer, 'salt': salt, 'hash': hash_user}

dateiname = 'login.json'

if os.path.exists(dateiname):
    with open(dateiname, 'r', encoding='utf-8') as f:
        registriert = json.load(f)


else:
    registriert = []
registriert.append(login_data)

with open(dateiname, 'w', encoding='utf-8') as f:
    json.dump(registriert, f, ensure_ascii=False, indent=2)

with open(dateiname, 'r', encoding='utf-8') as f:
    registriert = json.load(f)

print("Hallo, bitte melde dich an:\n")
nutzername = input("Gib deinen Nutzernamen ein\n:    ")

nutzer_gefunden = False

for n in registriert:
    if nutzername == n['nutzername']:
        nutzer_gefunden = True
        print(f"Hallo {nutzername}")
        while True:
            passworteingabe = input("Bitte gib dein Passwort ein\n:    ")
            if n['hash'] == hasher(passworteingabe, n['salt']):
                print("Vielen Dank, login erfolgreich.")
                break
            else:
                print("Passwort ist nicht korrekt.")
                frage = input("Möchtest du es nochmal versuchen? j/n\n:    ")
                if frage == 'j':
                    continue
                elif frage == 'n':
                    break
                else:
                    print("Eingabe ungültig!")
if not nutzer_gefunden:
    print("Nutzername nicht vorhanden")