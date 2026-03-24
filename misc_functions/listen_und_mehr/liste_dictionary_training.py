import json

favs = ["Pizza", "Haxe", "Rippchen"]
print(favs)

farben = {"rot": "warm", "blau": "kühl", "grün": "natürlich"}

print(farben)

if "Pizza" in favs:
    print("Pizza ist mit dabei!")
else:
    print("Leider keine Pizza vorhanden.")

for i, w in enumerate(favs, start=1):
    print(f"{i}. {w}")

with open("farben.json", "w", encoding="utf-8") as f:
    json.dump(farben, f, ensure_ascii=False, indent=2)

with open("farben.json", "r", encoding="utf-8") as f:
    file = json.load(f)

print(file)