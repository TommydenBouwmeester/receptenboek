from ingredient import Ingredient
from stap import Stap

class Recept:
    def __init__(self, naam, omschrijving):
        self.__naam = naam
        self.__omschrijving = omschrijving
        self.__ingredient_list = []
        self.__stappen = []
        self.__aantal_personen = 1 

    def voeg_ingredient_toe(self, ingredient: Ingredient):
        self.__ingredient_list.append(ingredient)

    def get_ingredienten(self):
        return self.__ingredient_list
    
    def get_naam(self):
        return self.__naam

    def voeg_stap_toe(self, stap):
        self.__stappen.append(stap)

    def set_aantal_personen(self, personen: int):
        vermeningvuldigingsfactor = personen / self.__aantal_personen
        for item in self.__ingredient_list:
            huidige_hoeveelheid = item.get_hoeveelheid()
            nieuwe_hoeveelheid = huidige_hoeveelheid * vermeningvuldigingsfactor
            item.set_hoeveelheid(nieuwe_hoeveelheid)
        
        self.__aantal_personen = personen

    def get_aantal_personenen(self):
        return self.__aantal_personen
    
    def get_plantaardig_recept(self, plantaardig: bool):
        totaal_kcal = 0
        titel = "RECEPT: " + self.__naam
        if plantaardig:
            titel = titel + "(PLANTAARDIGE VERSIE)"

        overzicht = titel + "\n"
        overzicht = overzicht + "OMSCHRIJVING:" + self.__omschrijving + "\n"
        overzicht = overzicht + "AANTAL PERSONEN: " + str(self.__aantal_personen) + "\n\n"
        overzicht = overzicht + "INGREDIËNTEN:\n"
        for item in self.__ingredient_list:
            gekozen_ingredient= item.get_ingredient(plantaardig)
            kcal_totaal_ingrediënt = gekozen_ingredient.get_kcal() * self.__aantal_personen
            totaal_kcal = totaal_kcal + kcal_totaal_ingrediënt
            naam = gekozen_ingredient.get_naam()
            hoeveelheid = gekozen_ingredient.get_hoeveelheid()
            eenheid = gekozen_ingredient.get_eenheid()
            overzicht = overzicht + f" - {naam}, {hoeveelheid} {eenheid}, {kcal_totaal_ingrediënt} kcal\n"
        overzicht = overzicht + "\nBEREIDING:\n"
        teller = 1
        for stapje in self.__stappen:
            overzicht = overzicht + str(teller) + ". " + str(stapje) + "\n"
            teller = teller + 1
        overzicht = overzicht + "\nTOTALE CALORIEËN: " + str(totaal_kcal)
        return overzicht
    
    def __str__(self):
        return self.get_plantaardig_recept(False)
        
           
















    


