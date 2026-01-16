systeme = [
    {"name": "Router", "status": "ok"},
    {"name": "Server", "status": "fehler"},
    {"name": "Drucker", "status": "offline"},
    {"name": "Laptop", "status": "ok"},
    {"name": "NAS", "status": "fehler"},
]

for dict_ in systeme:
    name = dict_['name']
    status = dict_['status']
    print(f"{name:7} -> {status}")

#zählen:
'''Ermittle:
wie viele Systeme insgesamt existieren
wie viele davon nicht den Status "ok" haben
Speichere diese Werte in sinnvollen Variablen.'''

#ich übe 3 Varianten:

#for-schleife mit zähler und separater if-bedingung
anzahl_systeme = 0
nicht_ok = 0
for system in systeme:
    status = system['status']
    anzahl_systeme += 1
    if status != 'ok':
        nicht_ok += 1
#len
anzahl_systeme_len = len(systeme)
#list-comprehension+walrus-operator+len
nicht_ok_count = [
    sys for sys in systeme if (status := sys['status']) != 'ok'
]
anzahl_nicht_ok = len(nicht_ok_count)
