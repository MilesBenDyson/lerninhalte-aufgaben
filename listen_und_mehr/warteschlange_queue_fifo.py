"""🧩 Snack – kleine Warteschlange

Erstelle eine Liste warteschlange = [].

Füge mit .append() drei „Kunden“ hinzu, z. B. "Kunde A", "Kunde B", "Kunde C".

Gib die Warteschlange aus.

Jetzt wird der erste Kunde bedient – nutze dafür .pop(0).
👉 Unterschied zum Stack: diesmal nicht der letzte, sondern der erste verlässt die Liste.

Drucke den bedienten Kunden und die aktuelle Warteschlange."""

warteschlange = []

def hinzufügen(liste, kunde):
    return liste.append(kunde)

hinzufügen(warteschlange, "Kunde A")
hinzufügen(warteschlange, "Kunde B")
hinzufügen(warteschlange, "Kunde C")

print(warteschlange)

#ersten Kunden bedienen
bedienen = warteschlange.pop(0)

print(f"Es wurde zuerst {bedienen} bedient. Es bleiben noch {warteschlange} übrig. ")

hinzufügen(warteschlange, "Kunde D")
hinzufügen(warteschlange, "Kunde E")
print("Es kamen neue Kunden hinzu. ")
while warteschlange:
    bedienen2 = warteschlange.pop(0)
    print(f"Es wurde der Kunde {bedienen2} bedient." )
