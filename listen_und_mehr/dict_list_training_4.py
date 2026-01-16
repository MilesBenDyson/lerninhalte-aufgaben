geraete = [
    {"name": "Router", "status": "ok"},
    {"name": "Laptop", "status": "offline"},
    {"name": "Server", "status": "ok"},
    {"name": "Drucker", "status": "fehler"}
]

probleme = 0

for dict_ in geraete:
    print(f"{dict_['name']:10} ->   {dict_['status']}")
    if dict_['status'] != 'ok':
        probleme += 1

print(f"Insgesamt bestehen {probleme} Probleme.")

statistik = {}

for dict_ in geraete:
    status = dict_['status']
    if not status in statistik:
        statistik[status] = 0

    statistik[status] += 1

for status, anzahl in statistik.items():
    print(f"{status:8} : {anzahl}")

print(f"{'Test':30}Hallo")
