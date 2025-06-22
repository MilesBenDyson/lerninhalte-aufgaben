import json
import datetime
import sys

# Liste
aufgaben = []

# Begrüßung
print("Dein Aufgabentool wurde geladen. Wenn Du fertig bist, kannst Du mit 'stopp' das Programm beenden.\nÄnderungen sind dann automatisch gespeichert. )"
while True:

    aufgabe_datum_wahl = input("Möchtest Du eine neue Aufgabenliste erstellen? Drücke Enter\nAnsonsten gib das Datum Deiner Aufgabenliste ein (tt.mm.yyyy) ")

    # bei Enter neue Liste erstellen mit aktuellem Datum
    if aufgabe_datum_wahl == "":
        with open("aufgaben-'aktuelles-Datum'.json", "w") as datei_new:
            json.dump(aufgaben, datei, indent=2)

        # Programm geht weiter mit neuer Liste
        while True:

            # Auswahl starten
            auswahl = input("1. Aufgabe hinzufügen\n2. Aufgabe abhaken\n3. Aufgabe löschen")

            # 1. Hinzufügen
            if auswahl == "1":
                while True:
                    hinzufügen =  input("Benenne Deine Aufgabe und drücke Enter. Mit der Eingabe von 'q' gelangst Du zur Auswahl zurück.")

                    # Eingabe zum Beenden des Programms
                    if hinzufügen == "stopp":
                        sys.exit()

                    # zurück zur Auswahl
                    elif hinzufügen == "q":
                        break

                    # Aufgabe hinzufügen
                    else:
                        datei_new.append(hinzufügen)
                        print(f"{hinzufügen} wurde Deiner Aufgabenliste hinzugefügt. ")
                        continue

            # 2. Abhaken
            elif auswahl == "2":


            # 3. Löschen
            elif auswahl == "3":
                löschen = input("Welche Aufgabe möchtest Du löschen? ")

                # zurück zur Auswahl
                if löschen == "q":
                    break

                # Programm beenden
                elif löschen == "stopp":
                    sys.exit()

                # Aufgabe löschen
                elif löschen in datei_new:
                    datei_new.remove(löschen)
                    print(f"{löschen} wurde aus Deiner Aufgabenliste gelöscht. ")
                    break








    # Aufgabenliste mit Input-Datum nicht vorhanden = Rückmeldung an User
    elif aufgabe_datum_wahl == #nicht vorhanden:
        print("Diese Liste ist nicht vorhanden.")
        input("Drücke Enter um zur ersten Auswahl zu gelangen ")
        break


    # Aufgabenliste mit Input-Datum vorhanden = laden + anzeigen
    elif datei_inputdatum vorhanden:

        with open("aufgaben-'datum'.json", "r") as datei_inputdatum:
             json.dump(aufgaben, datei, indent=2)

        while True:

            # Auswahl starten
            auswahl = input("1. Aufgabe hinzufügen\n2. Aufgabe abhaken\n3. Aufgabe löschen")

            # 1. Hinzufügen
            if auswahl == "1":
                while True:
                    hinzufügen = input("Benenne Deine Aufgabe und drücke Enter. Mit der Eingabe von 'q' gelangst Du zur Auswahl zurück.")

                    # Eingabe zum Beenden des Programms
                    if hinzufügen == "stopp":
                        sys.exit()

                    # zurück zur Auswahl
                    elif hinzufügen == "q":
                        break

                    # Aufgabe hinzufügen
                    else:
                        datei_inputdatum.append(hinzufügen)
                        print(f"{hinzufügen} wurde Deiner Aufgabenliste {datei_inputdatum}hinzugefügt. ")
                        continue

            # 2. Abhaken
            elif auswahl == "2":


            # 3. Löschen
            elif auswahl == "3":
                löschen = input("Welche Aufgabe möchtest Du löschen? ")

                # zurück zur Auswahl
                if löschen == "q":
                    break

                # Programm beenden
                elif löschen == "stopp":
                    sys.exit()

                # Aufgabe löschen
                elif löschen in datei_inputdatum:
                    datei_inputdatum.remove(löschen)
                    print(f"{löschen} wurde aus Deiner Aufgabenliste {datei_inputdatum} gelöscht. ")
                    break

    # Programm beenden
    elif aufgabe_datum_wahl == "stopp":
        sys.exit()










