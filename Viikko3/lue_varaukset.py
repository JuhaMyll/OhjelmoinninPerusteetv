"""
Ohjelma joka lukee tiedostossa olevat varaustiedot
ja tulostaa ne konsoliin käyttäen funkitoita.
Alla esimerkkitulostus:

Varausnumero: 123
Varaaja: Anna Virtanen
Päivämäärä: 31.10.2025
Aloitusaika: 10.00
Tuntimäärä: 2
Tuntihinta: 19,95 €
Kokonaishinta: 39,9 €
Maksettu: Kyllä
Kohde: Kokoustila A
Puhelin: 0401234567
Sähköposti: anna.virtanen@example.com

"""
from datetime import datetime

def hae_varausnumero(varaus):
    numero = varaus[0]
    print(f"Varausnumero: {numero}")

def hae_varaaja(varaus):
    nimi = varaus[1]
    print(f"Varaaja: {nimi}")

    datetime.strptime(varaus[2],"%Y-%m-%d").date()    

def hae_paiva(varaus):
    paiva = varaus[2]
    print(f"Päivämäärä: {paiva}")

    datetime.strptime(varaus[3],"%H:%M").time()

def hae_aloitusaika(varaus):
    aika = varaus[3]
    print(f"Aloitusaika: {aika}")

def hae_tuntimaara(varaus):
    hMaara = float(varaus[4])
    print(f"Tuntimäärä: {hMaara}")

def hae_tuntihinta(varaus):
    hHinta = float(varaus[5])
    print(f"Tuntihinta: {hHinta} €")

def hae_maksettu(varaus):
    varaus[6] = "KYLLÄ" if varaus[6] else "EI"
    maksettu = varaus[6] 
    print(f"Maksettu: {maksettu}")

def hae_kohde(varaus):
    kohde = varaus[7]
    print(f"Kohde: {kohde}")

def hae_puhelin(varaus):
    puhelin = varaus[8]
    print(f"Puhelin: {puhelin}")

def hae_sahkoposti(varaus):
    sPosti = varaus[9]
    print(f"Sähköposti: {sPosti}")

def laske_kokonaishinta(varaus):
    kHinta = float(varaus[4])*float(varaus[5])
    print(f"Kokonaishinta: {kHinta} €")                       

def main():
    # Maaritellaan tiedoston nimi suoraan koodissa
    varaukset = "varaukset.txt"

    # Avataan tiedosto, luetaan ja splitataan sisalto
    with open(varaukset, "r", encoding="utf-8") as f:
        varaus = f.read().strip()
        varaus = varaus.split('|')

    # Toteuta loput funktio hae_varaaja(varaus) mukaisesti
    # Luotavat funktiota tekevat tietotyyppien muunnoksen
    # ja tulostavat esimerkkitulosteen mukaisesti

    hae_varausnumero(varaus)
    hae_varaaja(varaus)
    hae_paiva(varaus)
    hae_aloitusaika(varaus)
    hae_tuntimaara(varaus)
    hae_tuntihinta(varaus)
    laske_kokonaishinta(varaus)
    hae_maksettu(varaus)
    hae_kohde(varaus)
    hae_puhelin(varaus)
    hae_sahkoposti(varaus)

if __name__ == "__main__":
    main()