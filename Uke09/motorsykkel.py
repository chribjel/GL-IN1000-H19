class Motorsykkel:
    def __init__(self, merke, regnr, kmstand):
        self._merke = merke
        self._regnr = regnr
        self._kmstand = kmstand

    def kjor(self, km):
        self._kmstand += km

    def hentKilometerstand(self):
        return self._kmstand

    def hentRegnr(self):
        return self._regnr

    def skrivUt(self):
        print()
        print("Merke:", self._merke)
        print("Registreringsnr:", self._regnr)
        print("Kilometerstand:", self._kmstand)
        print()

    def __eq__(self, motorsykkel):
        return self._regnr == motorsykkel.hentRegnr()

    def __str__(self):
        return f"Merke: {self._merke}\nRegistreringsnr: {self._regnr}\nKilometerstand: {self._kmstand}"
