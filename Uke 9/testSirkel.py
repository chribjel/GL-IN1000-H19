from sirkel import Sirkel

def hovedprogram():
    runding = Sirkel(5)

    assert runding.diameter() == 10
    print(runding.diameter())

    print(runding.omkrets())

    print(runding.areal())

hovedprogram()