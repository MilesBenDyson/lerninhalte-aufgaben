text = "Cybersecurity ist spannend"
if (l := len(text)) > 15:
    print(l)
else:
    print(f"{l} hat weniger als 16 Zeichen.")

name = "Server01"
status = "offline"
ip = "192.168.0.12"

geraet, zustand, adresse = name, status, ip

print(f"{geraet} ({adresse}) ist {zustand}")

import json

daten = '''
[
    {"name": "Router", "status": "ok"},
    {"name": "Laptop", "status": "offline"},
    {"name": "Server", "status": "ok"},
    {"name": "Drucker", "status": "fehler"}
]
'''
jl = json.loads(daten)

neue_liste = [d['name'] for d in jl if d['status'] != 'ok']

print(neue_liste)