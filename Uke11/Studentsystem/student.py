class Student:
	
    #10-2.1
	def __init__(self, navn):
		self._navn = navn
		self._fagliste = []
	
    #10-2.2
	def leggTilFag(self, fag):
		self._fagliste.append(fag)
	
    #10-2.3
	def hentAntallFag(self):
		return len(self._fagliste)
	
    #10-2.4
	def hentStudentNavn(self):
		return self._navn
	
    #10-2.5
	def skrivFagPaaStudent(self):
		print(self._navn)
		for fag in self._fagliste:
			print(fag.hentFagNavn())

	#11-gitt for oppgave 4.1
	def tarFag(self, fag):  #denne kan gjerne skrives paa en "enklere maate"
		return fag in self._fagliste

	#11- gitt for oppgave 7
	def fjernFag(self, fag):
		self._fagliste.remove(fag)