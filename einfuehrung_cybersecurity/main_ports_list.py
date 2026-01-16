import socket
ports_info = [
    {"Port": 20, "Dienst": "FTP (Data)", "Bedeutung": "Datenkanal für Dateiübertragungen"},
    {"Port": 21, "Dienst": "FTP (Control)", "Bedeutung": "Steuerkanal für Dateiübertragungen"},
    {"Port": 22, "Dienst": "SSH", "Bedeutung": "Sichere Remote-Konsole"},
    {"Port": 23, "Dienst": "Telnet", "Bedeutung": "Unsichere Remote-Konsole (veraltet)"},
    {"Port": 25, "Dienst": "SMTP", "Bedeutung": "E-Mails versenden"},
    {"Port": 53, "Dienst": "DNS", "Bedeutung": "Namensauflösung (Domain → IP)"},
    {"Port": 80, "Dienst": "HTTP", "Bedeutung": "Unverschlüsseltes Web"},
    {"Port": 110, "Dienst": "POP3", "Bedeutung": "E-Mails abrufen"},
    {"Port": 143, "Dienst": "IMAP", "Bedeutung": "E-Mails synchron abrufen"},
    {"Port": 443, "Dienst": "HTTPS", "Bedeutung": "Verschlüsseltes Web"},
    {"Port": 445, "Dienst": "SMB", "Bedeutung": "Windows-Dateifreigaben"},
    {"Port": 3306, "Dienst": "MySQL", "Bedeutung": "Datenbankzugriff"},
    {"Port": 3389, "Dienst": "RDP", "Bedeutung": "Windows-Remote-Desktop"},
    {"Port": 5900, "Dienst": "VNC", "Bedeutung": "Bildschirmfreigabe"},
    {"Port": 8080, "Dienst": "HTTP-Alt", "Bedeutung": "Web-Interfaces, Proxys, Admin-Panels"},
]

host = '127.0.0.1'

offene_ports = []
for dict_ in ports_info:
    port = dict_['Port']
    door = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    door.settimeout(0.3)
    result = door.connect_ex((host, port))
    door.close()
    if result == 0:
        offene_ports.append(port)

if offene_ports:
    for p in offene_ports:
        print(f"Port {p} ist offen.")
else:
    print("Alle Ports sind geschlossen.")