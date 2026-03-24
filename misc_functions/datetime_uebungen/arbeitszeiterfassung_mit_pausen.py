"""
Übung: Arbeitszeiterfassung mit Pausen
Datum: 17.08.2025
Ziel: Umgang mit datetime, timedelta und total_seconds üben
"""

# 1. Startzeit und eine Endzeit im Format HH:MM verarbeiten.
# 2. Beide Zeiten sollen mit dem heutigen Datum kombiniert werden
# 3. Differenz zwischen Start- und Endzeit berechnen.
# 4. Von dieser Differenz soll eine Pause in Minuten abgezogen werden.
# 5. Das Ergebnis soll auf zwei Arten ausgegeben werden:
# Ganze Stunden (als Zahl, abgerundet)
# Gesamte Minuten (exakt, nicht nur Stunden × 60)
# BONUS: Wenn die Endzeit vor der Startzeit liegt (z. B. Nachtschicht), soll dein Programm das automatisch berücksichtigen, indem die Endzeit um einen Tag erhöht wird.

import datetime
from datetime import timedelta

# Begrueßung
print("Willkommen beim Arbeitszeit-Berechenungs-Tool. Die Eingabe von Uhrzeiten bitte immer im Format hh:mm eingeben. ")
# 1:
abfragen_start = input("Hallo, wann hast Du heute angefangen zu arbeiten?\nUhrzeit:  ")
abfragen_ende = input("Vielen Dank, wann ist Dein regulärer Feierabend?\nUhrzeit:  ")

#2:
abfragen_start_dt = datetime.datetime.combine(datetime.date.today(), datetime.datetime.strptime(abfragen_start, "%H:%M").time())
abfragen_ende_dt = datetime.datetime.combine(datetime.date.today(), datetime.datetime.strptime(abfragen_ende, "%H:%M").time())

#3:
def rechner(start, ende):
    if ende < start:
        ende += datetime.timedelta(days=1)

    ergebnis = ende - start
    return ergebnis

#4:
differenz = rechner(abfragen_start_dt, abfragen_ende_dt)

abziehen_pause = differenz - timedelta(minutes=30)

arbeitszeit_stunden = abziehen_pause.total_seconds() // 3600
arbeitszeit_minuten =abziehen_pause.total_seconds() // 60
arbeitszeit_rest_minuten = (abziehen_pause.total_seconds() % 3600) // 60

arbeitszeit = f"{int(arbeitszeit_stunden)} Stunden und {int(arbeitszeit_rest_minuten)} Minuten"

#5:

print(f"Vielen Dank für Deine Eingaben. Abzüglich der regulären Pause von 30 Minuten beträgt Deine Arbeitszeit {arbeitszeit}. Die Gesamtminuten belaufen sich auf {arbeitszeit_minuten} Minuten. ")

