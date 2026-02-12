import json
import sys
import os

dateiname = 'musikarchiv.json'

if os.path.exists(dateiname):
    try:
        with open(dateiname, 'r', encoding='utf-8') as f:
            p_daten = json.load(f)
    except ValueError:
        print("Die Datei kann nicht korrekt gelesen werden. Es wird eine neue erstellt.")
        p_daten = []

else:
    p_daten = []

class Musikarchiv:
    pass

def m_eingabe(t, g, i, a):
    m = Musikarchiv()
    m.titel = t
    m.genre = g
    m.interpret = i
    m.album = a
    return m


interpret = None
genre = None
album = None
titel = None

def eintrag_json(m):
    return {
        "titel": m.titel,
        "genre": m.genre,
        "interpret": m.interpret,
        "album": m.album
    }

while True:
    if any([interpret, genre, album, titel]):
        abfrage_2 = input("Möchtest du mehr eingeben?(j/n)\n")
        if abfrage_2 == 'j':
            interpret = None
            genre = None
            album = None
            titel = None
            continue
        elif abfrage_2 == 'n':
            print("Okay, deine Eingabe wird gespeichert. Bis zum nächsten Mal.")
            break

    else:
        print("Hallo, willkommen zum MusikArchivator. Denk dran, mit 'q' kannst du das Programm beenden.")
        abfrage = input("Nach welchem Kriterium möchtest du eingeben? Interpret, Titel, Genre, Album?\n")
        if abfrage.lower() == 'interpret':
            abfrage_interpret = input("Wie heißt der Interpret?")
            interpret = f"{abfrage_interpret[0].upper()}{abfrage_interpret[1:].lower()}"

        elif abfrage.lower() == 'album':
            album_abfrage = input("Wie heißt das Album?")
            album = f"{album_abfrage[0].upper()}{album_abfrage[1:].lower()}"

        elif abfrage.lower() == 'titel':
            titel_abfrage = input("Wie ist der Titel des Songs?")
            titel = f"{titel_abfrage[0]}{titel_abfrage[1:].lower()}"

        elif abfrage.lower() == 'genre':
            genre_abfrage = input("Wie heißt das Genre?")
            genre = f"{genre_abfrage[0].upper()}{genre_abfrage[1:].lower()}"

        elif abfrage.lower() == 'q':
            print("Programm wird beendet... ... ...")
            sys.exit()
        while True:
            if titel:
                print(f"Okay, {titel} heißt der Song.")
                interpret = input("Von welchem Interpreten stammt der Song?\n")
                album = input("Von welchem Album?\n")
                genre = input("Welchem Genre ist die Musik zuzuordnen?\n")
                p_daten.append(eintrag_json(m_eingabe(titel, genre, interpret, album)))
                break
            elif album:
                print(f"Okay, {album} heißt das Album.")
                titel = input("Wie ist der Titel des Songs?\n")
                interpret = input("Von welchem Interpreten stammt der Song?\n")
                genre = input("Welchem Genre ist die Musik zuzuordnen?\n")
                p_daten.append(eintrag_json(m_eingabe(titel, genre, interpret, album)))
                break
            elif interpret:
                print(f"Okay, {interpret} heißt der Interpret.")
                titel = input("Wie ist der Titel des Songs?\n")
                genre = input("Welchem Genre ist die Musik zuzuordnen?\n")
                album = input("Von welchem Album?\n")
                p_daten.append(eintrag_json(m_eingabe(titel, genre, interpret, album)))
                break
            elif genre:
                print(f"Okay, {genre} ist das Genre.")
                titel = input("Wie ist der Titel des Songs?\n")
                interpret = input("Von welchem Interpreten stammt der Song?\n")
                album = input("Von welchem Album?\n")
                p_daten.append(eintrag_json(m_eingabe(titel, genre, interpret, album)))
                break
            else:
                print("Die Daten sind beschädigt.")
                break

with open(dateiname, 'w', encoding='utf-8') as f:
    json.dump(p_daten, f, ensure_ascii=False, indent=2)