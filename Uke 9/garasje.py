from motorsykkel import Motorsykkel

class Garasje:
    def __init__(self, etasjer, plassPrEtasje):
        self._garasje = [[] for i in range(etasjer)]
        self._plassPrEtasje = plassPrEtasje

    def parkerMotorsykkel(self, motorsykkel):
        for i in range(len(self._garasje)):
            # print(motorsykkel)  #Det var her jeg skjønte hva feilen var
            if len(self._garasje[i]) < self._plassPrEtasje:
                self._garasje[i].append(motorsykkel)

                #Måtte huske å gå ut av metoden når jeg hadde satt inn
                return
    
    def kjorUt(self, motorsykkel):
        for i in range(len(self._garasje)):
            for j in range(len(self._garasje[i])):
                if (motorsykkel == self._garasje[i][j]):
                    del self._garasje[i][j]

    def __str__(self):
        streng = ""
        for etasje in self._garasje:
            for motorsykkel in etasje:
                streng += motorsykkel.__str__() + " "
        return streng
