"""""Ziel

Ein kleines CLI-Tool, das mehrere Arbeits- und Pausen-Blöcke erfasst, Tageszeiten korrekt summiert (auch über Mitternacht), alles in JSON speichert und eine kurze TXT-Zusammenfassung ausgibt."""

import datetime
import json
import sys
import locale

locale.setlocale(locale.LC_ALL, "de_DE.utf-8")
bloecke = []
# Begrüßung und Einführung
print("Willkommen bei Deinem individuellen Zeiterfassungsprogramm. Damit Deine Arbeitszeit korrekt abgerechnet werden kann, \ngib bitte Deine Zeiten ein, wann Du gearbeitet und wann Du Pause gemacht hast.\nWenn Du die Eingabe leer lässt und Enter drückst, wird das Programm beendet und die erfassten Daten in eine Liste gespeichert. ")

# Abfragen des Datums für den jeweiligen Arbeitstag
while True:
    abfragen_datum = input("Gib bitte das Datum ein, für wann die Zeiten erfasst werden soll.\nDatum(dd.mm.yy):    ")
    try:
        parsen_datum = datetime.datetime.strptime(abfragen_datum, "%d.%m.%y").date()
        break
    except ValueError:
        print(f"Tut mir Leid, aber Deine Eingabe {abfragen_datum} ist für dieses Programm keine gültige Eingabe. Bitte versuche es erneut. ")
        continue
print(f"Danke, jetzt kannst Du nacheinander die Zeiten eingeben, wann Du am {abfragen_datum} gearbeitet und wann Du Pause gemacht hast. ")

# Funktion für Uhrzeiteingabe mit datetime kombinieren und Test
def abfragen_uhrzeit(datum, zeit):
    try:
        parsen_date = datetime.datetime.strptime(datum, "%d.%m.%y").date()
        datum = parsen_date
        parsen_uhrzeit = datetime.datetime.combine(datum, datetime.datetime.strptime(zeit, "%H:%M").time())

    except (ValueError, TypeError):
        parsen_uhrzeit = datetime.datetime.combine(datum, datetime.datetime.strptime(zeit, "%H:%M").time())

    return parsen_uhrzeit

while True:
    abfragen_zeiten = input("Arbeitsbeginn (h:m):    ")
    try:
        #1. Arbeitsblock
        arbeitsbeginn1 = abfragen_uhrzeit(parsen_datum, abfragen_zeiten)
        print(f"Danke, um {abfragen_zeiten} Uhr hast Du also angefangen. ")
        # es geht weiter in der Schleife mit der nächsten Abfrage
        abfragen_pauseanfang_datum1 = input("Wann hast Du Deine Pause angefangen?\nDatum Pausenbeginn (d.m.yy):    ")
        abfragen_pausenanfang_uhrzeit1 = input("Uhrzeit(h:m):    ")
        pausenbeginn1 = abfragen_uhrzeit(abfragen_pauseanfang_datum1, abfragen_pausenanfang_uhrzeit1)

        print(f"Danke, am {abfragen_pauseanfang_datum1} um {abfragen_pausenanfang_uhrzeit1} Uhr hast Du Deine Pause angefangen. ")
        abfragen_pausenende_datum1 = input("Wann hast Du Deine Pause beendet?\nDatum:    ")
        abfragen_pausenende_uhrzeit1 = input("Uhrzeit:    ")
        pausenende1 = abfragen_uhrzeit(abfragen_pausenende_datum1, abfragen_pausenende_uhrzeit1)

        print(f"Sehr gut, am {abfragen_pausenende_datum1} um {abfragen_pausenende_uhrzeit1} Uhr hast Du Deine Pause beendet.")
        choice = input("Wenn Du fertig bist, drücke einfach -ENTER-. Wenn Du weitere Zeiten eingeben willst, gib 'weiter' ein.\n")

        # Zeiten initialisieren
        def zeit_sek(start, ende):
            return int((ende - start).total_seconds())

        arbeitszeit_sek = zeit_sek(arbeitsbeginn1, pausenbeginn1)
        pausenzeit_sek = zeit_sek(pausenbeginn1, pausenende1)
        gesamtzeit_sek = zeit_sek(arbeitsbeginn1, pausenende1)
        bloecke.append({"start": arbeitsbeginn1.strftime("%H:%M"), "ende": pausenbeginn1.strftime("%H:%M"), "typ": "arbeit", "sekunden": arbeitszeit_sek})
        bloecke.append({"start": pausenbeginn1.strftime("%H:%M"), "ende": pausenende1.strftime("%H:%M"), "typ": "pause", "sekunden": pausenzeit_sek})
        dateiname = f"{parsen_datum.strftime('%d.%m.%Y')}.json"


        if choice == "":
            log = {"datum": abfragen_datum, "bloecke": bloecke,
                   "summen": {"arbeitszeit in Sekunden": arbeitszeit_sek, "pausenzeit in Sekunden": pausenzeit_sek,
                              "gesamtzeit in Sekunden": gesamtzeit_sek}}
            with open(dateiname, "w", encoding="utf-8") as f:
                json.dump(log, f, ensure_ascii=False, indent=2)
            sys.exit()
        else:
            continue
    except ValueError:
        print(f"Tut mir Leid, aber mind. eine Deiner Eingaben scheint ungültig zu sein. Bitte versuche es erneut.")
        continue





