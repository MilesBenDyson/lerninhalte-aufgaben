import json
import sys
from pokemonkarten import p_liste
import random

# die spielerklasse
class Spieler:
    spielernummer = 0
    def __init__(self, name):
        self.spielernummer = Spieler.spielernummer
        self.name = name
        self.karten = []
        Spieler.spielernummer += 1
    def anzahl_karten(self):
        return len(self.karten)

def auswahl_spielverlauf(frage):
    if frage == "j":
        print("Programm wird beendet...")
        sys.exit()
    elif frage == "n":
        return
    else:
        print("Scheinbar wurdest du von der Attacke 'Verwirrung' getroffen.\nDas Programm wird vorsichtshalber beendet, bevor du dich selbst verletzt.")
        sys.exit()
# start und begruessung
while True:
    anzahl_spieler = input("Willkommen beim Pokémon Quartett! Wieviele Spieler nehmen teil?\nEs können maximal 6 Spieler teilnehmen.\n")
    try:
        anzahl_spieler = int(anzahl_spieler)
        if anzahl_spieler <= 1 or anzahl_spieler > 6:
            print("Die Anzahl der Spieler ist leider nicht gültig.")
            beenden = input("Möchtest du das Spiel beenden?\nBeenden? (j/n)\n")
            auswahl_spielverlauf(beenden)
            continue
        break
    except (ValueError, TypeError):
        beenden = input("Vermutlich hast du dich vor Aufregung vertippt. Probiere es nochmal oder möchtest du das Spiel beenden?\nBeenden? (j/n)\n")
        auswahl_spielverlauf(beenden)

# namen zuweisung und Liste der Spieler
spieler_objekte = []
for i in range(anzahl_spieler):
    spieler = input(f"Gib bitte den Namen des Spielers {i+1} ein.")
    spieler_objekte.append(Spieler(spieler))

# kartenverteiler mit trick indexing u. modulo
def kartenverteilen(spielerobjekte, karten):
    random.shuffle(karten)
    i = 0
    while karten:
        spieler = spielerobjekte[i % len(spielerobjekte)]
        spieler.karten.append(karten.pop())
        i += 1

kartenverteilen(spieler_objekte, p_liste)
for s in spieler_objekte:
    print(f"Spieler {s.name} hat {len(s.karten)} Karten")



def falsche_eingabe():
    error = input("Bitte nutze die angegeben Zahlen oder möchtest du das Spiel beenden? (j/n)\n")
    if error == "j":
        print("Programm wird beenden, vielen Dank fürs Spielen... ... ...")
        sys.exit()
    elif error == 'n':
        return
    else:
        print("Die Eingabe ist wieder ungültig. Das Programm fährt vorsichtshalber runter\n... ... ...")
        sys.exit()

# duellsystem

zwischenstapel = []
# !!! stichstapel, was passiert wann damit? !!!

print("Danke! Nun beginnt eine Partie Pokemón Quartett!\n")

# Hauptmenu als Funktion
def hauptmenu(spieler):
    spieler_aktuell = spieler.name
    alle_karten = spieler.karten
    rest_karten = len(alle_karten)
    karte_aktuell = spieler.karten[0]
    print(f"\n{spieler_aktuell} ist am Zug...\n")
    while True:
        try:
            menu = int(input("1. Nächste Karte sehen\n2. Alle Karten sehen\n3. Anzahl verbleibender Karten anzeigen\n4. Spiel beenden\nGib bitte die entsprechende Nummer ein\n"))

            # Beenden
            if menu == 4:
                print("Okay, das Programm wird nun beendet. Bis zum nächsten Mal.\n")
                sys.exit()

            # Menu 1 Nächste Karte sehen
            elif menu == 1:
                print(karte_aktuell)
                while True:
                    try:
                        zug = int(input("1. Wert wählen\n2. zurück\n3. aufgeben\nwähle mit der entsprechenden Nummer (1 - 3)\n"))

                        # Auswahl Wert wählen
                        if zug == 1:
                            while True:
                                try:
                                    wert_auswahl = int(input("Welchen Wert möchtest du nehmen?\n1 = Level\n2 = KP\n3 = Angriff\n4 = Verteidigung\n5 = Spez. Angriff\n6 = Spez. Verteidigung\nWähle 1 - 6:\n"))
                                    # Auswahl Level
                                    wert_map = {
                                        1: "level",
                                        2: "kraftpunkte",
                                        3: "angriff",
                                        4: "verteidigung",
                                        5: "spezialangriff",
                                        6: "spezialverteidigung"
                                    }
                                    try:
                                        kategorie = wert_map[wert_auswahl]
                                        wert_aktuell = getattr(karte_aktuell, kategorie)
                                        return (spieler_aktuell, karte_aktuell, kategorie, wert_aktuell)
                                    except (ValueError, TypeError):
                                        falsche_eingabe()
                                except (ValueError, TypeError):
                                    falsche_eingabe()
                        # Auswahl zurück
                        elif zug == 2:
                            break
                        # Auswahl Aufgeben
                        elif zug == 3:
                            print("Okay, du möchtest aufgeben. Das nächste mal hast du mehr Glück!")
                            spieler_objekte.remove(spieler) # genaue Bezeichnung des Spielers wird noch entschieden
                            print(f"{spieler.name} ist ausgeschieden.")

                    except (ValueError, TypeError):
                        falsche_eingabe()
                    break
            # Menu 2 Alle Karten sehen
            elif menu == 2:
                for p in alle_karten:
                    print(p.__str__())

            # Menu 3 Anzahl verbleibender Karten
            elif menu == 3:
                print(f"Du hast noch {rest_karten} übrig.\n")
            # Falscheingabe
            else:
                falsche_eingabe()

        except (ValueError, TypeError):
            falsche_eingabe()

