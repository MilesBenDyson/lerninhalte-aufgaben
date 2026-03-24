# Reflexion – Zeiterfassungs-Tool

## ✅ Was ich gelernt und gefestigt habe

### 1. Datetime basics
- Strings wie `12:30` oder `31.08.25` in `datetime`-Objekte umwandeln.
- Mit `datetime.combine()` Datum + Uhrzeit zusammensetzen.
- Mit `.strftime()` Datums- und Zeitangaben formatiert ausgeben (`%H:%M`, `%d.%m.%Y`, `%Y-%m-%d`).

### 2. Zeitdifferenzen berechnen
- `ende - start` liefert ein `timedelta`.
- `.total_seconds()` gibt die Dauer in Sekunden zurück (auch über längere Intervalle).
- Eigene Hilfsfunktion `zeit_sek(start, ende)` geschrieben.

### 3. Listen & Dictionaries
- Liste `bloecke` gebaut, in der jeder Block ein Dictionary ist.
- Keys: `"start"`, `"ende"`, `"typ"`, `"sekunden"`.
- Elemente mit `.append()` dynamisch hinzugefügt.

### 4. JSON speichern
- Datenstruktur (`log`) mit `json.dump()` gespeichert.
- `ensure_ascii=False` und `indent=2` genutzt → lesbare, saubere JSON-Dateien.

### 5. Schleifen & Steuerung
- Endlosschleife mit Abbruch bei leerem Input (`choice == ""`).
- Eingaben werden so gesammelt, bis gespeichert werden soll.

### 6. Projekt-Workflow
- Vom **ersten Gerüst** → **Blöcke erfassen** → **Sekunden berechnen** → **JSON schreiben**.
- Schrittweise vorgegangen, ohne Perfektionismus.
- Richtige Strategie: *erstmal lauffähig machen, später verschönern*.

---

## 🎯 Mein Lerneffekt
- Kombination von **Datetime + JSON + Schleifen** = ein echtes kleines Programm.
- JSON muss man **komplett neu schreiben** statt einfach mit `"a"` anhängen.
- Ich habe ein Gefühl für **Listen von Dicts** bekommen – ein wichtiges Muster für viele Programme.

---

## 🚀 Fazit
Mit dieser Aufgabe habe ich meine Grundlagen (datetime, Schleifen, Listen, Dicts, JSON) **stark gefestigt**.  
Das ist ein echter Meilenstein für meinen Lernweg. 🎉
