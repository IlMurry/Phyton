def contoProteine(stringa):
	numA = len([a for a in stringa if a == 'A'])
	numT = len([t for t in stringa if t == 'T'])
	numG = len([g for g in stringa if g == 'G'])
	numC = len([c for c in stringa if c == 'C'])

	print(numA, numT, numG, numC)

def cercaSequenza(stringa):
	sequenza = "ATGTTTGTTTTT"

	for i,c in enumerate(stringa):
		stringa[i] = sequenza
		

		

def main():
	file = open("covid-19_gen1.txt", "r")
	righe = file.readlines()
	file.close()

	stringa = ""

	for riga in righe:
		stringa = stringa + riga[:-1]

	print(stringa)

	contoProteine(stringa)

	



if __name__ == '__main__':
	main()