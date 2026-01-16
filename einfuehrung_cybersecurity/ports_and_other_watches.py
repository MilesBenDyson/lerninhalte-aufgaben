import socket

ports_statusliste = []
ports_offen = []


host = '127.0.0.1'
ports = [21, 22, 23,
         53,
         80, 443,
         135, 139, 445,
         3389,
         5900,
         8080]

dienste = [{'Port': 21, 'Dienst': 'FTP'},
           {'Port': 22, 'Dienst': 'SSH'},
           {'Port': 23, 'Dienst': 'Telnet'},
           {'Port': 53, 'Dienst': 'DNS'},
           {'Port': 80, 'Dienst': 'Web / HTTP(S)'},
           {'Port': 443, 'Dienst': 'Web / HTTP(S)'},
           {'Port': 135, 'Dienst': 'RPC, NetBIOS, SMB'},
           {'Port': 139, 'Dienst': 'RPC, NetBIOS, SMB'},
           {'Port': 445, 'Dienst': 'RPC, NetBIOS, SMB'},
           {'Port': 3389, 'Dienst': 'Remote Desktop'},
           {'Port': 5900, 'Dienst': 'VNC'},
           {'Port': 8080, 'Dienst': 'Alternative Webports'}]


for p in ports:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.3)
    result = s.connect_ex((host, p))
    dienst = None
    for d in dienste:
        if d['Port'] == p:
            dienst = d['Dienst']
    if result == 0:
        ports_offen.append({'Port offen': p, 'Dienst': dienst})
        ports_statusliste.append({'Port': p, 'Dienst': dienst, 'Status': 'OFFEN'})
    else:
        ports_statusliste.append({'Port': p, 'Dienst': dienst, 'Status': 'GESCHLOSSEN'})
    s.close()

for key in ports_statusliste:
    print(key)
