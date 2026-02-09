class Ingredient:
    def __init__(self, naam: str, hoeveelheid: float, eenheid: str, kcal: str):
        self.__naam = naam
        self.__hoeveelheid = hoeveelheid
        self.__eenheid = eenheid
        self.__kcal = kcal
    def __str__(self):
        return f"- {self.__naam}, {self.__hoeveelheid}, {self.__eenheid}, {self.__kcal}"
    

    