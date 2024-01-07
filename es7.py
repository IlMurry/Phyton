def main():
	num = int(input("inserisci un numero"))
	div = 0

	if (num%2 == 0):
		print("divisibile per 2")
		div = 1
	elif (num%3 == 0):
		print("divisibile per 3")
		div = 1
	elif (num%5 == 0):
		print("divisibile per 5")
		div = 1
	else:
		print("non divisibile per 2 3 e 5")

if __name__ == '__main__':
	main()