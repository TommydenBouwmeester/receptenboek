class Ingredient:
    def __init__(self, naam: str, hoeveelheid: float, eenheid: str, kcal: str):
        self.__naam = naam
        self.__hoeveelheid = hoeveelheid
        self.__eenheid = eenheid
        self.__kcal = kcal
        self.__plantaardig_alternatief= None


    def set_hoeveelheid(self, hoeveelheid: float):
        self.__hoeveelheid = hoeveelheid

    def get_hoeveelheid(self):
        return self.__hoeveelheid
    
    def get_kcal(self):
        return self.__kcal
    
    def get_naam(self):
        return self.__naam
    
    def get_eenheid(self):
        return self.__eenheid
    
    def set_plantaardig_alternatief(self, alternatief):
        self.__plantaardig_alternatief = alternatief
    
    def get_ingredient(self, plantaardig: bool):
        if plantaardig and self.__plantaardig_alternatief:
            return self.__plantaardig_alternatief
        return self

    def __str__(self):
        return f"- {self.__naam}, {self.__hoeveelheid} {self.__eenheid}, {self.__kcal} kcal"
    

    

    

    