import turtle

def print_list(l):
	print("la lista è:", end=" ")
	for element in l:
		print(element, end=" ")
		print("\n")

def main():
	lista = []
	lett = 'm'
	while lett != 'Z':
		lett = input("Una lettera: \nF = Avanti\nR = Destra\nL = Sinistra\n('Z' per inter.)\n")
		if lett != 'Z':
			lista.append(lett)

	finestra = turtle.Screen()
	command = turtle.Turtle()

	finestra.mainloop()

	for element in lista:
		if element == 'F':
			command.forward(100)
		elif element == 'R':
			command.right(90)
		elif element == 'L':
			command.left(90)

	

	##print_list(lista)

if __name__ == "__main__":
	main()