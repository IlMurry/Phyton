def main():
	sub = int(input("inserisci un cdc per la subnet senza usare '/' (es. 24) "))

	if (sub < 1 or sub > 31):
		print("numero inserito non valido")
	else:
		binario = sub * '1' + '0' * (32 - sub)
		group1 = int(binario[0:8],2)
		group2 = int(binario[8:16],2)
		group3 = int(binario[16:24],2)
		group4 = int(binario[24:],2)

		lista = [group1, group2, group3, group4]
		lista = [str(elemento) for elemento in lista]
		print(".".join(lista))

if __name__ == '__main__':
	main()