# Copyright (c) 2025 Juha Myllyaho
#
# This code is licensed under the MIT License.
# You are free to use, modify, and distribute this code,
# provided that the original copyright notice is retained.
#
# See LICENSE file in the project root for full license information.

from datetime import datetime, date, timedelta


def muunna_tiedot(tietue: list) -> list:
    """
    Muuttaa jokaisen annetun tietorivin tietotyypit oikeiksi

    Parametrit:
     tietue: Sisältää 7 kenttää, joista ensimmäinen date -> loput int

    Palautus:
     Listan, jossa muutetut tietotyypit
    """
    return [
        datetime.fromisoformat(tietue[0]),
        int(tietue[1]),
        int(tietue[2]),
        int(tietue[3]),
        int(tietue[4]),
        int(tietue[5]),
        int(tietue[6]),
    ]


def lue_data(tiedoston_nimi: str) -> list:
    """
    Lukee CSV-tiedoston ja palauttaa rivit sopivassa rakenteessa ja tietotyypeissä.

    Kutsuu funktiota muunna_tiedot (lst):
     funktio palauttaa listan -> Tietotyypit muutettu

    Parametrit:
     tiedoston_nimi (str): ottaa vastaan tiedoston, jossa kentät jaettu merkillä ;

    Palautus:
     tietokanta (lst): palauttaa tietokannan, jossa tietotyypit on muutettu
    """
    tietokanta = []
    with open(tiedoston_nimi, "r", encoding="utf-8") as f:
        next(f)  # Otetaan kenttien esittelytiedot pois
        for tietue in f:
            tietue = tietue.split(";")
            tietokanta.append(muunna_tiedot(tietue))

    return tietokanta


def paivantiedot(paiva: date, tietokanta: list) -> list:
    """
    Laskee kulutus- ja tuotantotiedot vaiheittain ja palauttaa listan
    Laskettavat tiedot muutetaan Wh -> kWh

    Parametrit:
     paiva (date): Raportoitava päivä
     tietokanta (list): Kulutus- ja tuotantotiedot + päivämäärät

    Palautus:
     Listan, jossa tulostettavat merkkijonot
    """
    kulutus = [0, 0, 0]
    tuotanto = [0, 0, 0]
    for tietue in tietokanta:
        if tietue[0].date() == paiva:
            kulutus[0] += tietue[1] / 1000
            kulutus[1] += tietue[2] / 1000
            kulutus[2] += tietue[3] / 1000
            tuotanto[0] += tietue[4] / 1000
            tuotanto[1] += tietue[5] / 1000
            tuotanto[2] += tietue[6] / 1000

    return [
        f"{paiva.day}.{paiva.month}.{paiva.year}",
        f"{kulutus[0]:.2f}".replace(".", ","),
        f"{kulutus[1]:.2f}".replace(".", ","),
        f"{kulutus[2]:.2f}".replace(".", ","),
        f"{tuotanto[0]:.2f}".replace(".", ","),
        f"{tuotanto[1]:.2f}".replace(".", ","),
        f"{tuotanto[2]:.2f}".replace(".", ","),
    ]

    

def viikon_paivat(alku: date) -> list:
    """Palauttaa listan viikon (7 pv) päivämääristä alkaen annetusta päivästä."""
    return [alku.fromordinal(alku.toordinal() + i) for i in range(7)]

    
def viikkoraportti(viikkonumero: int, aloituspv: datetime.date, tietokanta: list) -> str:
    """
    Laskee viikkoraportin annettuihin viikonpäiviin ja

    Parametrit:
     viikkonumero (int): Raportoivan viikon numero
     aloituspv (datetime.date): Viikon ensimmäinen päivämäärä
     tietokanta (list): Kulutus- ja tuotantotiedot + päivämäärät

    Palautus:
     raportti (Str): Raportti tekstinä
    """

    viikonpaivat = [
        "maanantai",
        "tiistais",
        "keskiviikko",
        "torstai\t",
        "perjantai",
        "lauantain",
        "sunnuntai",
    ]

    raportti = f"\nViikon {viikkonumero} sähkönkulutus ja -tuotanto (kWh, vaiheittain)\n\n"
    raportti += "Viikonäivä\tPäivämäärä\tKulutus [kWh]\t\tTuotanto [kWh]\n"
    raportti += "\t\t\t\t\t\tv1\t\tv2\t\tv3\t\tv1\t\tv2\t\tv3\n"
    raportti += "----------------------------------------------------------------------------\n"
    for i, paiva in enumerate(viikonpaivat):
        raportti += paiva + "\t" + "\t".join(paivantiedot(aloituspv+timedelta(days=i), tietokanta)) + "\n"

    raportti += "----------------------------------------------------------------------------\n"
    return raportti


