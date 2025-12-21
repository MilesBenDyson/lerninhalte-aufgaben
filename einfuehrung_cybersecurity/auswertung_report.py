'''🧩 Ziel: kleines Analyse-Tool für deinen Report

Du schreibst ein Python-Skript, das deine gespeicherte Report-Datei einliest und dir einfache Statistiken ausgibt.'''

import json

# reportdatei öffnen
report_datei = "C:\\Users\\bensc\\Desktop\\IT\\Python\\lerninhalte-aufgaben-uebungen\\einfuehrung_cybersecurity\\report_2025-11-11_1.json"

# datei laden
with open(report_datei, 'r', encoding='utf-8') as f:
    reportliste = json.load(f)

count_hosts = 0
count_hosts_len = len(reportliste)
for h in reportliste:
    if h['host']:
        count_hosts += 1

print(f"Es sind insgesamt {count_hosts} vorhanden.")
print(f"Es sind insgesamt {count_hosts_len} vorhanden.")