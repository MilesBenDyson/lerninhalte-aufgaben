import sys
import os

einkaufsliste = []
# Begrüßung
print("Hallo, ich bin Dein Einkaufsassistent. Mit mir kannst Du eine \nEinkaufsliste erstellen und verwalten. Möchtest Du anfangen? ")
start = input("j/n ")
if start == "j":
    # Regeln (w = Wahlmenü; q = Programm abbrechen)
    print("Alles klar, dann erkläre ich Dir kurz Deine Möglichkeiten:")
    print("Du kannst jederzeit 'w' drücken, um ins Wahlmenü zu gelangen und \n 'q' um das Programm zu beenden. Wenn Du im Hauptmenü bist \n gib die Nummer des jeweiligen Bereiches ein." )
    quit = input("Drücke Enter ")
    if quit == "q":
        print("Programm wurde beendet ")
        sys.exit()
    else:

# Start - Wahlmenümenü: 1. Artikel hinzufügen 2. Artikel entfernen 3. Einkaufsliste anzeigen
        while True:
            wahlmenü = (input("Wahlmenü: \n1. Artikel hinzufügen \n2. Artikel entfernen \n3. Einkaufsliste anzeigen "))

            if wahlmenü == "1":
                while True:
                    hinzufügen = input("Welchen Artikel möchtest Du hinzufügen? ")
                    einkaufsliste.append(hinzufügen)
                    print(f"{hinzufügen} wurde Deiner Liste hinzugefügt. ")
                    hz = input("Möchtest Du einen weiteren Artikel hinzufügen (h) oder zurück zum Hauptmenü (z)? ")
                    if hz == "h":
                        continue
                    elif hz == "z":
                        break
                    elif hz == "q":
                        sys.exit()
                    elif hz == "w":
                        break
                    else:
                        print("Ungültige Eingabe")
                        break

            # 2. Welchen Artikel möchtest Du entfernen?
            elif wahlmenü == "2":
                while True:
                    entfernen = input("Welchen Artikel möchtest Du entfernen? ")
                    if entfernen in einkaufsliste:
                        einkaufsliste.remove(entfernen)
                        print(f"{entfernen} wurde aus Deiner Einkaufsliste entfernt. ")
                        mehrentfernen = input("Möchtest Du noch etwas entfernen (e) ? Oder ins Wahlmenü (w) ?")
                        if mehrentfernen == "e":
                            continue
                        elif mehrentfernen == "w":
                            break
                    else:
                        print("Artikel nicht gefunden. ")
                        break

                # 3. Liste Anzeigen & als Liste speichern
            elif wahlmenü == "3":
                print(einkaufsliste)
                x = input("Möchtest Du ins Wahlmenü zurück? Drücke 'w'. Möchtest Du die Einkaufsliste speichern? Drücke 's'" )
                if x == "w":
                    continue
                elif x == "s":
                    with open("einkaufsliste.txt", "w") as datei:
                        for item in einkaufsliste:
                            datei.write(item + "\n")
                    dateiname = "einkaufsliste.txt"
                    voller_pfad = os.path.join(os.getcwd(), dateiname)
                    print(f"Deine Einkaufsliste wurde abgespeichert als: {voller_pfad}")
                elif x == "q":
                    print("Programm wurde beendet ")
                    sys.exit()

            elif wahlmenü == "q":
                print("Programm wurde beendet ")
                sys.exit()
    # 1. Was möchtest Du hinzufügen?





# Begrüßung nicht anfangen
elif start == "n":
    print("Programm wurde beendet ")
    sys.exit()
else:
    print("Ungültige Eingabe!")
