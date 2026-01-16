import socket

host = '127.0.0.1'
port = [21, 22, 23, 53, 80, 110, 135, 139, 335, 443, 445, 3306, 3389, 5900, 8080]
geschlossen = []
kritisch = []
for i in port:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.settimeout(0.3)

    result = s.connect_ex((host, i))
    s.close()
    if result == 0:
        print(f"Port {i} ist offen.")
        kritisch.append({'Kritischer Port': i})
    else:
        print(f"Port {i} ist dicht.")
        geschlossen.append({'Geschlossene Ports': i})

print(kritisch)