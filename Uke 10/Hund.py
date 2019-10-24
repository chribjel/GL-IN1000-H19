class Hund:
    def __init__(self, kjonn, navn, alder):
        self._kjonn = kjonn
        self._navn = navn
        self._alder = alder

    def __str__(self):
        return self._navn
    
    def hentHund(self):
        if self._kjonn == 0:
            return "Navn: " + self._navn + "\n" + "Alder: " + str(self._alder) + "\n" + "Kjønn: Gutt"
        
        else:
            return "Navn: " + self._navn + "\n" + "Alder: " + str(self._alder) + "\n" + "Kjønn: Jente"

    def hentKjonn(self):
        return self._kjonn