def main:
	address = input("inserisci l indirizzo ip")

	groups = address.split(".")

	groups = [int(x) for x in groups]

	print(groups)

if __name__ == '__main__':
	main()