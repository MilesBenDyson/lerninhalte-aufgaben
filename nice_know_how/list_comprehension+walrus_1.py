zahlen = [3, 7, 12, 5, 18, 1, 9]

zahlen_groß = [z for z in zahlen if z > 8]

print(zahlen_groß)

text = "cybersecurity"

if (l := len(text)) > 10:
    print(f"{text} hat {l} Zeichen.")

#nächste Aufgabe:
'''Wie würdest du eine List Comprehension mit Walrus-Operator bauen, die aus einer Liste von Wörtern nur diejenigen übernimmt, deren Länge größer als 5 ist, ohne len() zweimal aufzurufen?
Beispiel-Daten:'''
wörter = ["Haus", "Cyber", "Firewall", "Code", "Python", "Netz"]
'''Ziel: wörter_2 = ["Firewall", "Python"]'''

wörter_2 = [w for w in wörter if (l := len(w)) > 5]

print(wörter_2)
