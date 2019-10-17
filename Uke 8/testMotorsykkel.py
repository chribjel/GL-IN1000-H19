from motorsykkel import Motorsykkel
from garasje import Garasje

def hovedprogram():
    sykkel1 = Motorsykkel("Honda", "BS1234", 0)
    sykkel2 = Motorsykkel("Ducati", "BS4321", 0)
    sykkel3 = Motorsykkel("BMW", "BS6789", 0)
    sykkel4 = Motorsykkel("Honda", "BS6729", 0)

    garasje = Garasje(3, 1)

    garasje.parkerMotorsykkel(sykkel1)
    garasje.parkerMotorsykkel(sykkel2)
    garasje.parkerMotorsykkel(sykkel3)
    garasje.parkerMotorsykkel(sykkel4)



    print(garasje)

hovedprogram()