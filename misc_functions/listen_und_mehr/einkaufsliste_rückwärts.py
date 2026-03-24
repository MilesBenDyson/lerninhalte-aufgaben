
einkauf = []

einkauf.append("Milch")
einkauf.append("Wasser")
einkauf.append("Brot")

for i, w in enumerate(einkauf[::-1], start=1):
    print(f"{i}. {w}")