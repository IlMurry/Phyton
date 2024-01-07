
def push(pila, element):
	pila.append(element)

def pop(pila):
	x = pila.pop()
	return x

def main():
	parentesi_aperte = ["(", "[", "{"]
	stringa = "{1+[2+3]*5}"
	pila = []
	for carattere in stringa:
		if carattere in parentesi_aperte:
			push(pila, carattere)
		if carattere in parentesi_chiuse:
			parentesi = pop(pila)
			if dizionario[parentesi]!=carattere:
print(pila)