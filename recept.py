from ingredient import Ingredient
from stap import Stap


class Recept:
    def __init__(self, naam, omschrijving):
        self.__naam = naam
        self.__omschrijving = omschrijving
        self.__ingredient_list = []
        self.__stappen = []
    
    def voeg_ingredient_toe(self, ingredient: Ingredient):
        self.__ingredient_list.append(ingredient)

    def get_ingredienten(self):
        return self.__ingredient_list
    
    def get_naam(self):
        return self.__naam
    
    def voeg_stap_toe(self, stap: Stap):
        self.__stappen.append(stap)

    def __str__(self):
        overzicht = "RECEPT: " + self.__naam + "\n"
        overzicht = overzicht + "OMSCHRIJVING:"  + self.__omschrijving + "\n\n"

        overzicht = overzicht + "INGREDIËNTEN:\n"
        for item in self.__ingredient_list:
            overzicht = overzicht + str(item) + "\n"

        overzicht = overzicht + "\nBEREIDING:\n"
        teller = 1
        for stapje in self.__stappen:
            overzicht = overzicht + str(teller) + ". " + str(stapje) + "\n"
            teller = teller + 1
            
        return overzicht


    


