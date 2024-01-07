def print_list(l):
	print("la lista è:", end=" ")
	for element in l:
		print(element, end=" ")
		print("\n")

def main():
	lista = []
	num = 1
	while num>0:
		num = int(input("Un numero: (-1 per inter.)"))
		if num>0:
			lista.append(num)

	print_list(lista)

if __name__ == "__main__":
	main()