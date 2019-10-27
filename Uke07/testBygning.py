from bygning import Bygning

def hovedprogram():
    hus = Bygning("Lars", "Adressegate 14")
    hus.skrivUtInfo()

    hus.flyttInn(3)
    hus.endreHuseier("Kari")

    hus.skrivUtInfo()

hovedprogram()
