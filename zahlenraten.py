# Zahlenraten

import random

titel = "Willkommen beim Zahlen-Rate-Spiel!"
print(titel)

von = int(input("Bitte die Zufallszahl-Unterschranke festlegen: "))
bis = int(input("Bitte die Zufallszahl-Oberschranke festlegen: "))
zufallszahl = random.randint(von, bis)

text = "Versuche meine Zahl zwischen " + str(von) + " und " + str(bis) + " zu erraten."
print(text)

eingabeText = "Bitte gib eine Zahl ein: "
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
