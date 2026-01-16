import socket
import json
host = "127.0.0.1"

port = [80, 135, 443, 445, 3389]
critical_ports = [135, 445, 3389]
result_list = []

for p in port:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.3)
    result = s.connect_ex((host, p))
    s.close()
    if result == 0:
        result_list.append({'Port': p, 'Host': host, 'Status': 'OPEN'})
    else:
        result_list.append({'Port': p, 'Host': host, 'Status': 'CLOSED'})

dateiname = 'portical.json'
with open(dateiname, 'w', encoding='utf-8') as f:
    json.dump(result_list, f, ensure_ascii=False, indent=2)

with open(dateiname, 'r', encoding='utf-8') as f:
    watch = json.load(f)

kritisch = []
for p in watch:
        for c in critical_ports:
            if p['Port'] == c and p['Status'] == 'OPEN':
                kritisch.append({'Kritischer Port': p['Port'], 'Status': p['Status']})

print(kritisch)