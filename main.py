from recept import Recept 
from ingredient import Ingredient 
from stap import Stap
from reportlab.pdfgen import canvas
from reportlab.lib import colors


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
    hamblokjes = Ingredient("hamblokjes", 62.5, "gram", 75)
    vegatarische_hamblokjes = Ingredient("GoodBite hamblokjes (plantaardig)",62.5, "gram", 75)
    hamblokjes.set_plantaardig_alternatief(vegatarische_hamblokjes)
    recept3.voeg_ingredient_toe(hamblokjes)
    recept3.voeg_ingredient_toe(Ingredient("fusilli", 75, "gram", 265))
    recept3.voeg_ingredient_toe(Ingredient("traditionele olijfolie", 1/4, "el",30))
    recept3.voeg_ingredient_toe(Ingredient("macaroni-spaghettigroente", 112.5, "gram",35))
    recept3.voeg_ingredient_toe(Ingredient("AH BASIC pastasaus basillicum", 130, "gram",65))
    recept3.voeg_ingredient_toe(Ingredient("grana padano 32+", 12.5, "gram", 50))
    recept3.voeg_stap_toe(Stap("Kook de fusilli beetgaar volgens de aanwijzingen op de verpakking. Verhit ondertussen de olijfolie in een hapjespan en bak de groenten 5 min. op middelhoog vuur."))
    recept3.voeg_stap_toe(Stap("Voeg de hamblokjes toe en bak 1 min. mee. Schenk de pastasaus bij het groente-hammengsel en warm 2 min. goed door."))
    recept3.voeg_stap_toe(Stap("Giet de pasta af en meng door de saus. Rasp er de Grana Padano over en serveer."))
    recepten.append(recept3)

    return recepten

def tonen_keuzemenu():
    recepten = main()
    while True:
        keuzemenu = input("Toevoegen of tonen overzicht of exit?: ").lower()
        if keuzemenu == "tonen":
            tonen_recepten(recepten)

        elif keuzemenu == "toevoegen":
            voeg_recept_toe(recepten)

        elif keuzemenu == "exit":
            print("Programma sluit")
            break

        else:
            print("Foutieve invoer. Kies toevoegen, tonen of exit")

def tonen_recepten(recepten):
    print("Beschikbare recepten")
    teller = 1
    for recept in recepten:
        print(str(teller) + ". " + recept.get_naam())
        teller = teller + 1

    while True:
        try:
            keuze = int(input("Welk recept wilt u bekijken? "))
            if keuze <= 0:
                print("Recept niet gevonden")
                continue
            gekozen_recept = recepten[keuze - 1]
            break
        except (IndexError, ValueError):
            print("Recept niet gevonden")

    while True:
        try:
            aantal = int(input("Wat is het aantal personen? "))
            if aantal <= 0:
                print("Foutieve invoer")
                continue
            gekozen_recept.set_aantal_personen(aantal)
            break
        except ValueError:
            print("Foutieve invoer")


    while True:
        plantaardig = input("Wilt u de plantaardige versie? (ja/nee): ").lower()
        if plantaardig == "ja":
            print(gekozen_recept.get_plantaardig_recept(True))
            while True:
                pdf_vraag = input("Wilt u dit recept opslaan als PDF? (ja/nee): ").lower()
                if pdf_vraag == "ja":
                    exporteer_naar_pdf(gekozen_recept, True)
                    break
                elif pdf_vraag == "nee":
                    break
                else:
                    print("Foutieve invoer")

            while True:
                keuzemenu = input("Wilt u het recepten verwijderen of terug naar home? ").lower()
                if keuzemenu == "verwijderen":
                    recepten.pop(keuze -1)
                    break
                elif keuzemenu == "terug":
                    break
                else:
                    print("Foutieve invoer")
            break

        elif plantaardig == "nee":
            print(gekozen_recept)
            while True:
                pdf_vraag = input("Wilt u dit recept opslaan als PDF? (ja/nee): ").lower()
                if pdf_vraag == "ja":
                    exporteer_naar_pdf(gekozen_recept, False)
                    break
                elif pdf_vraag == "nee":
                    break
                else:
                    print("Foutieve invoer")
            while True:
                keuzemenu = input("Wilt u het recepten verwijderen of terug naar home? ").lower()
                if keuzemenu == "verwijderen":
                    recepten.pop(keuze -1)
                    break
                elif keuzemenu == "terug":
                    break
                else:
                    print("Foutieve invoer")
            break
        else:
            print("Foutieve invoer")

