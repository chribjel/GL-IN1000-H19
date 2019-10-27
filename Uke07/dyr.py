class Dyr:
    def __init__(self, art, kjonn, vekt):
        self._art = str(art)
        self._kjonn = kjonn
        self._vekt = int(vekt)

    def hentArt(self):
        return self._art

    def hentKjonn(self):
        return self._kjonn

    def hentVekt(self):
        return self._vekt

    #Alternativ
    def hentData(self):
        return [self._art, self._kjonn, self._vekt]