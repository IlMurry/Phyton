import turtle

def nord(bussola, movimento):
	bussola.forward(movimento)

def est(bussola, movimento):
	bussola.right(90)
	bussola.forward(movimento)
	bussola.left(90)

def ovest(bussola, movimento):
	bussola.left(90)
	bussola.forward(movimento)
	bussola.right(90)

def sud(bussola, movimento):
	bussola.left(180)
	bussola.forward(movimento)
	bussola.right(180)

def kill(bussola, movimento):
	exit(0)

def main():
	finestra = turtle.Screen()
	bussola = turtle.Turtle()
	bussola.left(90)
	dizionario = {"n": nord, "s": sud, "o": ovest, "e": est, "x": exit}
	while True:
		direzione = input("Inserisci n per nord, s per sud, o per ovest, e per est, x per uscire: ")
		movimento = int(input("Inserisci la lunghezza del movimento: "))
		if direzione in dizionario:
			dizionario[direzione](bussola, movimento)
		else:
			print("Errore")
			break	
	finestra.mainloop()

if __name__ == '__main__':
	main()