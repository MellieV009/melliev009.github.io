#################################################
# Opdracht 1: Druk de huidige datum en tijd af. #
#################################################
import datetime

#Onderstaande script haalt de huidige datum en tijd op.
huidige_datum_tijd = datetime.datetime.now()

#Onderstaande script print de datum en tijd.
print("Huidige datum en tijd:", huidige_datum_tijd)

#Als je de datum en tijd wilt afdrukken in een specifiek formaat, kun je de strftime() methode gebruiken 
#om de datum en tijd naar een string te formatteren. Bijvoorbeeld:

#Onderstaande script laat zien hoe je de datum en tijd formateert naar een specifiek formaat:
datum_tijd_str = huidige_datum_tijd.strftime("%Y-%m-%d %H:%M:%S")

#Onderstaande script print de geformateerde datum en tijd af.
print("Huidige datum en tijd (geformatteerd):", datum_tijd_str) 


##################################################################################################
# Opdracht 2: Maak  een variabele Path aan om het pad te definiëren naar onderstaande bestanden. #
##################################################################################################
from pathlib import Path

#Onderstaande script definieert het pad naar de bestanden.
pad_naar_bestanden = Path("C:\\Users\\Melvin Verriet\\Documents\\GitHub\\melliev009.github.io\\data\\csv")

#Met onderstaande script gebruik je het pad variabele om de bestanden te openen.
docenten_csv = open(pad_naar_bestanden / "Docenten.csv", 'r+')
studenten_csv = open(pad_naar_bestanden / "Studenten.csv", 'r+')

#Met onderstaande script kun je de bestanden lezen.
for line in docenten_csv:
    print(line.strip())

for line in studenten_csv:
    print(line.strip())

wissen = input('Wil je de bestanden leegmaken? (j/n): ').lower()
if wissen == 'j':
    docenten_csv.truncate(0)
    studenten_csv.truncate(0)

#Met onderstaande script sluit je de bestanden na gebruik.
docenten_csv.close()
studenten_csv.close()

##################################################################
# Verander nu de loop op zo’n manier dat zodra hij               #
# bij het getal 3 is, de loop stopt en de volgende output geeft: #
##################################################################

for getal in range(1, 5):
    if getal == 3:
        print("De loop stopt nu", getal)
        break
    print("Het getal is nu", getal)
