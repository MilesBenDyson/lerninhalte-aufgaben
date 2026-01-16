#Aufgabe1:
'''Ziel:
Du schreibst ein kleines Python-Skript, das auf 127.0.0.1 (dein eigener PC) prüft,
welche Ports in einem kleinen Bereich offen sind.'''

'''Rahmen:
Nutze das Modul socket
Prüfe z. B. die Ports 20 bis 100
Für jeden Port:
Versuche eine Verbindung
Wenn sie gelingt → „offen“
Wenn nicht → ignorieren oder als „geschlossen“ markieren
Erzeuge ein Socket-Objekt
Setze ein kurzes Timeout (z. B. 0.2 Sekunden)
Iteriere über einen Port-Bereich
Versuche mit connect_ex() eine Verbindung
Wenn das Ergebnis 0 ist → Port ist offen'''

import socket

ports = [p for p in range(20, 101)]
host = "127.0.0.1"
offene_ports = []
for p in ports:
    door = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    door.settimeout(0.3)
    result = door.connect_ex((host, p))
    door.close()
    if result == 0:
        offene_ports.append(p)
if offene_ports:
    for p in offene_ports:
        print(f"Port {p} ist offen.")
else:
    print(f"Die Ports {ports} sind alle geschlossen.")