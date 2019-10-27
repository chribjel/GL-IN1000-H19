from motorsykkel import Motorsykkel

def hovedprogram():
    sykkel1 = Motorsykkel("Honda", "BS1234", 0)
    sykkel2 = Motorsykkel("Ducati", "BS4321", 0)
    sykkel3 = Motorsykkel("BMW", "BS6789", 0)

    sykkel1.skrivUt()
    sykkel2.skrivUt()
    sykkel3.skrivUt()

    sykkel3.kjor(10)

    print(sykkel3.hentKilometerstand())

hovedprogram()