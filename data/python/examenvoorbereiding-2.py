#Oefenopdracht 1 berekent de leeftijd in hondenjaren
"""" 
#Onderstaande code vraagt de leeftijd van de hond in jaren
leeftijd= int(input("Hoe oud is de hond"))

#De eerste 2 jaar is 10,5 mensenjaren.
if leeftijd < 3: 
    #Onderstaande code berekent het aantal jaar * 10.5 en laat de uitkomst zien
    hondenjaren = leeftijd * 10.5
    print(hondenjaren)
#Onderstaande code is van toepassing als de hond ouder is dan 2 jaar.
else:
    #Onderstaande code haalt 2 jaar van de leeftijd af voor de som 2 * 10.5
    leeftijd_aangepast = leeftijd - 2 
    #Onderstaande code berekent de resterende jaren.
    som = leeftijd_aangepast * 4
    #Onderstaande code telt alles bij elkaar op en laat dit zien
    leeftijd_totaal = som + 21 
    print(leeftijd_totaal )
"""
#Oefenopdracht 2 Maakt een programma dat bepaalt of een bepaald jaar een schrikkeljaar is of niet
jaar = int(input("Welk jaar is het"))
#De onderstaande code kijkt of het jaar gedeeld kan worden door of 400; en niet door 100.
if (jaar % 4 == 0 and jaar % 100 != 0) or jaar % 400 == 0:
    print("Dit is een schrikeljaar")  
else:
    print("Dit is geen schrikeljaar") 