""" Schreibe ein kleines Python-Programm namens „Pausenplaner“.
Das Programm soll:
Den Arbeitsbeginn und das geplante Arbeitsende abfragen.
Automatisch die gesamte Arbeitszeit berechnen.
Dir zwei Pausen vorschlagen:
Erste Pause nach 1/3 der Arbeitszeit
Zweite Pause nach 2/3 der Arbeitszeit
Die Uhrzeiten der beiden Pausen ausgeben.
👉 Bonus: Wenn du Lust hast, lass das Programm auch prüfen, ob die Pausen mindestens 1 Stunde auseinander liegen. Falls nicht, soll es eine Meldung ausgeben („Die Pausen liegen zu nah beieinander“)."""

import datetime


# Arbeitsbeginn und Arbeitsende abfragen
while True:

    abfragen_beginn = input("Willkommen beim Pausenplaner. Um Dir perfekte Pausen vorschlagen zu können, benötige ich erstmal den Beginn Deiner Arbeitszeit heute. Nutze als Zeitangabe immer das Format hh:mm.\nUhrzeit Beginn:    ")
    try:
      parsen_beginn = datetime.datetime.strptime(abfragen_beginn, "%H:%M").time()
      abfragen_ende = input(f"Vielen Dank, also um {parsen_beginn.strftime('%H:%M')} Uhr fängt Deine Arbeitszeit an. Wann ist Dein regulärer Feierabend?\nUhrzeit Feierabend:    ")
      parsen_ende = datetime.datetime.strptime(abfragen_ende, "%H:%M").time()
      print(f"Vielen Dank, also um {parsen_ende.strftime('%H:%M')} Uhr hast Du den regulären Feierabend erreicht. ")
      break
    except ValueError:
     print("Es tut mir Leid, aber Deine Eingabe ist ungültig. Versuche es erneut. ")
     continue

beginn_dt = datetime.datetime.combine(datetime.date.today(), parsen_beginn)
ende_dt = datetime.datetime.combine(datetime.date.today(), parsen_ende)

# berechnen der gesamten Arbeitszeit
if beginn_dt > ende_dt:
    ende_dt += datetime.timedelta(days=1)

arbeitszeit_ohne_pause = ende_dt - beginn_dt

def rechnen_minuten_gesamt(differenz):
    return differenz.total_seconds() // 60

def rechnen_stunden(differenz):
    return differenz.total_seconds() // 3600

def rechnen_minuten_rest(differenz):
    return (differenz.total_seconds() % 3600) // 60

minuten_gesamt = rechnen_minuten_gesamt(arbeitszeit_ohne_pause)
stunden = rechnen_stunden(arbeitszeit_ohne_pause)
rest_minuten = rechnen_minuten_rest(arbeitszeit_ohne_pause)

# 2 Pausen vorschlagen: 1. Pause nach 1/3 der Arbeitszeit; 2. Pause nach 2/3 der Arbeitszeit

# Uhrzeit nach einem Drittel der gesamten Arbeitszeit
ein_drittel = beginn_dt + datetime.timedelta(minutes=(minuten_gesamt // 3))
ein_drittel_str = ein_drittel.strftime("%H:%M")
# Uhrzeit nach zwei Drittel der gesamten Arbeitszeit
zwei_drittel = beginn_dt + datetime.timedelta(minutes=(minuten_gesamt * (2 / 3)))
zwei_drittel_str = zwei_drittel.strftime("%H:%M")
haelfte_str = (beginn_dt + datetime.timedelta(minutes=minuten_gesamt // 2)).strftime("%H:%M")

# Bonus: prüfen ob Pausen mindestens eine Stunde auseinander liegen
if (zwei_drittel - ein_drittel) <= datetime.timedelta(hours=1):
    print(f"Eigentlich würde ich Dir vorschlagen, um {ein_drittel_str} Uhr die erste Pause und um {zwei_drittel_str} Uhr die zweite Pause. Aber die liegen zu nah bei einander. Vielleicht reicht eine Pause um {haelfte_str} Uhr heute. Du scheinst einen kürzeren Arbeitstag zu haben. ")

else:
    print(f"Du hast heute langen Arbeitstag. Am besten machst Du um {ein_drittel_str} Uhr die erste Pause und um {zwei_drittel_str} Uhr die zweite Pause. ")




