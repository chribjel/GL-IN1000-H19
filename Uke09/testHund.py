from hund import Hund

def hovedprogram():
    bikkje = Hund(2, 8)
    print("Vekt:", bikkje.hentVekt())
    for i in range(5):
        bikkje.spring()

    print("Løper fem runder")
    print("Vekt:", bikkje.hentVekt())
    bikkje.spis(8)
    print("Spiser en grov biff")
    print("Vekt:", bikkje.hentVekt())


hovedprogram()