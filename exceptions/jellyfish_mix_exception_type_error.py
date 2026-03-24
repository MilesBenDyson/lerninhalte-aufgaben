import json

zutat_1 = "Zucker"
zutat_2 = 5

zutaten = [
    zutat_1,
    zutat_2
]

dateiname = 'mix.json'

with open(dateiname, 'w', encoding='utf-8') as f:
    json.dump(zutaten, f, ensure_ascii=False, indent=2)

with open(dateiname, 'r', encoding='utf-8') as f:
    z = json.load(f)

try:
    mixer = z[0] + z[1]

except TypeError:
    print(f"Aber Patrick, {zutat_1} und {zutat_2} kann man doch nicht mischen!")
    mixer = None
result_datei = 'mix_result.json'

with open(result_datei, 'w', encoding='utf-8') as f:
    json.dump(mixer, f, ensure_ascii=False, indent=2)


