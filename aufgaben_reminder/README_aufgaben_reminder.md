# 🧠 Aufgaben-Reminder (Übungsaufgabe)

## Ziel der Übung
Das Ziel dieser Übung ist es, ein kleines Python-Programm zu schreiben, das an bevorstehende Aufgaben erinnert. Die Aufgaben sollen in einer JSON-Datei gespeichert und nach ihrem Fälligkeitsdatum gefiltert angezeigt werden.

---

## Anforderungen

### 1. Aufgaben speichern
- Die Aufgaben werden in einer Datei namens `aufgaben.json` gespeichert.
- Jede Aufgabe ist ein Dictionary mit den Feldern:
  - `"titel"`: Titel der Aufgabe (z. B. `"Mathe lernen"`)
  - `"beschreibung"`: kurze Info (optional)
  - `"faellig_am"`: Fälligkeitsdatum im Format `YYYY-MM-DD`

### 2. Aufgaben anzeigen
- Das Programm `aufgaben_reminder_uebungsaufgabe.py` soll:
  - die Datei `aufgaben.json` laden,
  - alle Aufgaben anzeigen, die in den nächsten 7 Tagen fällig sind.

### 3. Bonus (optional)
- Aufgaben farblich hervorheben, je nach Dringlichkeit:
  - Heute fällig: 🔴 **rot**
  - In 1–3 Tagen fällig: 🟠 **orange**
  - In 4–7 Tagen fällig: 🟢 **grün**
- Eingabe ermöglichen, um eine neue Aufgabe hinzuzufügen.

---

## Hinweise
- Verwende das `datetime`-Modul für Datumsberechnungen.
- Arbeite mit `json` zum Einlesen und Speichern der Daten.
- Achte auf fehlerfreie Eingabeformate (z. B. per `try-except`).

---

## Beispielaufgabe

```json
{
  "titel": "Git Commit üben",
  "beschreibung": "Lerne, wie man git status, add, commit und push benutzt.",
  "faellig_am": "2025-07-04"
}
```

---

## Lernziel
Diese Übung festigt den Umgang mit:
- dem `datetime`-Modul,
- dem JSON-Format,
- dem Datei-Handling (`open()`),
- dem logischen Filtern von Daten,
- sowie dem Schreiben eines klar strukturierten Skripts.

---

Viel Erfolg beim Coden! 🚀
