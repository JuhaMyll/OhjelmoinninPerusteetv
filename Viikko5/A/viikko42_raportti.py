# Copyright (c) 2025 Juha Myllyaho
#
# This code is licensed under the MIT License.
# You are free to use, modify, and distribute this code,
# provided that the original copyright notice is retained.
#
# See LICENSE file in the project root for full license information.

from datetime import datetime, date


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

def main():
    """
    Ohjelman pääfunktio: lukee datan, laskee yhteenvedot ja tulostaa raportin.
    """
    kulutusTuotantoDB = lue_data("viikko42.csv")
    print("\nViikon 42 sähkönkulutus ja -tuotanto (kWh, vaiheittain)", end="\n\n")
    print("Päivä\t\tPvm\t\tKulutus [kWh]\t\tTuotanto [kWh]")
    print("\t\t(pv.kk.vvvv)\tv1\tv2\tv3\tv1\tv2\tv3")
    print("---------------------------------------------------------------------------")
    

    
    viikonpaivat_fi = [
        "maanantai", "tiistai   ", "keskiviikko",
        "torstai    ", "perjantai", "lauantai", "sunnuntai"
    ]

    paivat = viikon_paivat(date(2025, 10, 13))  # Viikko 42 alkaa tästä

    for i, paiva in enumerate(paivat):
        print(f"{viikonpaivat_fi[i]}\t" + "\t".join(paivantiedot(paiva, kulutusTuotantoDB)))

if __name__ == "__main__":
    main()