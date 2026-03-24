🏅 Zertifikat: Hairmetal-Quiz (CLI-Tool mit Fragesystem)
Aufgabenbeschreibung:
→ Programmiere ein Hairmetal-Quiz in Python, das:

den User begrüßt

Regeln erklärt

Fragen stellt (Multiple Choice / freie Eingabe)

Punkte zählt

besondere Bedingungen erlaubt:

"weiter" → Frage überspringen

"Ich liebe Schlager" → Quiz sofort beenden

Erreicht:
✅ Begrüßung und Regeln sehr schön formuliert → hohe Benutzerfreundlichkeit
✅ Punkte zählen korrekt umgesetzt
✅ Fragen als Texte gespeichert und ausgegeben → sauber
✅ Eingaben abgefangen (weiter, Ich liebe Schlager) → sehr gut!
✅ Programmabbruch bei "Ich liebe Schlager" → korrekt mit sys.exit() gelöst
✅ Schöne thematische Gestaltung ("wie füllig ist Deine Mähne") → sehr kreativ → Pluspunkt!

Kritikpunkte & Verbesserungen:
⚠️ Code-Struktur noch linear → alles in einer großen Kette → Verbesserung durch Nutzung von Funktionen wäre sinnvoll gewesen (haben wir damals als Tipp besprochen)
⚠️ Kommentierte Antworten (antwort1 = "Ratt", etc.) waren im Code noch auskommentiert → das war okay als Test, aber für finale Version sollten die Fragen/Antworten besser in Variablen/Listen gespeichert werden → saubere Trennung von Daten und Logik.

⚠️ Fragen und Antwortprüfung → fest im Code → Verbesserung wäre hier der Einsatz von Schleifen + Liste von Fragen gewesen → hatten wir als mögliches "nächstes Level" besprochen.

Fazit:
✅ Für das angestrebte Ziel Hairmetal-Quiz als CLI → sehr charmant und funktional gelöst
✅ User Experience → sehr hoch → liebevolle Gestaltung
✅ Steuerlogik verstanden und korrekt umgesetzt (mit sys.exit(), weiter, etc.)
✅ Punkte zählen → korrekt

Level 100% bestanden für den geforderten Schwierigkeitsgrad.

→ für die nächste Version (bei Lust) könntest du:

Funktionen nutzen (z.B. frage_stellen() → schöner Code)

Fragen/Antworten aus einer Liste holen → gut für Erweiterbarkeit.

Gesamtfazit zum Hairmetal-Quiz:
Sehr kreativ, funktional und korrekt gelöst.
Du hast die wichtigen Steuerlogiken (Schleifen, sys.exit, Eingabekontrolle) verstanden und umgesetzt → das ist exakt das Lernziel dieser Übung.