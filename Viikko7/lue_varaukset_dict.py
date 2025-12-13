# Copyright (c) 2025 Juha Myllyaho
#
# This code is licensed under the MIT License.
# You are free to use, modify, and distribute this code,
# provided that the original copyright notice is retained.
#
# See LICENSE file in the project root for full license information.

from datetime import datetime

def muunna_varaustiedot(varaus: list) -> dict:
    return {
        "varausId": int(varaus[0]),
        "nimi": varaus[1],
        "sähköposti": varaus[2],
        "puhelin": varaus[3],
        "varauksenPvm": datetime.strptime(varaus[4], "%Y-%m-%d").date(),
        "varauksenKlo": datetime.strptime(varaus[5], "%H:%M").time(),
        "varauksenKesto": int(varaus[6]),
        "hinta": float(varaus[7]),
        "varausVahvistettu": varaus[8].lower() == "true",
        "varattuTila": varaus[9],
        "varausLuotu": datetime.strptime(varaus[10], "%Y-%m-%d %H:%M:%S")
    }

def hae_varaukset(varaustiedosto: str) -> list[dict]:
    varaukset = []

    with open(varaustiedosto, "r", encoding="utf-8") as f:
        for rivi in f:
            rivi = rivi.strip()
            varaustiedot = rivi.split('|')
            varaukset.append(muunna_varaustiedot(varaustiedot))

    return varaukset

def vahvistetut_varaukset(varaukset: list[dict]):
    for v in varaukset:
        if v["varausVahvistettu"]:
            print(
                f"- {v['nimi']}, {v['varattuTila']}, "
                f"{v['varauksenPvm'].strftime('%d.%m.%Y')} "
                f"klo {v['varauksenKlo'].strftime('%H.%M')}"
            )
    print()

def pitkat_varaukset(varaukset: list[dict]):
    for v in varaukset:
        if v["varauksenKesto"] >= 3:
            print(
                f"- {v['nimi']}, "
                f"{v['varauksenPvm'].strftime('%d.%m.%Y')} "
                f"klo {v['varauksenKlo'].strftime('%H.%M')}, "
                f"kesto {v['varauksenKesto']} h, {v['varattuTila']}"
            )
    print()

def varausten_vahvistusstatus(varaukset: list[dict]):
    for v in varaukset:
        status = "Vahvistettu" if v["varausVahvistettu"] else "EI vahvistettu"
        print(f"{v['nimi']} → {status}")
    print()

def varausten_lkm(varaukset: list[dict]):
    vahvistetut = sum(1 for v in varaukset if v["varausVahvistettu"])
    ei_vahvistetut = len(varaukset) - vahvistetut

    print(f"- Vahvistettuja varauksia: {vahvistetut} kpl")
    print(f"- Ei-vahvistettuja varauksia: {ei_vahvistetut} kpl")
    print()

def varausten_kokonaistulot(varaukset: list[dict]):
    tulot = sum(
        v["varauksenKesto"] * v["hinta"]
        for v in varaukset
        if v["varausVahvistettu"]
    )

    print(
        "Vahvistettujen varausten kokonaistulot:",
        f"{tulot:.2f}".replace('.', ','),
        "€"
    )
    print()

def main(): 
    varaukset = hae_varaukset("varaukset.txt")

    print("1) Vahvistetut varaukset")
    vahvistetut_varaukset(varaukset)

    print("2) Pitkät varaukset (≥ 3 h)")
    pitkat_varaukset(varaukset)

    print("3) Varausten vahvistusstatus")
    varausten_vahvistusstatus(varaukset)

    print("4) Yhteenveto vahvistuksista")
    varausten_lkm(varaukset)

    print("5) Vahvistettujen varausten kokonaistulot")
    varausten_kokonaistulot(varaukset)


if __name__ == "__main__":
    main()
