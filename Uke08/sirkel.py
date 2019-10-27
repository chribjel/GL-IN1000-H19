
class Sirkel:
    def __init__(self, rad):
        self._radius = rad
        print(self.diameter())
        print(self.omkrets())
        print(self.areal())

    def diameter(self):
        return 2 * self._radius

    def omkrets(self):
        return 2 * 3.14 * self._radius

    def areal(self):
        return 3.14 * self._radius**2