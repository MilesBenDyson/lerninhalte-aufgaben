'''🔥 HEUTIGE LERNSESSION: „gefunden = False“ verstehen & anwenden'''

import json

namen = ["Alex", "Ben", "Lina", "August"]

gefunden = False
abfrage_1 = input("Welchen Namen möchtest du suchen?")
for n in namen:
    if n.lower() == abfrage_1.lower():
        gefunden = True
        break
if gefunden:
    print(f"Der Name {abfrage_1} wurde gefunden. ")
else:
    print(f"Der Name {abfrage_1} konnte nicht gefunden werden. ")