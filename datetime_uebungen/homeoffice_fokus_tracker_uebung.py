"""Anforderungen

Beim Start:
Frage Datum (Enter = heute), dann 1–3 Arbeitsblöcke (Start/Ende im Format HH:MM). Leere Eingabe beendet die Block-Abfrage.
Wenn eine Endzeit vor der Startzeit liegt → Block endet am nächsten Tag.
Rechne je Block die Dauer in Minuten aus und gib sie formatiert aus.
Rechne die Gesamtarbeitszeit (Summe der Blöcke).
Rechne die Pausen zwischen den Blöcken (Differenz: Start_n – Ende_{n-1}).
Speichere als homeoffice_log.json:
{
  "datum": "YYYY-MM-DD",
  "wochentag": "Samstag",
  "bloecke": [
    {"start": "08:30", "ende": "12:00", "minuten": 210},
    {"start": "13:00", "ende": "16:15", "minuten": 195}
  ],
  "pausen_minuten": [60],
  "gesamt_minuten": 405,
  "notiz": "Home Office"
}
Lade die Datei direkt wieder und drucke eine Kurz-Zusammenfassung aus der geladenen Struktur (nicht aus deinen Variablen)."""

import datetime
import sys
import locale
import json



locale.setlocale(locale.LC_ALL, "de_DE.utf-8")

# Begrüßung
print("Sei willkommen bei Deinem Personal Planer.\nMir mir kannst Du Deine Produktiv-Tage planen. Dadurch hast Du eine Übersicht, \nzu welcher Zeit Du Deine Übungen und Lehrinhalte umsetzen kannst und wann Du am\nbesten eine Pause machst. Auch die Dauer der Pause wird erfasst.\n")
# Frage Datum, Enter=heute
while True:
    abfragen_datum = input("Gib das Datum an, an dem Du Deinen Produktivtag planen möchtest. Bei -Enter- nehme ich das heutige Datum.\nDatum:  ")

    if abfragen_datum == "":
        parsen_abfragen_datum = datetime.date.today()
        break

    else:
        try:
            parsen_abfragen_datum = datetime.datetime.strptime(abfragen_datum, "%d.%m.%Y").date()
            break
        except ValueError:
            print(f"Es tut mir Leid, aber Deine Eingabe {abfragen_datum} ist ungültig. Probiere es erneut, oder möchtest Du das Programm beenden?\n ")
            choice1 = input("Beenden? j/n:   ")
            if choice1 == "j":
                print("Alles okay, das Programm wird nun beendet. Bis zum nächsten Mal :) ")
                sys.exit()
            else:
                continue
# datum kürzer benennen
datum = parsen_abfragen_datum

# Funktion für parsen in datetimeobjekte
def datetimemaker(d, h, m):
    return datetime.datetime.combine(d, datetime.time(h, m))
def differenz(start, ende):
    if start > ende:
        ende += datetime.timedelta(days=1)
    return ende - start

def uhrzeitstringer(zeit):
    return zeit.strftime("%H:%M")




# Zeitblöcke definieren
# 1. Block 08:00 - 09:30 Uhr Pause 30 Minuten
start1 = datetimemaker(datum,8, 0)
ende1 = datetimemaker(datum,9, 30)
dauer1 = differenz(start1, ende1)

# 2. Block 10:00 - 12:00 Uhr Pause 45 Minuten
start2 = datetimemaker(datum,10, 0)
ende2 = datetimemaker(datum,12,0)
dauer2 = differenz(start2, ende2)

# 3. Block 12:45 - 15:00 Uhr
start3 = datetimemaker(datum,22,45)
ende3 = datetimemaker(datum,6,0)
dauer3 = differenz(start3, ende3)


# Zusammenfassung


wochentag = datum.strftime("%A")
# Block 1
uhrzeit_start1 = uhrzeitstringer(start1)
uhrzeit_ende1 = uhrzeitstringer(ende1)
gesamt1 = int(dauer1.total_seconds() // 60)

pause1 = differenz(ende1, start2)
pause1_minuten = int(pause1.total_seconds() // 60)

# Block 2
uhrzeit_start2 = uhrzeitstringer(start2)
uhrzeit_ende2 = uhrzeitstringer(ende2)
gesamt2 = int(dauer2.total_seconds() // 60)

pause2 = differenz(ende2, start3)
pause2_minuten = int(pause2.total_seconds() // 60)

# Block 3
uhrzeit_start3 = uhrzeitstringer(start3)
uhrzeit_ende3 = uhrzeitstringer(ende3)
gesamt3 = int(dauer3.total_seconds() // 60)

pause_minuten_gesamt = pause1_minuten + pause2_minuten
produktivzeit_gesamt = gesamt1 + gesamt2 + gesamt3

log = {"datum": datum.strftime("%d.%m.%Y"), "wochentag": wochentag, "bloecke": [{"start": uhrzeit_start1, "ende": uhrzeit_ende1, "minuten": gesamt1}, {"start": uhrzeit_start2, "ende": uhrzeit_ende2, "minuten": gesamt2}, {"start": uhrzeit_start3, "ende": uhrzeit_ende3, "minuten": gesamt3}], "pausen_minuten": pause_minuten_gesamt, "gesamt_minuten": produktivzeit_gesamt, "notiz": "homeoffice"}

with open("homeoffice_log.json", "w", encoding="utf-8") as f:
    json.dump(log, f, ensure_ascii=False, indent=2)

with open("homeoffice_log.json", "r", encoding="utf-8") as f:
    logfile = json.load(f)

print(logfile)