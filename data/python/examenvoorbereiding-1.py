#Onderstaande code opent de 2 bestanden.
fietsonderdelen = open("C:\\Users\\Melvin Verriet\\AppData\\Local\\Programs\\Python\\Python311\\Fiets BV\\Nijmegen\\Administratie\\fietsonderdelen.csv")
klanten = open("C:\\Users\\Melvin Verriet\\AppData\\Local\\Programs\\Python\\Python311\\Fiets BV\\Nijmegen\\Administratie\\klanten.csv")

#Onderstaande code toont de inhoud van de 2 bestanden.
print(fietsonderdelen.read())
print(klanten.read())

#In onderstaande code print ik de huidige datum en tijd
from datetime import datetime
#Onderstaande code laat de tijd op het scherm zien
tijd = datetime.now()
print(tijd)
