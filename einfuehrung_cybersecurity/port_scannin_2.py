import socket


port_limit = None

while True:
    port_abfrage = input("Bis zu einschließlich welchen Port soll gescannt werden?\n-Nur Ziffern eingeben-\n")
    if port_abfrage.isdigit() and (p := int(port_abfrage)) <= 1024:
        port_limit = p
        break
    else:
        print("Du hast keine Zahl eingegeben. Bitte versuche es erneut.")
        continue

port = range(1, port_limit + 1)
host = "127.0.0.1"

def ist_offen(host, port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.1)
        result = s.connect_ex((host, port))
        s.close()
        return result == 0


offene_ports_comprehension = [p for p in port if ist_offen(host, p)]

print(offene_ports_comprehension)
