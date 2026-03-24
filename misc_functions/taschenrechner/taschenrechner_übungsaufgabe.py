# Extra-Feature (optional): Füge Datum und Uhrzeit hinzu bei jedem Rechenschritt
import datetime

# Begrüßung
print("Hallo, Du nutzt einen Taschenrechner mit den 4 Rechengrundarten.\nEs dürfen nur Zahlen und die Operatoren '+ | - | / | *' eingeben werden und statt ',' drückst Du '.'\nDeine Eingaben und die Ergebnisse werden mit Datum und Uhrzeit als .txt-Datei gespeichert.")
input("Drücke Enter, um fortzufahren...")


while True:
    # Fehlerbehandlung mit try/except
    try:
        eingabe = input("Was soll ich rechnen? ")

        # Operatoren dynamisch verarbeiten (+, -, *, /)
        ergebnis = eval(eingabe)

        # Extra-Feature (optional): Füge Datum und Uhrzeit hinzu bei jedem Rechenschritt
        current_time = datetime.datetime.now().strftime("%Y-%m-%d | %H:%M:%S")

        print(f"Dein Ergebnis lautet: {ergebnis} | {current_time}")
        # Textdatei erstellen und erweitern statt überschreiben ("a" statt "w")
        with open("rechenprotokoll.txt", "a") as file:
            file.write(f"{eingabe}={ergebnis} --> {current_time}\n")

    # Fehlerbehandlung mit try/except
    except Exception as fehler:
        print("Deine Eingabe konnte nicht berechnet werden. Bitte versuche es mit einer anderen Eingabe. ")
        with open("rechenprotokoll.txt", "a") as file:
            file.write(f"{eingabe} !ungueltiger Vorgang!")




