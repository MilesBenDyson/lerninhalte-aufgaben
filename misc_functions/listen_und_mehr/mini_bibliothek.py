"""🧩 Aufgabe – Mini-Bibliothek

Stell dir vor, du hast eine kleine Bücherverwaltung:

Erstelle eine Liste bücher = [].

Füge mit .append() drei Bücher hinzu, z. B. "Herr der Ringe", "Harry Potter", "Der Hobbit".

Simuliere einen Stapel (LIFO):

Ziehe mit .pop() das oberste Buch vom Stapel.

Drucke: "Oben lag <Buch>".

Füge wieder ein neues Buch hinzu, z. B. "Game of Thrones".

Simuliere eine Warteschlange (FIFO):

Ziehe mit .pop(0) das erste hinzugefügte Buch.

Drucke: "Als erstes ausgeliehen wurde <Buch>".

Gib am Ende die aktuelle Bücherliste aus."""

buecher = []

def sammeln(liste, buch):
    return liste.append(buch)

sammeln(buecher, "Harry Potter")
sammeln(buecher, "Herr der Ringe")
sammeln(buecher, "Der Struwwelpeter")

oberste_buch = buecher.pop()
print(f"Das oberste Buch ist '{oberste_buch}'")

sammeln(buecher, "Game of Thrones")
print(f"Als erstes wurde '{buecher.pop(0)}' ausgeliehen. Es sind noch die Titel {buecher} im Bestand. ")