# Spiel TicTacToe
import random

spiel_aktiv = True

spieler_aktuell = "X"

spielfeld = [" ",
             "1","2","3",
             "4","5","6",
             "7","8","9"]

# Spielfeld ausgeben
def spielfeld_ausgeben():

    print(spielfeld[1] + "  |  " + spielfeld[2] + "  |  " + spielfeld[3] )
    print("---|-----|---")
    print(spielfeld[4] + "  |  " + spielfeld[5] + "  |  " + spielfeld[6] )
    print("---|-----|---")
    print(spielfeld[7] + "  |  " + spielfeld[8] + "  |  " + spielfeld[9] )

# Spielereingabe und Überprüfung
def spieler_eingabe():
    global spiel_aktiv
    while True:
        spielzug = input("Bitte Feld eingeben. ")
        #vorzeitiges Spielende durch Spieler
        if spielzug == "q":
            spiel_aktiv = False
            return
        try:
            spielzug = int(spielzug)
        except ValueError:
            print("Ungültige Eingabe! Bitte ZAHL von 1 - 9 eingeben" )
        else:
            if spielzug >= 1 and spielzug <= 9:
                # Spielereingabe und Kontrolle der Eingabe
                if spielfeld[spielzug] == "X" or spielfeld[spielzug] == "O":
                    print("Das Feld ist bereits belegt. Bitte wähle ein anderes Feld. ")
                    spielfeld_ausgeben()
                else:
                    return spielzug
            else:
                print("Ungültige Eingabe! Bitte Zahl zwischen 1 - 9 eingeben" )

#zweiter Spieler und Wechsel
def spieler_wechseln():
    global spieler_aktuell
    if spieler_aktuell == "X":
        spieler_aktuell = "O"
    else:
        spieler_aktuell = "X"


# Kontrolle wann wer gewinnt
def kontrolle_gewonnen():
    # wenn alle drei Felder gleich sind hat entspr. Spieler gewonnen

    #1. Kontrolle alle REIHEN
    if spielfeld[1] == spielfeld[2] == spielfeld[3]:
        return spielfeld[1]
    if spielfeld[4] == spielfeld[5] == spielfeld[6]:
        return spielfeld[4]
    if spielfeld[7] == spielfeld[8] == spielfeld[9]:
        return spielfeld[7]

    # 2. Kontrolle alle SPALTEN
    if spielfeld[1] == spielfeld[4] == spielfeld[7]:
        return spielfeld[1]
    if spielfeld[2] == spielfeld[5] == spielfeld[8]:
        return spielfeld[2]
    if spielfeld[3] == spielfeld[6] == spielfeld[9]:
        return spielfeld[3]

    #3. Kontrolle alle DIAGONALEN
    if spielfeld[1] == spielfeld[5] == spielfeld[9]:
        return spielfeld[1]
    if spielfeld[3] == spielfeld[5] == spielfeld[7]:
        return spielfeld[3]


# Funtkion Kontrolle unentschieden
def kontrolle_auf_unentschieden():
    if (spielfeld[1] == "X" or spielfeld[1] == "O") \
        and (spielfeld[2] == "X" or spielfeld[2] == "O") \
        and (spielfeld[3] == "X" or spielfeld[3] == "O") \
        and (spielfeld[4] == "X" or spielfeld[4] == "O") \
        and (spielfeld[5] == "X" or spielfeld[5] == "O") \
        and (spielfeld[6] == "X" or spielfeld[6] == "O") \
        and (spielfeld[7] == "X" or spielfeld[7] == "O") \
        and (spielfeld[8] == "X" or spielfeld[8] == "O") \
        and (spielfeld[9] == "X" or spielfeld[9] == "O"):
        return ("unentschieden")





spielfeld_ausgeben()
while spiel_aktiv:
    # Eingabe des aktiven Spielers
    print()
    print("Spieler", spieler_aktuell, "ist am Zug. ")

    # aus der Liste spielfeld alle X und O und leere Felder entfernen
    spielfeld_KI = []
    for moegliche_felder in spielfeld[1:]:
        if moegliche_felder != "X" and moegliche_felder != "O":
            spielfeld_KI.append(moegliche_felder)
        # print (spielfeld_KI)
        # print()
        # print (random.choice(spielfeld_KI))

        # wenn Computergegner am Zug ist, ein freies zufälliges Feld belegen
    if spieler_aktuell == "O":
        spielzug = int(random.choice(spielfeld_KI))
    else:
        spielzug = spieler_eingabe()

    if spielzug:
        spielfeld[spielzug] = spieler_aktuell
        # aktuelles Spielfeld ausgeben
        spielfeld_ausgeben()
        # Kontrolle ob jemand gewonnen hat
        gewonnen = kontrolle_gewonnen()

        print("Spieler ",spieler_aktuell, "hat", spielzug, "eingegeben.")

        if gewonnen:
            print("Spieler", gewonnen, "hat gewonnen.")
            spiel_aktiv = False
            break
        # Kontrolle ob unentschieden
        unentschieden = kontrolle_auf_unentschieden()

        if unentschieden:
            print("Das Spiel ist unentschieden.")
        # Spieler wechseln
        spieler_wechseln()






