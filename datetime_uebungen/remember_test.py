import datetime



def uhrzeit():
    time = datetime.datetime.now()
    return time

while True:
    zielzeit = input("Wie lange musst du heute arbeiten? Bitte gib die Uhrzeit in hh:mm ein:\n")
    try:
        zielzeit_parsed_1 = datetime.datetime.strptime(zielzeit, "%H:%M").time()
        zielzeit_parsed_2 = datetime.datetime.combine(datetime.date.today(), zielzeit_parsed_1)
        break
    except ValueError:
        print("Das ist kein gültiges Uhrzeitformat, bitte versuche es erneut...")
        continue

zeit_differenz = zielzeit_parsed_2 - uhrzeit()

totale_sekunden = zeit_differenz.total_seconds()
stunden = totale_sekunden // (60 * 60)
rest_minuten = (totale_sekunden % (60 * 60)) // 60

print(f"Du hast in {int(stunden)} Stunden und {int(rest_minuten)} Minuten Feierabend.")
