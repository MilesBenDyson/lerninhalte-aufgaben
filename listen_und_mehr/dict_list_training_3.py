alerts = [
    {
        "id": 101,
        "type": "login_failed",
        "user": "admin",
        "ip": "10.0.0.5",
        "severity": "high"
    },
    {
        "id": 102,
        "type": "file_access",
        "user": "ben",
        "ip": "10.0.0.12",
        "severity": "low"
    },
    {
        "id": 103,
        "type": "login_failed",
        "user": "root",
        "ip": "10.0.0.8",
        "severity": "high"
    }
]

#Aufgabe 1: Iteriere über alerts und gib nur die id jedes Eintrags aus.
for dict in alerts:
    print(dict['id'])
#Aufgabe 2: Gib für jeden Eintrag einen Satz aus, z. B.:
# Benutzer admin hatte ein login_failed von 10.0.0.5
for dict in alerts:
    if dict['type'] == 'login_failed':
        print(f"Benutzer -{dict['user']}- hatte ein login_failed von {dict['ip']}")

#Aufgabe 3: Gib nur die IPs der Einträge aus, bei denen severity == "high".
high_ip = []
for dict in alerts:
    if dict['severity'] == 'high':
        high_ip.append(dict['ip'])
print("IPs mit hoher Severity:")
for element in high_ip:
    print(element)

#Aufgabe 4: Zähle, wie viele Alerts vom Typ "login_failed" existieren.
login_failed_count = 0
for dict in alerts:
    if dict['type'] == 'login_failed':
        login_failed_count += 1
print(f"Es gab {login_failed_count} login_failed-Versuche")
