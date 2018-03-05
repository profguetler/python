# Zahlenraten

import random
zufallszahl = random.randint(1,100)

titel = "Willkommen beim Zahlen-Rate-Spiel!"
text = "Versuche meine Zahl zwischen 1 und 100 zu erraten."
eingabeText = "Bitte gib eine Zahl ein: "

print(titel)
print(text)

fertig = False
anzahlDerVersuche = 0

while fertig == False:
    anzahlDerVersuche = anzahlDerVersuche + 1
    zahl = int(input(eingabeText))
    if (zahl == zufallszahl):
        print("gewonnen!")
        fertig = True
    elif (zahl < zufallszahl):
        print("die gesuchte Zahl ist größer")
    else:
        print("die gesuchte Zahl ist kleiner")

print("super, du hast dafür nur ", anzahlDerVersuche, " Versuche benötigt.")
print("ende.")