# kampfsystem

# ausgewählte werte werden zwischengespeichert und verglichen
def kampf(zwischenspeicher, scoredefault, zwischenstapel):
    max_wert = None
    for k in zwischenspeicher:
        wert = k['wert']
        name = k['name']
        kategorie = k['kategorie']
        karten = k['karten']
        karte = karten.pop(0)
        print(f"{name}: Sein {karte.name} hat bei {kategorie.capitalize()} einen Wert von {wert}")
        input()

        zwischenstapel.append(karte)

        if max_wert is None:
            max_wert = wert
            scoredefault.append(k)

        elif wert > max_wert:
            scoredefault.clear()
            scoredefault.append(k)
            max_wert = wert


        elif wert == max_wert:
            print(f"Es gibt ein Stich!")
            scoredefault.append(k)





# vielleicht später ein json-Log, wie die Runden verlaufen sind

# Spiel beginnt

# spielerreihenfolge mischen
random.shuffle(spieler_objekte)

# wert vs. wert -> temporärer Rundenspeicher(Zwischenspeicher)
# --> arena heißt der Zwischenspeicher
arena = [{'spieler': s, 'name': s.name, 'karten': s.karten, 'karte': None, 'kategorie': None, 'wert': None} for s in spieler_objekte]

while True:
    index_spieler_raus = []
    for i, e in enumerate(arena):
        if not e['karten']:
            index_spieler_raus.append(i)
    for i in reversed(index_spieler_raus):
        arena.pop(i)
    if len(arena) == 1:
        print(f"{arena[0]['name']} hat gewonnen!")
        break
    score = []
    # ''' !!! erstmal fängt immer der erste spieler an. ein wechsel nach rundensieg muss noch erstellt werden !!!'''
    spieler_name, karte, kategorie, wert = hauptmenu(arena[0]['spieler'])

    # anzeigen was der spieler gewählt hat
    print(f"Spieler {spieler_name} nimmt {kategorie[0].upper() + kategorie[1:].lower()}.\n")

    input()

    # die Kategorie überall setzen
    for i in arena:
        karte = i['spieler'].karten[0]
        wert = getattr(karte, kategorie)
        i['karte'] = karte
        i['wert'] = wert
        i['kategorie'] = kategorie

    kampf(arena, score, zwischenstapel)

    while len(score) > 1:
            for s in score:
                karte = s['spieler'].karten[0]
                wert = getattr(karte, kategorie)
                s['karte'] = karte
                s['wert'] = wert
                s['kategorie'] = kategorie
            score_stich = []
            kampf(score, score_stich, zwischenstapel)

            score = score_stich
    if len(score) == 1:
        runden_gewinner = score[0]['name']
        print(f"Diese Runde hat {runden_gewinner} gewonnen.")
        for i in arena:
            name_arena = i['name']
            if name_arena == runden_gewinner:
                for k in zwischenstapel:
                    i['karten'].append(k)
                    print(f"{score[0]['name']} bekommt die Karte {k.name}")
        for i, e in enumerate(arena):
            if e['name'] == runden_gewinner:
                neue_spitze = arena.pop(i)
                arena.insert(0, neue_spitze)
                break
        zwischenstapel.clear()








'''🚀 Kleiner Ausblick (nächster sinnvoller Schritt)

evtl. Log-Ausgabe der Runde (wer hat was gespielt)'''