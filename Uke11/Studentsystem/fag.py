class Fag:
	
    #10-1.1
	def __init__(self, fagnavn):
		self._navn = fagnavn
		self._studentliste = []
	
    #10-1.2
	def leggTilStudent(self, student):
		self._studentliste.append(student)
	
    #10-1.3
	def hentAntallStudenter(self):
		return len(self._studentliste)
	
    #10-1.4
	def hentFagNavn(self):
		return self._navn
	
    #10-1.5
	def skrivStudenterVedFag(self):
		print(self._navn)
		for student in self._studentliste:
			print(student.hentStudentNavn())

	#gitt for oppgave 7
	def fjernStudent(self, student):
		self._studentliste.remove(student)