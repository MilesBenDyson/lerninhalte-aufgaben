geraete = [
    {"name": "Router", "status": "ok"},
    {"name": "Laptop", "status": "offline"},
    {"name": "Server", "status": "ok"},
    {"name": "Drucker", "status": "fehler"},
]

for g in geraete:
    name = g['name']
    status = g['status']
    print(f"Gerät {name:10} -> {status}")

anzahl = {}
for g in geraete:
    status = g['status']
    if status not in anzahl:
        anzahl[status] = 0
    anzahl[status] += 1

for a, b in anzahl.items():
    print(f"{a:9}:{b}")

for g in geraete:
    if (f := g['status']) != 'ok':
        print(f"{g['name']:8} --> {f}")

logs = [
    ["10:01", "Router", "ok"],
    ["10:02", "Laptop", "offline"],
    ["10:03", "Server", "ok"],
    ["10:04", "Drucker", "fehler"],
]


for e in logs:
    zeit, name, status = e
    print(f"{zeit} Uhr {name:8} -> {status}")

events = [
    ["11:00", "Login", "ok"],
    ["11:05", "Login", "fehler"],
    ["11:07", "Scan", "ok"],
    ["11:10", "Backup", "fehler"],
    ["11:12", "Scan", "ok"],
]

fehler = 0

for e in events:
    zeit, aktion, status = e
    if status != 'ok':
        fehler += 1
        print(f"Fehler erkannt um {zeit} Uhr.")
    print(f"{zeit} Uhr - {aktion:8} -> {status}")
print(f"Es wurden {fehler} Fehler gefunden")
