from Hund import Hund
from Kennel import Kennel

def hovedprogram():
    ny = Hund(1, "Kari", 10)
    print(ny)
    print()
    print(ny.hentHund())

    nyKennel = Kennel(5, 5)
    nyKennel.skrivHunder()

    for hund in nyKennel.finnNaboer(2, 2):
        print(hund)

hovedprogram()