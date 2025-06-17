from random import randint
zahl = randint(1, 100)

while True:

    print("An welche Zahl denke ich gerade? ")
    versuch = int(input("Gib eine Zahl zwischen 1 - 100 ein. "))

    if versuch < zahl:
        print("Nein, meine Zahl ist größer.")


    elif versuch > zahl:
        print("Nein, meine Zahl ist kleiner. ")


    elif versuch > 100:
        print("Die Zahl darf nicht über 100 sein. ")


    elif versuch < 1:
        print("Die Zahl darf nicht weniger als 1 sein. ")


    elif versuch == zahl:
        print("########Super! Du hast meine Zahl erraten!########")
        break

    else:
        print("Deine Eingabe ist nicht gültig. ")
