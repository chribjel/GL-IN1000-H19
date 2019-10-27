class Hund:

    def __init__(self, alder, vekt):
        self._alder = alder
        self._vekt = vekt
        self._metthet = 10

    def hentAlder(self):
        return self._alder

    def hentVekt(self):
        return self._vekt

    def spring(self):
        if self._metthet < 5:
            self._metthet -= 1
            self._vekt -= 1
        else:
            self._metthet -= 2

    def spis(self, heltall):
        self._metthet += heltall
        if self._metthet > 7:
            self._vekt += 1