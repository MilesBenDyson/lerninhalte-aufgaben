import json
import os
import datetime
import sys

aufgaben = []
liste_name = "Aufgaben"
heute = datetime.date.today()
version = 1

def liste_laden(liste, name, ver):
    if os.path.exists(f"{name}_{heute}.json"):
        while True:
            print(f"Die Liste {name}_{heute}.json wurde gefunden. Soll sie überschrieben werden?(j/n)\n")
            antwort = input("j/n\n")
            if antwort == "j":
                print(f"{name}_{heute}.json wird mit neuen Einträgen überschrieben. ")
                with open(f"{name}_{heute}.json", "w", encoding='utf-8') as f:
                    json.dump(liste, f, ensure_ascii=False, indent=2)
                    break
            elif antwort == "n":
                print(f"Es wird eine neue Liste erstellt:\n{name}_{heute}_{ver}.json")
                with open(f"{name}_{heute}_{ver}.json", "w", encoding='utf-8') as f:
                    json.dump(liste, f, ensure_ascii=False, indent=2)
                    ver += 1
                    break
            else:
                print(f"Deine Eingabe {antwort} ist leider ungültig.")
    else:
        with open(f"{name}_{heute}.json", "w", encoding="utf-8") as f:
            json.dump(liste, f, ensure_ascii=False, indent=2)


while True:
    hauptmenue = input("----Hauptmenü----\n1. Aufgabe hinzufügen\n2. Aufgaben anzeigen\n3. Aufgabe abhaken\n4. Programm beenden")
    if hauptmenue == "1":
        print("Welche Aufgabe möchtest du hinzufügen?\n")
        titel = input("Titel\n")
        try:
            prio = int(input("Priorität (1-5)\n"))
            if not 1 <= prio <= 5:
                print("Bitte eine Zahl zwischen 1 und 5 eingeben, danke. ")
                continue
        except ValueError:
            print("Du musst eine Zahl von 1-5 eingeben. ")
            continue
        status = "offen"
        aufgaben.append({"Titel": titel, "Priorität": prio, "Status": status})
        print(f"Deine Aufgabe {titel} wurde hinzugefügt. Du gelangst nun ins Hauptmenü zurück...")
    elif hauptmenue == "2":
        if aufgaben == []:
            print("Deine Liste ist noch leer.\n ")
            continue
        else:
            for i, w in enumerate(aufgaben, start=1):
                print(f"{i}. {w['Titel']}  Priorität: {w['Priorität']} --- Status: {w['Status']}")
                print("\n\nDu gelangst nun wieder ins Hauptmenü zurück...\n")

    elif hauptmenue == "3":
        abhaken = input("Gib den Namen der Aufgabe ein, die du abhaken möchtest:\n")
        gefunden = False
        for i in aufgaben:
            if i["Titel"] == abhaken:
                i["Status"] = "erledigt"
                gefunden = True
                print(f"Deine Aufgabe {i['Titel']} wurde abgehakt. ")

        if not gefunden:
            print(f"{abhaken} konnte nicht in deiner Liste gefunden werden. ")
    elif hauptmenue == "4":
        print("Das Programm wird nun beendet...")
        if aufgaben != []:
            print("Deine Liste wird in einer JSON.Datei gespeichert.")
            liste_laden(aufgaben, liste_name, version)
        sys.exit()

    else:
        print(f"Deine Eingabe {hauptmenue} ist leider ungültig.\n")