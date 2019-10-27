from dyr import Dyr

def hovedprogram():
    bert = Dyr("hund", "M", 10)
    kari = Dyr("katt", "K", 5)
    knut = Dyr("papegoye", "M", 1)

    dyr = [bert, kari, knut]

    # dyr.append(Dyr("katt", "K", 4))

    print(bert)
    print(dyr)

    for dyrEks in dyr:
        print(dyrEks.hentArt(), dyrEks.hentKjonn(), dyrEks.hentVekt())


hovedprogram()