
zahlen = [3, 7, 12, 4, 9, 18, 5]
grenze = 10

mehr_als_grenze = [z for z in zahlen if z > grenze]

print(mehr_als_grenze[0])

#mit flag

gefunden = False
h = 0
for z in zahlen:
    if z > grenze:
        gefunden = True
        h = z
        break

if gefunden:
    ergebnis = f"Erste Zahl über {grenze}: {h}"
else:
    ergebnis = f"Es wurde keine Zahl über {grenze} gefunden."
print(ergebnis)