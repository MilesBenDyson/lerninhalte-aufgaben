import json

faelle = [
    {"name": "Müller", "status": "offen",   "prio": 2},
    {"name": "Yilmaz", "status": "erledigt","prio": 1},
    {"name": "Schmidt","status": "offen",   "prio": 3},
    {"name": "Nguyen", "status": "offen",   "prio": 1},
]

count_status = [
    {'offen': 0, 'namen': []},
    {'erledigt': 0, 'namen': []}
]

for f in faelle:
    status = f['status']
    name = f['name']
    for c in count_status:
        if status in c:
            c[status] += 1
            c['namen'].append(name)
dateiname = 'listy.json'
with open(dateiname, 'w', encoding='utf-8') as f:
    json.dump(count_status, f, ensure_ascii=False, indent=2)

with open(dateiname, 'r', encoding='utf-8') as f:
    to_do = json.load(f)
print(to_do)


