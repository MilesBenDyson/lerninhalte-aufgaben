import json


daten = '''
[
    {"name": "alpha", "ok": true},
    {"name": "beta", "ok": false},
    {"name": "gamma", "ok": true},
    {"name": "delta", "ok": false}
]
'''


text = "IndexingIstMagie"

print(text[:8], text[11:], text[::-1])

if (l := len(text)) > 12:
    print(f"Text ist lang genug ({l} Zeichen)")

daten_python = json.loads(daten)


false_list = [l['name'] for l in daten_python if not l['ok']]
print(false_list)

daten = ["Ben", 36, "Neuss", "Sozialarbeiter"]

name, alter, ort, beruf = daten
print(name)
print(alter)
print(ort)
print(beruf)

werte = [10, 20, 30, 40, 50]

a, *rest, b  = werte
print(a, rest, b)