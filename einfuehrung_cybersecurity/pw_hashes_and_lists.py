'''🎯 Ziel der Aufgabe

Du simulierst einen simplen Offline-Angriff:

Eine Liste mit bekannten Hashes liegt vor

Du prüfst, welche Passwörter aus einer Kandidatenliste dazugehören

Das Ergebnis wird als JSON gespeichert

So arbeitest du wie ein Angreifer – aber kontrolliert und sauber.'''
import json
import hashlib
import sys
hashes = [
    "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8",
    "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824"
]

kandidaten = ["hallo", "123456", "password", "test", "admin"]

def hash_tool(p):
    #in bit umwandeln
    pw_bit = p.encode('utf-8')
    #hashen
    pw_hash = hashlib.sha256(pw_bit)
    #in hex wandeln
    pw_hex = pw_hash.hexdigest()
    return pw_hex


ergebnis = []
for h in hashes:
    gefunden = False
    for k in kandidaten:
        kan_hex = hash_tool(k)
        if kan_hex == h:
            gefunden = True
            ergebnis.append({'Hash': f'{h}: geknackt', 'Passwort': k})
            break
    if not gefunden:
        print(f"Keine  Übereinstimmung bei {h}")

if ergebnis:
    dateiname = 'crack_result.json'

    with open(dateiname, 'w', encoding='utf-8') as f:
        json.dump(ergebnis, f, ensure_ascii=False, indent=4)

    with open(dateiname, 'r', encoding='utf-8') as f:
        js_list = json.load(f)

    print(js_list)


