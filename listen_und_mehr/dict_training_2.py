import json

person = {
    "name": "Ben",
    "alter": 36,
    "job": "Sozialarbeiter"
}

for key in person:
    print(person['name'])
    break

for key, value in person.items():
    print(key, '\n------->', value, '<-------')

test = {'a': 1, 'b': 2}
namen = ['Ben', 'Alex', 'Lisa']

for name in namen:
    print(name)

for k, v, in test.items():
    print(v)



