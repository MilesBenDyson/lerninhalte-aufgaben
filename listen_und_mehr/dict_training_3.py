import json

#Übung 1
namen = ["Ben", "Lisa", "Peter"]

print(namen[0], '\n__________')
print(namen[-1], '\n__________')

for element in namen:
    print(element, '\n__________')

#Übung 2
person = {
    "name": "Ben",
    "alter": 36,
    "stadt": "Neuss"
}

print(person['name'])
print(person['alter'])
for key in person:
    print(key, '\n__________')
for key in person:
   print(person[key], '\n__________')

for key in person:
    print(key)

for key, value in person.items():
    print(key, '->', value)

#Übung 4
personen = [
    {"name": "Ben", "alter": 36},
    {"name": "Lisa", "alter": 34},
    {"name": "Peter", "alter": 45}
]

for key in personen:
    print(key['name'], key['alter'], '______________', f"{key['name']} ist {key['alter']} Jahre alt.")

#Übung 5 – Zugriff verstehen (Denkaufgabe)
#Beantworte ohne Code auszuführen:
#personen[1]["name"]
#❓ Was kommt raus und warum?
'''Antwort: -"Lisa", weil [1] das zweite dict meint und mit "name" auf den Wert des Keys "name" eingegangen wird-'''


