class Motorsykkel:
    def __init__(self, merke, regnr, kmstand):
        self._merke = merke
        self._regnr = regnr
        self._kmstand = kmstand

    def kjor(self, km):
        self._kmstand += km

    def hentKilometerstand(self):
        return self._kmstand

    def skrivUt(self):
        print()
        print("Merke:", self._merke)
        print("Registreringsnr:", self._regnr)
        print("Kilometerstand:", self._kmstand)
        print()
