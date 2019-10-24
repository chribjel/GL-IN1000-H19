from random import randint
from Hund import Hund

class Kennel:
    def __init__(self, rad, kol):
        self._rader = rad
        self._kolonner = kol
        self._hundeliste = self.generer(rad, kol)

    def generer(self, rader, kol):
        navneliste = ["Abe","Ace", "Achillies","Agar", "Aiden", "AJax", 
            "Allegro", "Allie","Amazon", "Amigo","Anaconda", 
            "Andres","Android", "Angstrom", "Anise",
    	    "Aquarius", "Archie", "Argus","Artemis", "Ashes", "Aspen", 
            "Atlas", "August",
    	    "Avalon", "Armani"]
        
        max_alder = 15

        hundeliste = []

        for i in range(rader):
            hundeliste.append([])
            for j in range(kol):
                kjonn = randint(0, 1)
                navn = navneliste[randint(0, len(navneliste)-1)]
                alder = randint(0, max_alder)

                hundeliste[i].append(Hund(kjonn, navn, alder))
        return hundeliste

    def hentHund(self, rad, kol):
        return self._hundeliste[rad][kol]

    def skrivHunder(self):
        for i in range(len(self._hundeliste)):
            tekst = "Rad: " + str(i) + "  Hunder: "
            for j in range(len(self._hundeliste[i])):
                tekst += str(self.hentHund(i, j)) + " "
            print(tekst)
    
    def finnNaboer(self, rad, kol):
        naboliste = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                naboRad = rad + i
                naboKol = kol + j
                gyldig = True

                if naboRad == rad and naboKol == kol:
                    gyldig = False
                
                if naboRad >= self._rader or naboRad < 0:
                    gyldig = False

                if naboKol >= self._kolonner or naboKol < 0:
                    gyldig = False

                if gyldig:
                    naboliste.append(self.hentHund(naboRad, naboKol))
        
        return naboliste