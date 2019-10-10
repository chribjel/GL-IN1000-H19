class Person:
    def __init__(self, nvn, ald, hde, vkt):
        self._navn = nvn
        self._alder = ald
        self._hoyde = hde
        self._vekt = vkt
        self._skrittTeller = 0

    
    def gaa(self, skritt):
        self._skrittTeller += skritt

    def skrivUtSkrittTeller(self):
        print(self._skrittTeller)