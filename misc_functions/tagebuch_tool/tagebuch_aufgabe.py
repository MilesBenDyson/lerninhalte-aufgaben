import sys
import datetime
import os

# Begrüßung
print("Hey grüß Dich, schön dass Du Dein persönliches Tagebuch gestartet hast.\nIch freue mich schon Dein Buch der Erinnerung zu füllen.\n\nDrücke Enter um fortzufahren ")
input()
# Menü
while True:
    menue = input("Wähle eine der folgenden Optionen:\n1. Eintrag für heute machen\n2. Letzten Eintrag lesen\n3. Textdatei anzeigen mit allen Einträgen\n4. Programm beenden\n")

    # 1.Eintrag heute
    if menue == "1":
        eintrag_heute = input("\nDann erzähl doch mal, ich bin sehr gespannt\n\n ")
        if eintrag_heute != "":
            print(f" Danke für Deine Worte:\n\n'{eintrag_heute}'\n\nwerde ich mir merken.\n\n")

            #Einträge als .txt speichern
            with open("Buch_der_Erinnerung.txt", "a", encoding="utf-8") as alle_einträge:
                zeitpunkt = datetime.datetime.now().strftime("%Y.%m.%d      %H:%M     ")
                alle_einträge.write(f"\n--- {zeitpunkt}")
                alle_einträge.write(eintrag_heute + "\n\n")

            # letzter Eintrag definieren
            with open("letzter_Eintrag.txt", "w", encoding="utf-8") as letzter_eintrag:
                letzter_eintrag.write(f"{eintrag_heute}\n\n")

            while True:
                entscheidung = input("Möchtest Du zum Menue zurück (m)? Oder Programm beenden (q)? ")

                if entscheidung == "m":
                    break

                elif entscheidung == "q":
                    print("Vielen Dank, bis zum nächsten mal ")
                    sys.exit()
                else:
                    print("Ungültige Eingabe mein Freund. Versuchs nochmal\n")
                    continue

        # falls kein Eintrag eingeben wird
        else:
                print("Du hast leider nichts eingegeben. Du gelangst zur Menüauswahl zurück ")

    # 2.Letzten Eintrag lesen
    elif menue == "2":
        try:
            with open("letzter_Eintrag.txt", "r", encoding="utf-8") as notiz:
                inhalt_notiz = notiz.read()
                print(f"Dein letzter Eintrag lautet:\n\n{inhalt_notiz}")

        except FileNotFoundError:
            print("Ohje, scheinbar hast Du noch keinen Eintrag gemacht. Egal, wähle als nächstes die 1 und hole es nach! :D ")



    # komplette Textdatei anzeigen
    elif menue == "3":
        print("Die Textdatei wird nun in Deinem Texteditor geöffnet ... ... ... ")
        os.startfile("Buch_der_Erinnerung.txt")
    # Beenden
    elif menue == "4":
        print("Alles klar, dann bis zum nächsten Mal. Auf wiedersehen :) ")
        sys.exit()

    else:
        print("Ungültige Eingabe mein Freund. Versuchs nochmal\n")