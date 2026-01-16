import socket
import sys


print("Hallo, hier kannst du prüfen, welche Ports offen sind.")
while True:
    ports_anzahl = input("Bis zu welcher Grenze sollen die Ports überprüft werden? Gib eine Zahl zwischen 2 - 65001 ein.")
    try:
        zahl = int(ports_anzahl)
        ports_anzahl = zahl

    except ValueError:
        print("Bitte gib eine gültige Zahl ein.")
        continue

    if ports_anzahl > 65000 or ports_anzahl < 2:
        print(f"Deine Eingabe {ports_anzahl} befindet sich außerhalb des gültigen Bereiches. Bitte versuche es erneut.")
        continue
    break
while True:
    timeout_set = input("Setze ein Zeitlimit. Am besten eine Zahl zwischen 0.1 - 0.9")
    try:
        zeit = float(timeout_set)
        timeout_set = zeit
    except ValueError:
        print("Du musst eine Zahl eingeben. Versuche es erneut.")
        continue
    break

ports = range(1, ports_anzahl +1)

host = "127.0.0.1"

offene_ports = []

def klopfen(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(timeout_set)
    result = s.connect_ex((host, port))
    s.close()
    if result == 0:
        return port
    return None

dauer_sekunden = timeout_set*ports_anzahl
dauer_stunden = (dauer_sekunden / (60*60))
dauer_rest_minuten = ((dauer_sekunden % 3600) // 60)
dauer_rest_sekunden = dauer_sekunden % 60

print(f"Das Prüfen wird ca. {int(dauer_stunden)} Stunden, {int(dauer_rest_minuten)} Minuten und {dauer_rest_sekunden} Sekunden dauern.")
grundwert = ports_anzahl
teil = 0

while True:
    fortfahren = input("Möchtest du fortfahren?\n(j/n)").strip().lower()
    if fortfahren == 'j':
        last_percent = -1
        for p in ports:
            treffer = klopfen(host, p)
            if treffer is not None:
                offene_ports.append(treffer)
            teil += 1
            prozent_fertig = int(teil / grundwert * 100)
            if prozent_fertig != last_percent:
                last_percent = prozent_fertig
                print(f"\r{prozent_fertig}% fertig | Offene Ports bisher:{offene_ports}", end="", flush=True)
        print("\r100 Prozent fertig.".ljust(100), end="", flush=True)
        print()
    elif fortfahren == 'n':
        print("Das Programm wird nun beendet.")
        sys.exit()
    else:
        print(f"Deine Eingabe '{fortfahren}' ist ungültig. Bitte versuche es erneut.")
    break



if offene_ports:
    print(f"Folgende Ports sind derzeit offen:")
    for p in offene_ports:
        print(p)
else:
    print("Alle geprüften Ports sind geschlossen.")