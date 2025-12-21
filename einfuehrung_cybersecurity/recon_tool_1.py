# JSON Datei einlesen
import socket
import sys
import json
import os
import datetime

reportliste = []
COMMON_PORTS = [21, 22, 80, 443, 3306, 8080]


# datei laden
while True:
    dateiname = input("Nenne den Pfad zur Datei, die du laden möchtest.\n")
    if not dateiname:
        print("Du musst einen Dateinamen eingeben.")
        continue
    try:
        with open(dateiname, 'r', encoding='utf-8') as f:
            ip_liste = json.load(f)
        print(f"Datei {dateiname} erfolgreich geladen. ")
        break
    except FileNotFoundError:
        print("Die Datei ist nicht vorhanden.\n")
        while True:
            frage1 = input("Möchtest du eine neue Eingabe versuchen? j/n\n")
            if frage1 == "j":
                break
            elif frage1 == "n":
                print("Das Programm wird nun beendet.\n")
                sys.exit()
            else:
                print("Deine Eingabe ist ungültig.")
                continue

    except json.JSONDecodeError:
        print("Die Datei ist nicht lesbar.")

    except Exception:
        print("Ein unerwarteter Fehler ist aufgetreten. Das Programm wird nun beendet...")
        sys.exit()
# portcheck fuer jeden host
def check_port(ip, port, timeout=1.0):
    """gibt True zurück, wenn der Port offen ist, sonst False."""
    try:
        with socket.create_connection((ip, port), timeout=timeout):
            return True
    except (socket.timeout, ConnectionRefusedError, OSError):
        return False

print("\n--- Port-Check für jeden Host ---")



# IP auflösen über DNS
for host in ip_liste:
    try:
        ip = socket.gethostbyname(host)
        print(f"{host} heißt {ip}")

        ports_result = {}
        for port in COMMON_PORTS:
            offen = check_port(ip, port)
            status = "offen" if offen else "geschlossen"
            ports_result[str(port)] = status
            print(f" Port {port} ist {status}")
        reportliste.append({
            'host': host,
            'IP': ip,
            'ports': ports_result,

        })
    except socket.gaierror:
        print(f"{host} -> konnte nicht aufgelöst werden (DNS-Fehler)")
    except Exception as e:
        print(f"Bein Auflösen von {host} ist es zu einem unerwarteten Fehler gekommen ({e}).")
        sys.exit()

# report speichern mit datum und nummerierung

count = 1
datum = datetime.date.today()

while True:
    name = f"report_{datum}_{count}.json"
    if not os.path.exists(name):
        break
    count += 1

with open(f"report_{datum}_{count}.json", 'w', encoding='utf-8') as f:
    json.dump(reportliste, f, ensure_ascii=False, indent=2)

print(reportliste)
