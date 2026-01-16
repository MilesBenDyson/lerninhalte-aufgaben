import socket

host = "127.0.0.1"
port = 335

#1️⃣ Erzeugen – „Ich brauche ein Werkzeug“
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#2️⃣ Begrenzen – „Ich will nicht ewig warten“
s.settimeout(0.3)

#3️⃣ Testen – „Ist da jemand?“
result = s.connect_ex((host, port))

#4️⃣ Aufräumen – „Fertig, Werkzeug weglegen“
s.close()
