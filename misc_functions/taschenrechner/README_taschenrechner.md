# 🧮 Taschenrechner (Übungsaufgabe)

Dies ist eine Python-Übungsaufgabe im Rahmen des Projekts **lerninhalte-aufgaben**.

## 📋 Beschreibung

Ein einfacher CLI-Taschenrechner, der Benutzereingaben im Format `Zahl Operator Zahl` verarbeitet (z. B. `3 + 4`). Das Ergebnis wird angezeigt und mit Zeitstempel in einer Protokolldatei gespeichert.

Beispielausgabe:
```
Was soll ich rechnen? 3 * 5
Dein Ergebnis lautet: 15 | 2025-06-14 12:34:56
```

## ✅ Lernziele

- Umgang mit Benutzereingaben (`input`)
- Verwendung von `eval()` zur dynamischen Auswertung von Rechenausdrücken
- Nutzung des `datetime`-Moduls für Zeitstempel
- Schreiben in Textdateien mit `with open(..., "a")`
- Fehlerbehandlung mit `try/except`

## 🗂️ Dateien

| Datei | Beschreibung |
|-------|--------------|
| `taschenrechner_übungsaufgabe.py` | Das Hauptprogramm |
| `rechenprotokoll.txt` | Protokoll der Rechnungen (automatisch erstellt) |
| `zertifikat_taschenrechner.md` | Zertifikat für die abgeschlossene Aufgabe |
| `README.md` | Diese Datei |

## 🚀 Ausführen

Starte das Programm über ein Terminal mit:
```bash
python taschenrechner_übungsaufgabe.py
```

> Hinweis: Dezimalzahlen müssen mit Punkt (`.`) statt Komma (`,`) eingegeben werden.

## 🛡️ Sicherheitshinweis

Die Funktion `eval()` ist mächtig, aber potentiell unsicher. In produktiven Umgebungen sollte ein sicherer Parser verwendet werden.

## 📅 Status

Aufgabe abgeschlossen am 14. Juni 2025 ✅
