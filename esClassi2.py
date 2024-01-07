import random

class Nemico():
	def __init__(self, pos_x, pos_y, n_vite):
		self.pos_x = pos_x
		self.pos_y = pos_y
		self.n_vite = n_vite

	def stampa(self):
		print(f"Nemico in posizione:  {self.pos_x}, {self.pos_y}, e ha {self.n_vite} vite")

def main():
	N_NEMICI = 5
	WIDTH = 888
	HEIGHT = 488
	lista_nemici = []

	for i in range(N_NEMICI):
		pos_x = random.randint(0, WIDTH-1)
		pos_y = random.randint(0, HEIGHT-1)

		nemico = Nemico(pos_x, pos_y, 5)

		lista_nemici.append(nemico)

	print(lista_nemici)

	personaggio = {"pos_x": 100, "pos_y": 200}
	for nemico in lista_nemici:
		nemico.stampa()
		if(nemico.pos_x == personaggio["pos_x"]) and (nemico.pos_y == personaggio["pos_y"]):
			print("COLLISIONE")

if __name__ == '__main__':
	main()