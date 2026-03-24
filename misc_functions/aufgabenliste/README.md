# 🗒️ Aufgabenliste (CLI-Tool)

Ein einfaches Python-Programm zum Verwalten deiner Aufgaben über die Kommandozeile.  
Aufgaben können hinzugefügt, als erledigt markiert oder gelöscht werden. Die Liste wird automatisch als JSON-Datei gespeichert – datumsbasiert.

---

## ✅ Funktionen

- Neue Aufgabenliste erstellen (automatisch mit aktuellem Datum)
- Bestehende Aufgabenlisten laden (per Datumseingabe)
- Aufgaben hinzufügen
- Aufgaben löschen
- Aufgaben als erledigt markieren (**noch in Arbeit**)
- Automatische Speicherung beim Beenden
- Steuerung über einfache Tasteneingaben

---

## 💻 Benutzung

### 1. Starte das Programm

```bash
python aufgabenliste_uebungsaufgabe.py
```

### 2. Auswahl beim Start

- **Enter** → Neue Aufgabenliste für das heutige Datum wird erstellt
- **Datum eingeben (z. B. `21.06.2025`)** → Bestehende Aufgabenliste laden
- **`stopp`** → Programm beenden

### 3. Menü

```
1. Aufgabe hinzufügen
2. Aufgabe abhaken (noch nicht implementiert)
3. Aufgabe löschen
```

Innerhalb der Eingabe:
- **`q`** → zurück zum Menü
- **`stopp`** → Programm beenden

---

## 💾 Dateien

- Die Aufgaben werden unter dem Namen `aufgaben-tt.mm.jjjj.json` gespeichert
- Der Status jeder Aufgabe wird später als `{"name": ..., "erledigt": True/False}` gespeichert

---

## 📦 Abhängigkeiten

- Python 3.9 oder höher
- Keine externen Pakete – nutzt nur:
  - `json`
  - `datetime`
  - `sys`
  - `os` (optional)

---

## 🔧 Noch geplante Features

- [ ] Aufgaben als **erledigt markieren**
- [ ] Aufgaben **nummeriert anzeigen**
- [ ] **Status-Symbole** anzeigen (✅/❌)
- [ ] Aufgaben nach **Status filtern** (nur offene)
- [ ] Automatische Backups

---

## 👨‍💻 Autor

Ben aka MilesBenDyson  
Lernprojekt im Rahmen der Python-Grundlagen mit Coach 🤖
