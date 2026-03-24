import datetime

start = datetime.time(8, 30)
ende = datetime.time(15, 45)

def combi(zeit):
    return datetime.datetime.combine(datetime.date.today(), zeit)

dauer = combi(ende) - combi(start)

stunden = int(dauer.total_seconds() // 3600)

minuten = int((dauer.total_seconds() % 3600) // 60)

print(f"Die Differenz beträgt {stunden} Stunden und {minuten} Minuten.")