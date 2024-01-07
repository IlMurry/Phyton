dizionario = {"a":"albero", "b":"brutto", "c":"casa"} #crea dizionario

print(dizionario["b"]) #stampa elemento in chiave b

dizionario["d"] = "dado" #aggiunge elemento

dizionario["a"] = "alto" #sovrascrive elemento

for chiave in dizionario:											#stampa chiave
	print(f"la chiave: {chiave}")

for chiave in dizionario:											#stampa valore
	print(f"ha valore {dizionario[chiave]}")

for chiave in dizionario:											#stampa chiave e dizionario
	print(f"la chiave: {chiave} ha valore {dizionario[chiave]}")

if "a" in dizionario:						#controlla se la chiave è presente nel dizionario
	print("è presente a nel dizionario")



