#Lag en klasse Bygning
#adresse
#huseier
#antall leietakere
#metoder flytte inn og ut
#endre huseier

class Bygning:
    def __init__(self, huseier, adresse):
        self._huseier = huseier
        self._adresse = adresse
        self._leietakere = 0
    
    def flyttInn(self, antLeietakere):
        self._leietakere += antLeietakere
    
    def flyttUt(self, antLeietakere):
        self._leietakere -= antLeietakere

    def endreHuseier(self, nyHuseier):
        self._huseier = nyHuseier

    def skrivUtInfo(self):
        print("Adresse: " + self._adresse +
            "\nHuseier: " + self._huseier +
            "\nLeietakere:", self._leietakere)
