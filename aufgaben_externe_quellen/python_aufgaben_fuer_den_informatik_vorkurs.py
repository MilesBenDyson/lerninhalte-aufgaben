'''1 Einstieg
1.1 Gib den Text “Hallo Welt” aus.
1.2 Hänge zwei Strings aneinander.
1.3 Gib einen Text viermal aus.
Hinweis: Mit etwas herumprobieren geht das sehr schnell, ohne den Text
4-mal zu kopieren!
1.4 Multipliziere zwei Zahlen.
1.5 Dividiere zwei Zahlen. Was passiert, wenn du durch Null teilst?
1.6 Ziehe die Quadratwurzel aus einer Zahl.
'''

# 1.1
print("Hallo Welt")
# 1.2
string1 = "an"
string2 = "einander"
string_glued = string1 + string2
print(string_glued)
# 1.3
einen_text = "Tatüüütataaaa\n"
print(4 * einen_text)
# 1.4
zahl_1 = 3
zahl_2 =5345
multigebnis = zahl_1 * zahl_2
print(multigebnis)
# 1.5
divigebnis = zahl_1 / zahl_2
print(divigebnis)
try:
    nullversuch = divigebnis / 0
except ZeroDivisionError:
    print("Es wurde versucht durch '0' zu dividieren. Das ist so nicht zulässig")

# 1.6
zahl_9 = 9
quadawu = 0
for i in range(1, zahl_9 + 1):
    if i * i == zahl_9:
        quadawu = i
        break

if quadawu > 0:
    print(f"Die Quadratwurzel von {zahl_9} lautet {quadawu}")
else:
    print(f"Es konnte keine Ganzzahl als Quadratwurzel von {zahl_9} ermittelt werden.")

'''2 If - Abfragen
2.1 Sortiere zwei vorher festgelegte Zahlen nach Größe und gib sie in der richtigen
Reihenfolge aus.
2.2 Bestimme die Größte aus drei vorher festgelegten Zahlen und gib diese Zahl
aus.
2.3 Sortiere drei vorher festgelegte Zahlen und gib sie in der richtigen Reihenfolge
aus. Zeichne dazu zuerst ein Ablaufdiagramm/Flussdiagramm, wie du es aus
der Vorlesung kennst. (Mit Paper+Stift)
2.4 Überprüfe, ob ein vorher festgelegtes Jahr ein Schaltjahr ist. Dabei sind folgende 
Regeln zu beachten:
nicht durch 4 teilbar kein Schaltjahr
durch 4 teilbar Schaltjahr
durch 100 teilbar kein Schaltjahr
durch 400 teilbar Schaltjahr
Beispiele: 1900 kein Schaltjahr, 2000 Schaltjahr, 2004 Schaltjahr, 2006 kein
Schaltjahr, ...
1
2.5 Lass den Benutzer Temperatur (warm, kalt) und Wetter eingeben (regnerisch,
verschneit, sonnig) und gib ihm einen Vorschlag zurück, wie er sich dem Wetter ¨
entsprechend kleiden soll.
Beispiel:
Eingabe: warm und sonnig
Ausgabe: Ein T-Shirt reicht fur heute völlig!'''

# 2.1
zahl_sort_1 = 2314
zahl_sort_2 = 45235

if zahl_sort_1 >= zahl_sort_2:
    print(zahl_sort_1, zahl_sort_2)
else:
    print(zahl_sort_2, zahl_sort_1)

# 2.2
zahl_sort_3 = 3453245234

if zahl_sort_1 >= zahl_sort_2 and zahl_sort_1 >= zahl_sort_3:
    print(zahl_sort_1)
elif zahl_sort_2 >= zahl_sort_3:
    print(zahl_sort_2)
else:
    print(zahl_sort_3)

# 2.3
'''
Flussdiagramm:
Start
aa, bb, cc

aa > bb?
ja?
aa, bb = bb, aa

bb > cc?
ja?
bb, cc = cc, bb

aa > bb?
ja?
aa, bb = bb, aa

Ausgabe aa, bb, cc
Ende

'''
aa = 3
bb = 23
cc = 1

if aa > bb:
    aa, bb = bb, aa
if bb > cc:
    bb, cc = cc, bb
if aa > bb:
    aa, bb = bb, aa
print(aa, bb, cc)

'''2.4 Überprüfe, ob ein vorher festgelegtes Jahr ein Schaltjahr ist. Dabei sind folgende 
Regeln zu beachten:
nicht durch 4 teilbar kein Schaltjahr
durch 4 teilbar Schaltjahr
durch 100 teilbar kein Schaltjahr
durch 400 teilbar Schaltjahr
Beispiele: 1900 kein Schaltjahr, 2000 Schaltjahr, 2004 Schaltjahr, 2006 kein
Schaltjahr, ...'''
# 2.4

jahr = 2001

flag = False

if jahr % 4 == 0:
    flag = True
if jahr % 100 == 0:
    flag = False
if jahr % 400 == 0:
    flag = True
if flag:
    print(f"{jahr} ist ein Schaltjahr")
else:
    print(f"{jahr} ist kein Schaltjahr")


if jahr % 4 != 0:
    flag = False
elif jahr % 400 == 0:
    flag = True
elif jahr % 100 == 0:
    flag = False
else:
    flag = True
if flag:
    print(f"{jahr} ist ein Schaltjahr")
else:
    print(f"{jahr} ist kein Schaltjahr")

# 2.5
temperatur = input("Ist es warm oder kalt?\n")
wetter = input(f"Ist es\n- regnerisch\n- verschneit {'oder':>10}\n- sonnig?")

shirt = False
regenschirm = False
jacke = False
winterkleidung = False
leichte_kleidung = False


if temperatur.lower() == 'warm':
    shirt = True
if wetter.lower() == 'regnerisch':
    regenschirm = True
    leichte_kleidung = True
if temperatur.lower() == 'kalt':
    jacke = True
elif wetter.lower() == 'regnerisch':
    regenschirm = True
elif wetter.lower() == 'verschneit':
    winterkleidung = True
elif wetter.lower() == 'sonnig':
    jacke = True
kleiderschrank = [shirt, regenschirm, jacke, winterkleidung, leichte_kleidung]
for i in kleiderschrank:
    if i:
        print(i)