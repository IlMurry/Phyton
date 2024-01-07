def main():
	file = open("Rubrica.txt", "r")
	righe = file.readlines()
	file.close()

	rubrica = {}

	for riga in righe:
		riga.split(", ")
		campi = riga.split(", ")
		numeroTelefonico = int(campi[1].replace("\n", ""))
		nome = campi[0]
		rubrica[numeroTelefonico] = nome

	print(rubrica)

if __name__ == '__main__':
	main()