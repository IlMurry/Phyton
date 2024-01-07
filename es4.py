def main():
	a = float(input("inserisci un numero: "))
	b = float(input("inserisci un numero: "))
	c = 0.0

	if (a < b):
		a, b = b, a

	print(f"i numeri in ordine decrescente sono {a} e {b}")

if __name__ == '__main__':
	main()