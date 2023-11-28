


def feladat1(szam_lista):
    print("1. feladat")
    szamok_osszege: int = sum(szam_lista)
    atlag: int = szamok_osszege / len(szam_lista)

    return atlag

def feladat2(szam_lista):
    print("2. feladat")
    nagyobb: int = 0
    for i in szam_lista:
        if i > 50:
            nagyobb += 1
    
    return nagyobb

def feladat3(szam_lista):
    print("3. feladat")
    legnagyobb = max(szam_lista)

    return legnagyobb

def feladat5(szam_lista):
    print("5. feladat")
    legkisebb = min(szam_lista)

    return legkisebb

def feladat6(szam_lista):
    print("6. feladat")
    legkisebb = min(szam_lista)
    legnagyobb = max(szam_lista)

    kulonbseg = legnagyobb - legkisebb

    return kulonbseg

def feladat7(szam_lista):
    print("7. feladat")
    tipp_mix: int = int(input("Tippeljen egy számot: "))
    if tipp_mix in szam_lista:
        print(f"Az ön száma: {tipp_mix}, szerepel a számok között!")
    else:
        print(f"Az ön száma: {tipp_mix}, viszont ez nem szerepel a számok között!")