def main():
    """
    Ohjelman pääfunktio: lukee datan, laskee yhteenvedot ja tulostaa raportin.
    """
    v41 = lue_data("viikko41.csv")
    v42 = lue_data("viikko42.csv")
    v43 = lue_data("viikko43.csv")

    """
    Luodaan viikonpäivät
    """

    viikonpaivat_fi = [
        "Maanantai", "Tiistai   ", "Keskiviikko",
        "Torstai    ", "Perjantai", "Lauantai", "Sunnuntai"
    ]

    print("\nViikon 41 sähkönkulutus ja -tuotanto (kWh, vaiheittain)", end="\n\n")
    print("Päivä\t\tPvm\t\tKulutus [kWh]\t\tTuotanto [kWh]")
    print("\t\t(pv.kk.vvvv)\tv1\tv2\tv3\tv1\tv2\tv3")
    print("---------------------------------------------------------------------------")
    """
    Luodaan printti joka yhdistää viikonpäivän ja sen tiedot 
    """
    paivat = viikon_paivat(date(2025, 10, 6))
    for i, paiva in enumerate(paivat):
        print(f"{viikonpaivat_fi[i]}\t" + "\t".join(paivantiedot(paiva, v41)))

    print("\nViikon 42 sähkönkulutus ja -tuotanto (kWh, vaiheittain)", end="\n\n")
    print("Päivä\t\tPvm\t\tKulutus [kWh]\t\tTuotanto [kWh]")
    print("\t\t(pv.kk.vvvv)\tv1\tv2\tv3\tv1\tv2\tv3")
    print("---------------------------------------------------------------------------")
    
    paivat = viikon_paivat(date(2025, 10, 13))
    for i, paiva in enumerate(paivat):
        print(f"{viikonpaivat_fi[i]}\t" + "\t".join(paivantiedot(paiva, v42)))

    print("\nViikon 43 sähkönkulutus ja -tuotanto (kWh, vaiheittain)", end="\n\n")
    print("Päivä\t\tPvm\t\tKulutus [kWh]\t\tTuotanto [kWh]")
    print("\t\t(pv.kk.vvvv)\tv1\tv2\tv3\tv1\tv2\tv3")
    print("---------------------------------------------------------------------------")
    
    paivat = viikon_paivat(date(2025, 10, 20))
    for i, paiva in enumerate(paivat):
        print(f"{viikonpaivat_fi[i]}\t" + "\t".join(paivantiedot(paiva, v43)))

         # Luetaan data tiedostoista
    kulutusTuotantoViikko41 = lue_data("viikko41.csv")
    kulutusTuotantoViikko42 = lue_data("viikko42.csv")
    kulutusTuotantoViikko43 = lue_data("viikko43.csv")

    # Luodaan raportit
    raportti_viikko_41 = viikkoraportti(41, date(2025, 10, 6), kulutusTuotantoViikko41)
    raportti_viikko_42 = viikkoraportti(42, date(2025, 10, 13), kulutusTuotantoViikko42)
    raportti_viikko_43 = viikkoraportti(43, date(2025, 10, 20), kulutusTuotantoViikko43)

    # Kirjoitetaan raportit tiedostoon
    with open("yhteenveto.txt", "w", encoding="utf-8") as f:
        f.write(raportti_viikko_41)
        f.write(raportti_viikko_42)
        f.write(raportti_viikko_43)

    print("Raportti luotu")

    

if __name__ == "__main__":
    main()