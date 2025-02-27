#Module importieren
import random

#Höchste Zahl definieren
maxint = int(input("Höchste Zahl: "))
maxstr = str(maxint)

#Computer und Spieler entscheidung
computer = random.randint(1,maxint)

while True:
    player = int(input("wähle eine zahl zwischen 1 und " + maxstr +": "))

#Restlicher Code
    if computer == player:
        print("richtig erraten")
        print(" ")
        break
    elif computer > player:
        choice = input("zu klein, nochmal versuchen? (y/n) ")
        print(" ")
    else:
        choice = input("zu groß, nochmal versuchen? (y/n) ")
        print(" ")
        
#Loop-Schleife
    if choice == "y":
        print(" ")
    elif choice == "n":
        print("danke fürs spielen")
        break
    else:
        print("ungültige antwort, automatisches ende")
        break