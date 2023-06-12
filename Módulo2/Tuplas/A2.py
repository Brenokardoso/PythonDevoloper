frutas = ("Abacaxi","Frutas","Melancia","Uva","Graviola","Uva","Pêra","Tangerina","Uva")
print(frutas)

letras = tuple("Python")
print(letras)

lista = tuple[(1,2,3,4)]
print(lista)

print(frutas[2])

print(letras[0::2])

for x,y in enumerate(frutas):
    print(f"{x}:{y}")

print(frutas.count("Uva"))

print(frutas.index("Melancia"))