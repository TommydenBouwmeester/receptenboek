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
    
    
    

    # etc.. etc..
    # Succes!
