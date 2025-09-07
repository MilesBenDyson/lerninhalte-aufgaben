"""🧩 Snack – kleiner Kartenstapel

Erstelle eine leere Liste stapel = [].

Lege mit .append() drei „Karten“ drauf, z. B. "Herz Ass", "Karo 10", "Pik Dame".

Gib den Stapel aus.

Ziehe mit .pop() die oberste Karte und speichere sie in einer Variablen karte.

Drucke:

die gezogene Karte

den aktuellen Stapel"""

stapel = []

def stapeln(liste, karte):
    return liste.append(karte)

stapeln(stapel, "Herz Ass")
stapeln(stapel, "Karo 10")
stapeln(stapel, "Pik Dame")
print(stapel)

ziehen = stapel.pop(-1)

print(stapel)
print(ziehen)

""" 🧩 Snack – Stapel komplett ziehen

Du hast deinen Stapel mit Karten.

Solange noch Karten drin sind (while stapel:), soll eine Karte mit .pop() gezogen werden.

Jede gezogene Karte wird ausgegeben.

Am Ende ist der Stapel leer."""

stapeln(stapel, "Bube Kreuz")
stapeln(stapel, "10 Karo")
stapeln(stapel, "8 Kreuz")

while stapel:
    gezogen = stapel.pop(-1)

    print(f"Die Karte {gezogen} wurde gezogen.\n")

print("Der Stapel ist nun leer. ")


