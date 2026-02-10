from recept import Recept 
from ingredient import Ingredient 
from stap import Stap


def main():
    recepten = []

    recept1 = Recept("Kip Kerrie", "Kip kerrie zonder pakjes en zakjes")
    kip = Ingredient("kip", 175,"gram", 280)
    vega_kip = Ingredient("vegatarische kipstukkies", 180, "gram", 45)
    kip.set_plantaardig_alternatief(vega_kip)
    recept1.voeg_ingredient_toe(kip)

    recept1.voeg_ingredient_toe(Ingredient("sperziebonen", 200, "gram", 60))

    recept1.voeg_stap_toe(Stap("Kook de rijst en zet een pan water met een snuf zout op het vuur voor de sperziebonen."))
    recept1.voeg_stap_toe(Stap("Snijd de kip in kleine blokjes, snipper het uitje, snijd de knoflook fijn en snijd de kontjes van de sperziebonen (was ze ook even)."))
    recepten.append(recept1)
    

    recept2 = Recept("Wraps met kip", "makkelijk zelf te maken")

    kip = Ingredient("kip", 125, "gram", 200)
    plantaardige_kipstukjes = Ingredient("Plantaardige kipstukjes", 125, "gram", 200)
    kip.set_plantaardig_alternatief(plantaardige_kipstukjes)
    recept2.voeg_ingredient_toe(kip)
    recept2.voeg_ingredient_toe(Ingredient("middelgrote tortilla's", 2, "stuks", 350))
    recept2.voeg_ingredient_toe(Ingredient("rode paprika", 1, "stuk", 30))
    recept2.voeg_ingredient_toe(Ingredient("maïs", 1, "blikje", 150))
    recept2.voeg_ingredient_toe(Ingredient("ui", 1, "stuk", 40))
    recept2.voeg_ingredient_toe(Ingredient("Mexicaanse kruidenmix", 1, "eetlepel",20))
    recept2.voeg_ingredient_toe(Ingredient("lente ui", 1, "stuk", 5))

    recept2.voeg_stap_toe(Stap("Hak de ui fijn en bak deze samen met de kip ongeveer 5 min. in een pan. Snijd ook de paprika in kleine blokjes en bak nog 5 min mee."))
    recept2.voeg_stap_toe(Stap("Voeg 2 eetlepels van de mexicaanse kruidenmix toe aan het kipmensel samen met 3 eetlepels water"))
    recept2.voeg_stap_toe(Stap("Laat de maïs uitlekken en warm nog even mee in de pan, verwarm intussen de wraps kort in een pan of in de oven"))
    recept2.voeg_stap_toe(Stap("Schep wat van de vulling op de wraps, bestrooi met wat ringetjes gehakte lente ui, rol op en steek vast met prikkers"))
    
    recepten.append(recept2)



    recept3 = Recept("Fusilli", "met groentesaus en hamblokjes")
    recept3.voeg_ingredient_toe(Ingredient("fusilli", 75, "gram", 265))
    recept3.voeg_ingredient_toe(Ingredient("traditionele olijfolie", 1/4, "el",30))
    recept3.voeg_ingredient_toe(Ingredient("macaroni-spaghettigroente", 112.5, "gram",35))
    recept3.voeg_ingredient_toe(Ingredient("hamblokjes", 62.5, "gram", 75))
    recept3.voeg_ingredient_toe(Ingredient("AH BASIC pastasaus basillicum", 130, "gram",65))
    recept3.voeg_ingredient_toe(Ingredient("grana padano 32+", 12.5, "gram", 50))

    recept3.voeg_stap_toe(Stap("Kook de fusilli beetgaar volgens de aanwijzingen op de verpakking. Verhit ondertussen de olijfolie in een hapjespan en bak de groenten 5 min. op middelhoog vuur.", "water in de pan is handig habibi"))
    recept3.voeg_stap_toe(Stap("Voeg de hamblokjes toe en bak 1 min. mee. Schenk de pastasaus bij het groente-hammengsel en warm 2 min. goed door."))
    recept3.voeg_stap_toe(Stap("Giet de pasta af en meng door de saus. Rasp er de Grana Padano over en serveer."))
    
    recepten.append(recept3)


    print("Beschikbare recepten")

    teller = 1
    for recept in recepten:
        print(str(teller) + ". " + recept.get_naam())
        teller = teller + 1
    

    try:
        keuze = int(input("Welk recept wilt u bekijken? "))
        gekozen_recept = recepten[keuze - 1]
    except ValueError:
        print("foutief of niet bestaand recept geselecteerd")
        
    
    try:

        aantal = int(input("Wat is het aantal personen? "))
        gekozen_recept.set_aantal_personen(aantal)
    except ValueError:
        print("Foutieve invoer")

    plantaardig = input("Wilt u de plantaardige versie? (ja/nee): ").lower()
    if plantaardig == "ja":
        print(gekozen_recept.get_plantaardig_recept(True))
    else:
        print(gekozen_recept)


if __name__ == "__main__":
    main()
