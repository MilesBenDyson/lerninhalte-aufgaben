import json
farben = []

farben.append("rot")
farben.append("blau")
farben.append("grün")
farben.append("gelb")

print(farben)

bedeutung = {}

for f in farben:
    if f == "rot":
        bedeutung[f] = "warm"
    elif f  == "blau":
        bedeutung[f] = "kühl"
    elif f == "grün":
        bedeutung[f] = "natürlich"
    elif f == "gelb":
        bedeutung[f] = "mild"


print(bedeutung)

for f, b in bedeutung.items():
    print(f"Die Farbe {f} ist {b}.")

with open("farben.json", "w", encoding="utf-8") as f:
    json.dump(bedeutung, f, ensure_ascii=False, indent=2)

with open("farben.json", "r", encoding="utf-8") as f:
    file = json.load(f)

print(file)