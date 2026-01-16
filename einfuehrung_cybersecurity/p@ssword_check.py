import json
import hashlib
liste_sonderzeichen = ["!", "§", "$", "%", "&", "/", "(", ")", "=", "?", "\\", "#", "*", "+"]
pw = "hallo12345!"
p_hash = None

def hashy(p):
    #passwort in bytes wandeln
    p_bytes = p.encode('utf-8')
    p_hash = hashlib.sha256(p_bytes)
    p_hex = p_hash.hexdigest()
    return p_hex

p_hash = hashy(pw)

liste_check = []
def laenge(p):
    laenge_pw = False
    x = len(p)
    if x < 8:
        print(f"{p} ist zu kurz. Du brauchst mindestens 8 Zeichen.")
    else:
        laenge_pw = True
        return laenge_pw
    return laenge_pw
def mind_zahl(p):
    m_zahl = False
    anzahl_zahl = 0
    for i in p:
        if i.isdigit():
            anzahl_zahl += 1
    if anzahl_zahl > 0:
        m_zahl = True

    else:
        print(f"{p} enthält keine Zahl, es muss aber mindestens ein vorkommen.")
    return m_zahl
def mind_gross(p):
    m_gross = False
    anzahl_g = 0
    for i in p:
        if i.isupper():
            anzahl_g += 1
    if anzahl_g > 0:
        m_gross = True

    else:
        print(f"{p} enthält keinen Großbuchstaben, es wird jedoch mindestens einer benötigt.")
    return m_gross

def mind_sonder(p):
    m_sonder = False
    anzahl = 0
    for i in p:
        for s in liste_sonderzeichen:
            if i == s:
                anzahl += 1
    if anzahl > 0:
        m_sonder = True

    else:
        print(f"{p} enthält keines der erlaubten Sonderzeichen, es wird jedoch mindestens eines aus folgender Liste benötigt:\n{liste_sonderzeichen}")
    return m_sonder
laenge_pw = laenge(pw)
m_zahl = mind_zahl(pw)
m_gross = mind_gross(pw)
m_sonder = mind_sonder(pw)
liste_check.append({'Passwort': p_hash, 'Passwortlänge': laenge_pw, 'Mindestens eine Zahl': m_zahl, 'Mindestens ein Großbuchstabe': m_gross, 'Mindestens ein Sonderzeichen': m_sonder})


for eintrag in liste_check:
    bewertung = 0
    passwort = eintrag['Passwort']
    for value in eintrag.values():
        if isinstance(value, bool) and value:
            bewertung += 1

    if bewertung == 0:
        print(f"{passwort} ist ein schwaches Passwort.")
    elif bewertung > 0 and bewertung < 3:
        print(f"{passwort} ist ein mittelstarkes Passwort.")
    else:
        print(f"{passwort} ist ein starkes Passwort.")