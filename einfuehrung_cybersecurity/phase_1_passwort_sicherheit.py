'''Aufgabe: Passwort-Stärke-Prüfer (Coding-Snack)

Ziel: Schreibe ein kleines Python-Programm, das ein Passwort bewertet und Verbesserungstipps gibt.
Lernziele: input()/print(), Zeichenprüfung, Funktionen, hashlib (Hashing), einfache Unit-Tests (manuell).

Anforderungen (Minimal)

Lies ein Passwort von der Konsole ein.

Prüfe folgende Kriterien:

Länge ≥ 8 Zeichen

Mindestens eine Großbuchstabe

Mindestens eine Kleinbuchstabe

Mindestens eine Ziffer

Mindestens ein Sonderzeichen (z. B. !@#$%ˆ&*()-_+=)

Vergib eine Punktzahl 0–5 (ein Punkt pro erfülltes Kriterium).

Gib eine verbale Bewertung:

0–1: Sehr schwach

2–3: Schwach

4: Gut

5: Sehr gut

Gib konkrete Verbesserungstipps (z. B. „Länger machen“, „Großbuchstaben hinzufügen“).

(Bonus, kurz) Zeige den SHA-256 Hash des Passworts (nur lokal, demonstrativ).'''

import hashlib
import string

SPECIALS = set("!@#$%^&*()-_+=[]{};:,.<>?/|\\`~\"'")


def check_length(pw: str) -> bool:
    return len(pw) >= 8

def has_upper(pw: str) -> bool:
    return any(c.isupper() for c in pw)

def has_lower(pw: str) -> bool:
    return any(c.islower() for c in pw)

def has_digit(pw: str) -> bool:
    return any(c.isdigit() for c in pw)

def has_special(pw: str) -> bool:
    return any(c in SPECIALS for c in pw)

def score_password(pw: str) -> int:
    score = 0
    if check_length(pw): score += 1
    if has_upper(pw): score += 1
    if has_lower(pw): score += 1
    if has_digit(pw): score += 1
    if has_special(pw): score += 1
    return score

wertung = None

eingabe = input("Gib dein Passwort ein. Es soll mindestens 8 Zeichen lang sein. ")
score = score_password(eingabe)
if score >= 4:
    wertung = "Dein Passwort ist stark."
elif score < 4 and score >= 2:
    wertung = "Dein Passwort ist mittelstark."
else:
    wertung = "Dein Passwort ist zu schwach."

print(wertung)

def give_feedback(pw: str) -> list[str]:
    tipps = []
    if not check_length(eingabe):
        tipps.append("Dein Passwort ist zu kurz. Es müssen mind. 8 Zeichen sein. ")
    if not has_lower(eingabe):
        tipps.append("Dein Passwort muss mind. einen Kleinbuchstaben enthalten. ")
    if not has_upper(eingabe):
        tipps.append("Dein Passwort muss mind. einen Großbuchstaben enthalten. ")
    if not has_digit(eingabe):
        tipps.append("Dein Passwort muss mind. eine Zahl enthalten. ")
    if not has_special(eingabe):
        tipps.append("Dein Passwort muss mind. ein Sonderzeichen enthalten. ")
    if not tipps:
        tipps.append("Dein Passwort ist sehr gut. ")
    return tipps
give_feedback(eingabe)

print("\nVerbesserungstipps:")

for i in give_feedback(eingabe):
    print(i)




