import os
import sys
# Start
while True:

    print("Bis zu welcher Zahl möchtest Du die Quadratzahlen sehen? ")
    eingabe = int(input("Gib deine Zahl ein: "))

#operator
    for i in range(1,eingabe + 1,1):
        #Ausgabe
        print(f"{i}^2 = {i ** 2}")

    # als Txt speichern
    with open(f"quadratzahlen von 1 -{eingabe}.txt", "w") as datei:
        for i in range(1, eingabe + 1, 1):
            datei.write(f"{i}^2 = {i ** 2}\n")

    while True:
        print("Möchtest Du eine neue Zahl eingeben? (j / n) ")
        jn = input("j / n ? ")
        if jn == "j":
            break
        elif jn == "n":
            print("Programm wurde beendet ")
            sys.exit()
        else:
           print("Ungültige Eingabe ")
           break




