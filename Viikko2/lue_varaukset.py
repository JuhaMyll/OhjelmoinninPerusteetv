"""
Ohjelma joka lukee tiedostossa olevat varaustiedot
ja tulostaa ne konsoliin. Alla esimerkkitulostus:

Varausnumero: 123
Varaaja: Anna Virtanen
Päivämäärä: 31.10.2025
Aloitusaika: 10.00
Tuntimäärä: 2
Tuntihinta: 19.95 €
Kokonaishinta: 39.9 €
Maksettu: Kyllä
Kohde: Kokoustila A
Puhelin: 0401234567
Sähköposti: anna.virtanen@example.com

"""

def main():
    # Määritellään tiedoston nimi suoraan koodissa
    varaukset = "varaukset.txt"

    # Avataan tiedosto ja luetaan sisältö
    with open(varaukset, "r", encoding="utf-8") as f:
        varaus = f.read().strip()

        #tietojen jako
        varausId = varaus.split('|')

        #päivämäärän tuonti
        from datetime import datetime

        #tietotyyppien määritys
        varausId[0] = int(varausId[0])
        varausId[1] = str(varausId[1])
        #muunnetaan päivämäärät ja kellonajat
        varausId[2] = datetime.strptime(varausId[2],"%Y-%m-%d").date()
        varausId[3] = datetime.strptime(varausId[3],"%H:%M").time()
        varausId[4] = int(varausId[4])
        varausId[5] = float(varausId[5])
        #lasketaan kokonaishinta
        varausId[6] = varausId[4]*varausId[5]
        #lisätään listaan
        varausId.insert(6, varausId[6])
        #IF/ELSE lauseke
        varausId[7] = "KYLLÄ" if varausId[7] else "EI"
        varausId[8] = str(varausId[8])
        varausId[9] = str(varausId[9])
        varausId[10] = str(varausId[10])

        #tehdään kopio ID listasta ja lisätään euron merkit tulosteeseen
        tuloste = varausId.copy()

        tuloste[5] = f"{tuloste[5]} €"
        tuloste[6] = f"{tuloste[6]} €"

        #otsikot
        otsikot = [
          "Varausnumero",
          "Varaaja",
          "Päivämäärä",
          "Aloitusaika",
          "Tuntimäärä",
          "Tuntihinta",
          "Kokonaishinta",
          "Maksettu",
          "Kohde",
          "Puhelin",
          "Sähköposti"  
        ]



        for otsikot, tuloste in zip(otsikot, tuloste):
            print(f"{otsikot}: {tuloste}")

    

if __name__ == "__main__":
    main()