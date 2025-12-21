'''Du baust ein kleines Menü, das immer wieder erscheint –
und darin benutzt du Flag-Logik, um zu prüfen, ob ein gesuchter Eintrag existiert.'''

personen = [
    {"name": "Alex", "level": 5},
    {"name": "Ben", "level": 12},
    {"name": "Lina", "level": 3},
    {"name": "Ben", "level": 23}
]

while True:
    print("1. Liste anzeigen\n2. Nach Namen suchen\n3. Beenden")
    auswahl_1 = input("Wähle: 1 - 2 - 3\n")
    if int(auswahl_1) == 1:
        for n in personen:
            print(f"Name: {n['name']} --> Level: {n['level']}\n")
    elif int(auswahl_1) == 2:
        gefunden = False
        ergebnis = []
        suche = input("Du möchtest einen Namen suchen.\nGib den Namen ein, den du suchen möchtest:\n")
        for n in personen:
            if n['name'].lower() == suche.lower():
                gefunden = True
                ergebnis.append(f"Name: {n['name']}, Level: {n['level']}")
        if gefunden:
            print(f"Es wurde folgende Personen mit dem Namen '{suche}' gefunden:\n{'\n'.join(ergebnis)}")


    elif int(auswahl_1) == 3:
        print("Programm wird beendet...")
        break
    else:
        print("Auswahl ungültig.")