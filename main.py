from recept import Recept 
from ingredient import Ingredient 
from stap import Stap


def main():
    recepten = []

    recept1 = Recept("Kip Kerrie", "Kip kerrie zonder pakjes en zakjes")
    recept1.voeg_ingredient_toe(Ingredient("kip", 500, "gram"))
    recept1.voeg_ingredient_toe(Ingredient("sperziebonen", 400, "gram"))

    recept1.voeg_stap_toe(Stap("Kook de rijst en zet een pan water met een snuf zout op het vuur voor de sperziebonen."))
    recept1.voeg_stap_toe(Stap("Snijd de kip in kleine blokjes, snipper het uitje, snijd de knoflook fijn en snijd de kontjes van de sperziebonen (was ze ook even)."))

    recepten.append(recept1)
    print(recept1)

    recept2 = Recept("Wraps met kip", "makkelijk zelf te maken")
    recept2.voeg_ingredient_toe(Ingredient("middelgrote tortilla's", 8, "stuks"))
    recept2.voeg_ingredient_toe(Ingredient("rode paprika", 2, "stuks"))
    recept2.voeg_ingredient_toe(Ingredient("maïs", 1, "blikje"))
    recept2.voeg_ingredient_toe(Ingredient("kip", 500, "gram"))
    recept2.voeg_ingredient_toe(Ingredient("ui", 1, "stuk"))
    recept2.voeg_ingredient_toe(Ingredient("Mexicaanse kruidenmix", 2, "eetlepels"))
    recept2.voeg_ingredient_toe(Ingredient("lente uien", 2, "stuks"))

    recept2.voeg_stap_toe(Stap("Hak de ui fijn en bak deze samen met de kip ongeveer 5 min. in een pan. Snijd ook de paprika in kleine blokjes en bak nog 5 min mee."))
    recept2.voeg_stap_toe(Stap("Voeg 2 eetlepels van de mexicaanse kruidenmix toe aan het kipmensel samen met 3 eetlepels water"))
    recept2.voeg_stap_toe(Stap("Laat de maïs uitlekken en warm nog even mee in de pan, verwarm intussen de wraps kort in een pan of in de oven"))
    recept2.voeg_stap_toe(Stap("Schep wat van de vulling op de wraps, bestrooi met wat ringetjes gehakte lente ui, rol op en steek vast met prikkers"))
    print(recept2)

    recept3 = Recept("Fusilli", "met groentesaus en hamblokjes")
    recept3.voeg_ingredient_toe(Ingredient("fusilli", 300, "gram"))
    recept3.voeg_ingredient_toe(Ingredient("traditionele olijfolie", 1, "el"))
    recept3.voeg_ingredient_toe(Ingredient("macaroni-spaghettigroente", 450, "gram"))
    recept3.voeg_ingredient_toe(Ingredient("hamblokjes", 250, "gram"))
    recept3.voeg_ingredient_toe(Ingredient("AH BASIC pastasaus basillicum", 520, "gram"))
    recept3.voeg_ingredient_toe(Ingredient("grana padano 32+", 50, "gram"))

    recept3.voeg_stap_toe(Stap("Kook de fusilli beetgaar volgens de aanwijzingen op de verpakking. Verhit ondertussen de olijfolie in een hapjespan en bak de groenten 5 min. op middelhoog vuur."))
    recept3.voeg_stap_toe(Stap("Voeg de hamblokjes toe en bak 1 min. mee. Schenk de pastasaus bij het groente-hammengsel en warm 2 min. goed door."))
    recept3.voeg_stap_toe(Stap("Giet de pasta af en meng door de saus. Rasp er de Grana Padano over en serveer."))
    print(recept3)


    # enz.. enz..
    # Veel succes!

if __name__ == "__main__":
    main()
