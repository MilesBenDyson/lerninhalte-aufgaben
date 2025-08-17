import sys # wenn das Programm beendet wird
# Punkte zählen
punkte = 0
# alle richtigen Antworten
# antwort1 = "Ratt"
# antwort2 = "Mötley Crüe"
# antwort3 = "i wanna rock"
# antwort4 = "Cinderella"
# antwort5 = "WASP"

# Begrüßung: Willkommen beim Hairmetal-Quiz. Beantworte die 5 Fragen und wir werden sehen, wie lang und füllig Deine Mähne ist!
print("Willkommen beim Hairmetal-Quiz. Beantworte die 5 Fragen und wir \nwerden sehen, wie lang und füllig Deine Mähne ist! ")
regeln = input("Hast Du Bock? Dann machen wir mit den Regeln weiter ... j/n ")
if regeln == "j":

# Regeln: Tippe die Lösung nach den Fragen ein. Wenn Du die Antwort nicht weißt, gib "weiter" ein. Wenn Du das Quiz beenden willst, gib "Ich liebe Schlager" ein.
    print("Tippe die Lösung nach den Fragen ein. \nWenn Du die Antwort nicht weißt, gib 'weiter' ein. \nWenn Du das Quiz beenden willst, gib 'Ich liebe Schlager' ein.")
elif regeln == "n":
    print("Dann hör Dir lieber den Musikantenstadl an, das hier ist nur was für echte \ngeschminkte Männer mit langen Haaren! ")
    sys.exit()

# starte Quiz oder beenden
start = input("Kann es losgehen? j/n ")
if start == "j":
    print("Super, dann kommen wir zur ersten Frage:")

    # Frage 1
    print("Welche Hair Metal Band schrieb den Song 'Round and round' ? ")
    antwort1 = input("Deine Antwort: ")# generell: Groß- und Kleinschreibung gleichsetzen

    if antwort1.lower() == "ratt":
        punkte += 1

    elif antwort1.lower() == "weiter":
        punkte += 0

    elif antwort1.lower() == "ich liebe schlager" :
        print("Deine Eingabe macht mich nicht glücklich. Quiz beendet")
        sys.exit()
    else:
        print("Deine Eingabe macht mich nicht glücklich. Quiz beendet")
        punkte += 0


    # Frage 2
    print("Welche Band trank gerne Löwenbräu und hat daher Umlautpunkte \nin den Bandnamen übernommen? ")
    antwort2 = input("Deine Antwort: ")

    if antwort2.lower() == "mötley crüe":
        punkte += 1

    elif antwort2.lower() == "weiter":
        punkte += 0

    elif antwort2.lower() == "ich liebe schlager" :
        print("Deine Eingabe macht mich nicht glücklich. Quiz beendet")
        sys.exit()
    else:
        print("Deine Eingabe macht mich nicht glücklich.")
        punkte += 0

    # Frage 3
    print("In einem Musikvideo wütet ein cholerischer Lehrer in der Klasse \nund schreit nen coolen Dude an. Wie heißt der Song des Musikvideos? ")
    antwort3 = input("Deine Antwort: ")

    if antwort3.lower() == "i wanna rock":
        punkte += 1
    elif antwort3.lower() == "weiter":
        punkte += 0
    elif antwort3.lower() == "ich liebe schlager":
        print("Deine Eingabe macht mich nicht glücklich. Quiz beendet")
        sys.exit()
    else:
        print("Deine Eingabe macht mich nicht glücklich.")
        punkte += 0

    # Frage 4
    print("Welche Band trägt den gleichen Namen, wie eine Disney-Prinzessin? ")
    antwort4 = input("Deine Antwort: ")
    if antwort4.lower() == "cinderella":
        punkte += 1

    elif antwort4.lower() == "weiter":
        punkte += 0

    elif antwort4.lower() == "ich liebe schlager":
        print("Deine Eingabe macht mich nicht glücklich. Quiz beendet")
        sys.exit()
    else:
        print("Deine Eingabe macht mich nicht glücklich.")
        punkte += 0

    # Frage 5
    print("Wie heißt die Band, dessen Sänger gerne Sägeblätter als Armschmuck trägt? ")
    antwort5 = input("Deine Antwort: ")
    if antwort5.lower() == "wasp":
        punkte += 1

    elif antwort5.lower() == "weiter":
        punkte += 0

    elif antwort5.lower() == "ich liebe schlager" :
        print("Deine Eingabe macht mich nicht glücklich. Quiz beendet")
        sys.exit()
    else:
        print("Deine Eingabe macht mich nicht glücklich.")
        punkte += 0
elif start == "n":
    print("Dann hör Dir lieber den Musikantenstadl an, das hier ist nur was für echte \ngeschminkte Männer mit langen Haaren! ")
    sys.exit()

# Ergebnis - Punkteauswertung
print("Nun kommen wir zur Asuwertung")
print(f"Du hast {punkte} Punkte erreicht")
# Beurteilung
# 0 - 1 Punkte: Schlecht! Deine Frisur gleicht einem Kasernenschnitt.
if punkte <= 1:
    print("Schlecht! Deine Frisur gleicht einem Kasernenschnitt ")
    sys.exit()
# 2 - 3 Punkte: Du scheinst noch nicht verloren! Alle haben mal mit dem Übergang auf lange Haare zu kämpfen gehabt.
elif punkte > 1 and punkte < 4:
    print("Du scheinst noch nicht verloren! Alle haben mal mit dem Übergang auf lange Haare zu kämpfen gehabt. ")
    sys.exit()
# 4 - 5 Punkte: Yeah, das ist mal ne ordentliche Matte! Das Haarspray Deiner Mähne trägt ein eigenes Ozonloch über sich!
else:
    print("Yeah, das ist mal ne ordentliche Matte! Das Haarspray Deiner Mähne trägt ein eigenes Ozonloch über sich!")
    sys.exit()