from person import Person

def hovedprogram():
    ola = Person("ola", 20, 180, 70)
    skritt = 150

    ola.skrivUtSkrittTeller()
    ola.gaa(skritt)
    ola.skrivUtSkrittTeller()



hovedprogram()