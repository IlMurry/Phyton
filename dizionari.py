def main():
	dizionario = {"nome": "Mario", "cognome": "Rossi"}
	#lista = ["mario", "rossi"]
	print(dizionario["nome"])

	#aggiunge 2 elementi nuovi
	dizionario["data nascita"] = "01/01/1990"
	dizionario["età"] = 123

	#sovrascrivere elemento con chiave "nome"
	dizionario["nome"] = "Luca"

	for chiave in dizionario:
		print(f,"chiave: {chiave} - valore: {dizionerio}")


	rubrica = {}

if __name__ == '__main__':
	main()