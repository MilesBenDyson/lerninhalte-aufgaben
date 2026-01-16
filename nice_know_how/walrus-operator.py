#grundsätzliches Beispiel:
if (laenge := len("Hallo")) > 3:
    print(laenge)

#Aufgabe1:
text = "Cybersecurity"
'''Schreibe eine if-Bedingung mit dem Walrus-Operator, die
die Länge von text in einer Variablen l speichert
prüft, ob diese Länge größer als 5 ist
und in diesem Fall l ausgibt
Baue alles in eine if-Zeile mit := ein.'''

if (l := len(text)) > 5:
    print(l)
else:
    print(f"{text} hat nur {l} Zeichen")

#Aufgabe2:
'''Gegeben ist diese Liste:'''
daten = ["ok", "ok", "fehler", "ok"]
'''Schreibe eine if-Bedingung mit dem Walrus-Operator, die:
die Anzahl von "fehler" in daten in einer Variablen f speichert
prüft, ob f größer als 0 ist
und dann ausgibt:
Es gibt f Fehler'''

if (f := daten.count('fehler')) > 0:
    print(f"Es gibt {f} Fehler.")