def voeg_recept_toe(recepten):
    naam = input("Naam van het recept: ")
    omschrijving = input("Omschrijving van het recept: ")
    nieuw_recept = Recept(naam, omschrijving)
    print("\nIngrediënten toevoegen of typ klaar om te stoppen")
    while True:
        try:
            naam_ingrediënt = input("Naam van het ingrediënt: ").lower()
            hoeveelheid_ingrediënt = float(input("Wat is de hoeveelheid? "))
            eenheid_ingrediënt = input("Wat is de eenheid? ")
            kcal_ingrediënt = float(input("Hoeveel caloriën bevat dit ingrediënt? "))
            ingrediënt = Ingredient(naam_ingrediënt, hoeveelheid_ingrediënt, eenheid_ingrediënt, kcal_ingrediënt)

            plantaardig_vraag = input("Is een plantaardig alternatief gewenst? (ja/nee): ")
            if plantaardig_vraag == "ja":
                plantaardig_naam = input("Naam van het ingrediënt: ").lower()
                plantaardig_hoeveelheid = float(input("Wat is de hoeveelheid? "))
                plantaardig_eenheid = input("Wat is de eenheid? ")
                plantaardig_kcal = float(input("Hoeveel caloriën bevaat dit plantaardig alternatief? "))
                plantaardig_ingrediënt = Ingredient(plantaardig_naam, plantaardig_hoeveelheid, plantaardig_eenheid, plantaardig_kcal)
                ingrediënt.set_plantaardig_alternatief(plantaardig_ingrediënt)

            nieuw_recept.voeg_ingredient_toe(ingrediënt)

            nieuw_ingrediënt = input("Wil je nog een ingrediënt toevoegen? ").lower()
            if nieuw_ingrediënt == "nee":
                break
        except ValueError:
                print("Foutieve invoer")

    while True:
        stap_tekst = input("Beschrijf de bereidingsstap: ")
        nieuwe_stap = Stap(stap_tekst)

        tip_vraag = input("Wilt u een tip toevoegen aan deze stap? (ja/nee): ").lower()
        if tip_vraag == "ja":
            tip_inhoud = input("Voer de tip in: ")
            nieuwe_stap.set(tip_inhoud) 

        nieuw_recept.voeg_stap_toe(nieuwe_stap)

        nog_stap = input("Nog een stap toevoegen? (ja/nee): ").lower()
        if nog_stap == "nee":
            break

    recepten.append(nieuw_recept)
    print("Recept is toegevoegd aan het overzicht!")
    print(nieuw_recept)

def exporteer_naar_pdf(gekozen_recept, plantaardige_keuze):
    bestandsnaam = gekozen_recept.get_naam()
    if plantaardige_keuze:
        bestandsnaam = bestandsnaam + "_plantaardig.pdf"
    bestandsnaam = bestandsnaam + ".pdf"
    pdf = canvas.Canvas(bestandsnaam)
    pdf.setTitle(gekozen_recept.get_naam())
    pdf.setFont("Helvetica-Bold", 24)
    pdf.drawCentredString(300, 770, gekozen_recept.get_naam())
    pdf.line(30, 750, 550, 750)
    tekst = pdf.beginText(40, 720)
    tekst.setFont("Helvetica", 12)
    tekst.setFillColor(colors.black)
    tekst_inhoud = gekozen_recept.get_plantaardig_recept(plantaardige_keuze)
    regels = tekst_inhoud.split('\n')

    for regel in regels:
        while len(regel) > 90:
            tekst.textLine(regel[:90])
            regel = "  " + regel[90:]  
        tekst.textLine(regel)

    pdf.drawText(tekst)
    pdf.save()
    print(f"PDF {bestandsnaam} is klaar!")

if __name__ == "__main__":
    tonen_keuzemenu()
