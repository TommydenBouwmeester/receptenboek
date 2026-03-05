class Stap:
    def __init__(self, beschrijving = str, tip: str = None):
        self.__beschrijving = beschrijving
        self.__tip = tip

    def set(self, tip):
        self.__tip = tip

    def __str__(self):
        overzicht = self.__beschrijving
        if self.__tip:
            overzicht = overzicht + f"\nTIP: {self.__tip}"
        return overzicht 
    

