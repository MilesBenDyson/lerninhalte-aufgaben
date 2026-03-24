import json
import datetime
import sys
import os

heute = datetime.date.today().strftime("%d.%m.%Y")
dateiname = f"aufgabenliste_vom_{heute}.json"


# Liste
aufgaben = []

# Begrüßung
print("Dein Aufgabentool wurde geladen. Wenn Du fertig bist, kannst Du mit 'stopp' das Programm beenden.\nÄnderungen sind dann automatisch gespeichert. ")

while True:

    aufgabe_datum_wahl = input("Möchtest Du eine neue Aufgabenliste erstellen? Drücke Enter\nAnsonsten gib das Datum Deiner Aufgabenliste ein (tt.mm.yyyy)\n")

    # bei Enter neue Liste erstellen mit aktuellem Datum
    if aufgabe_datum_wahl == "":
        with open(dateiname, "w") as datei_new:
            json.dump(aufgaben, datei_new, indent=2)
        print(f"Neue Aufgabenliste wurde unter dem Namen '{dateiname}' gespeichert")

        # Programm geht weiter mit neuer Liste
        while True:

            # Auswahl starten
            auswahl = input("1. Aufgabe hinzufügen\n2. Aufgabe abhaken\n3. Aufgabe löschen\n")

            # 1. Hinzufügen
            if auswahl == "1":
                while True:
                    hinzufügen =  input("Benenne Deine Aufgabe und drücke Enter. Mit der Eingabe von 'q' gelangst Du zur Auswahl zurück.\n")

                    # Eingabe zum Beenden des Programms & vorher speichern
                    if hinzufügen == "stopp":
                        with open(dateiname, "w") as datei_speichern:
                            json.dump(aufgaben, datei_speichern, indent=2)
                            print("Deine Liste wurde gespeichert. Bis zum nächsten mal. ")
                            sys.exit()

                    # zurück zur Auswahl
                    elif hinzufügen.lower() == "q":
                        break

                    elif hinzufügen.lower() == "stopp":
                        sys.exit()

                    # Aufgabe hinzufügen
                    else:
                        aufgaben.append({"To-Do": hinzufügen, "erledigt": False})
                        print(f"{hinzufügen} wurde Deiner Aufgabenliste hinzugefügt. ")
                        continue

            # 2. Abhaken
            elif auswahl == "2":

                # Schleife nicht vergessen, falls mehr abgehakt wird
                while True:
                    # wenn Liste leer ist
                    if not aufgaben:
                        print(f"Deine Aufgabenliste {dateiname} ist leer.")
                        break

                    # wenn Liste nicht leer ist, Abfrage
                    print("Welche Aufgabe möchtest Du abhaken? Gib die jeweilige Nummer ein: ")
                    for i, aufgabe in enumerate(aufgaben):
                        status = " ✅ " if aufgabe["erledigt"] else " ❌ "
                        print(f"{i + 1}. [{status}] {aufgabe['To-Do']}")

                    # start der Eingabe zur Auswahl zum Abhaken
                    nummer = input("Nummer der Aufgabe die Du abhaken möchtest:\n")
                    # Eingabe für zurück
                    if nummer.lower() == "q":
                        break
                        # Eingabe zum Beenden des Programms & vorher speichern
                    elif nummer.lower() == "stopp":
                        with open(dateiname, "w") as datei_speichern:
                            json.dump(aufgaben, datei_speichern, indent=2)
                            print("Deine Liste wurde gespeichert. Bis zum nächsten mal. ")
                            sys.exit()

                    # wenn der User Enter eingibt
                    elif nummer == "":
                        print("Du musst schon etwas eingeben :) ")
                        continue


                    # Eingabe zum Abhaken
                    if nummer.isdigit():
                        index = int(nummer) - 1
                        if 0 <= index < len(aufgaben):
                            aufgaben[index]["erledigt"] = True
                            print(f"Aufgabe '{aufgaben[index]['To-Do']}' wurde abgehakt ")
                            continue

                        else:
                            print("Ungültige Nummer")

                    else:
                        print("Bitte gib eine gültige Zahl ein.")



            # 3. Löschen
            elif auswahl == "3":
                löschen = input("Welche Aufgabe möchtest Du löschen?\n")

                # zurück zur Auswahl
                if löschen == "q":
                    break

                # Programm beenden
                elif löschen == "stopp":
                    sys.exit()

                elif löschen in [a["To-Do"] for a in aufgaben]:
                    aufgaben = [a for a in aufgaben if a["To-Do"] != löschen]
                    print(f"{löschen} wurde aus Deiner Aufgabenliste gelöscht. ")
                    break

                else:
                    print("Diese Aufgabe ist nicht vorhanden! Drücke Enter, um zur Auswahl zurück zu gelangen.\n")
                    input()








    # Aufgabenliste mit Input-Datum nicht vorhanden = Rückmeldung an User
    elif not os.path.exists(f"aufgabenliste_vom_{aufgabe_datum_wahl}.json"):
        print("Diese Liste ist nicht vorhanden.")
        input("Drücke Enter um zur ersten Auswahl zu gelangen\n")
        continue


    # Aufgabenliste mit Input-Datum vorhanden = laden + anzeigen
    elif os.path.exists(f"aufgabenliste_vom_{aufgabe_datum_wahl}.json"):

        dateiname = f"aufgabenliste_vom_{aufgabe_datum_wahl}.json" # "dateiname" ist einfach kürzer ^^

    elif os.path.exists(dateiname):

        with open(dateiname, "r") as datei_inputdatum:
             aufgaben = json.load(datei_inputdatum)
        print(f"Aufgabenliste vom {aufgabe_datum_wahl} wurde geladen. ")

        while True:

            # Auswahl starten
            auswahl = input("1. Aufgabe hinzufügen\n2. Aufgabe abhaken\n3. Aufgabe löschen\n")

            # 1. Hinzufügen
            if auswahl == "1":
                while True:
                    hinzufügen = input("Benenne Deine Aufgabe und drücke Enter. Mit der Eingabe von 'q' gelangst Du zur Auswahl zurück.\n")

                    # Eingabe zum Beenden des Programms
                    if hinzufügen == "stopp":
                        sys.exit()

                    # zurück zur Auswahl
                    elif hinzufügen == "q":
                        break

                    # Aufgabe hinzufügen
                    else:
                        aufgaben.append({"To-Do": hinzufügen, "erledigt": False})
                        with open(dateiname, "w") as speichern:
                            json.dump(aufgaben, speichern, indent=2)
                        print(f"{hinzufügen} wurde Deiner Aufgabenliste {datei_inputdatum}hinzugefügt. ")
                        continue

            # 2. Abhaken
            elif auswahl == "2":

                # Schleife nicht vergessen, falls mehr abgehakt wird
                while True:
                    # wenn Liste leer ist
                    if not aufgaben:
                        print(f"Deine Aufgabenliste vom {aufgabe_datum_wahl} ist leer.")
                        break

                    # wenn Liste nicht leer ist, Abfrage
                    print("Welche Aufgabe möchtest Du abhaken? Gib die jeweilige Nummer ein: ")
                    for i, aufgabe in enumerate(aufgaben):
                        status = " ✅ " if aufgabe["erledigt"] else " ❌ "
                        print(f"{i + 1}. [{status}] {aufgabe['To-Do']}")

                    # start der Eingabe zur Auswahl zum Abhaken
                    nummer = input("Nummer der Aufgabe die Du abhaken möchtest:\n")
                    # Eingabe für zurück
                    if nummer.lower() == "q":
                        break
                        # Eingabe zum Beenden des Programms & vorher speichern
                    elif nummer.lower() == "stopp":
                        with open(dateiname, "w") as datei_speichern:
                            json.dump(aufgaben, datei_speichern, indent=2)
                            print("Deine Liste wurde gespeichert. Bis zum nächsten mal. ")
                            sys.exit()

                    # wenn der User Enter eingibt
                    elif nummer == "":
                        print("Du musst schon etwas eingeben :) ")
                        continue


                    # Eingabe zum Abhaken
                    if nummer.isdigit():
                        index = int(nummer) - 1
                        if 0 <= index < len(aufgaben):
                            aufgaben[index]["erledigt"] = True
                            print(f"Aufgabe '{aufgaben[index]['To-Do']}' wurde abgehakt ")
                            continue

                        else:
                            print("Ungültige Nummer")

                    else:
                        print("Bitte gib eine gültige Zahl ein.")



            # 3. Löschen
            elif auswahl == "3":
                löschen = input("Welche Aufgabe möchtest Du löschen?\n").lower()

                # zurück zur Auswahl
                if löschen == "q":
                    break

                # Programm beenden
                elif löschen == "stopp":
                    sys.exit()

                # Aufgabe löschen
                elif löschen in [a["To-Do"] for a in aufgaben]:
                    aufgaben = [a for a in aufgaben if a["To-Do"] != löschen]
                    print(f"{löschen} wurde aus Deiner Aufgabenliste gelöscht. ")
                    break




    # Programm beenden
    elif aufgabe_datum_wahl == "stopp":
        sys.exit()










