
hosts = [
    {
        "ip": "192.168.0.10",
        "status": "online",
        "ports": [22, 80, 443]
    },
    {
        "ip": "192.168.0.11",
        "status": "offline",
        "ports": []
    },
    {
        "ip": "192.168.0.12",
        "status": "online",
        "ports": [21]
    }
]
host_count = 0
count_on = 0

ip_adressen = []
ip_on = []
host_ports = []
for h in hosts:
    ip_adressen.append(h['ip'])
    if h['status'] == 'online':
        host_count += 1
        ip_on.append(h['ip'])
        if h['ports']:
            for p in h['ports']:
                count_on += 1
    host_ports.append({'host': h['ip'], 'ports': h['ports']})


for element in host_ports:
        if element['ports']:
            print(f"Host {element['host']} hat die Ports {element['ports']}")

print(f"\n\nInsgesamt sind {count_on} Ports offen.\nEs gibt {host_count} Hosts, die online sind.")