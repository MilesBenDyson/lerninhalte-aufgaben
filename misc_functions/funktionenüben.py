import datetime

# minutes_diff(start_str, end_str) --> soll zwei Uhrzeiten im richtigen Format erhalten und:
# 1. beide Zeitpunkte mit datum heute kombiniert
# 2. differenz diff _ end - start bildet
# 3. zwei Werte ausgibt: min_via_second + min_via_total_seconds
# Bonus: in einem Text speichern, der den Unterschied seconds und _total_seconds() erklärt

def minutes_diff(start, end):
    # 1.:
    start_date = datetime.datetime.combine(datetime.date.today(), start)
    end_date = datetime.datetime.combine(datetime.date.today(), end)

    # 2.:
    diff_end_start = end_date - start_date

    # 3.:
    wert1 = diff_end_start.seconds // 60
    wert2 = int(diff_end_start.total_seconds() // 60)

    print(f"Der erste Wert gibt {wert1} Minuten wieder und wurde durch '.seconds' definiert. Dadurch erhält man die komplette Sekundenanzahl innerhalb von 24 Stunden. In diesem Fall kein Problem. Bei Wert 2 erhalten wir {wert2} Minuten. Ohne 'int' davor, wäre es ein float und würde aber auch alle Sekunden (daher TOTAL_seconds) wiedergeben, auch wenn die Differenz über 24 Stunden hinusgehen würde. ")

def uhrmacher(stunden, minuten):
    return datetime.time(stunden, minuten)

minutes_diff(uhrmacher(6, 30), uhrmacher(16, 50 ))

