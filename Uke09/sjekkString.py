hovedstring = "hei på deg"


def sjekkString(string):
    if string in hovedstring:
        return True
    return False


def sjekkString(string):
    stringListe = string.split()
    for ord in stringListe:
        if ord in hovedstring:
            return True
    return False
   