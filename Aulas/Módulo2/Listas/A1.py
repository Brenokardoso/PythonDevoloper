lista1 = ["Laranja","Abacaxi","pera"]
print(lista1[-1])

matrix = [1,2,3],[4,5,6],[7,8,9]
print(matrix[1][-2])

lista2 = ["p","y","t","h","o","n"]
print(lista2[2:])

carros = ["Marea","pajeiro","Chevet","Lancer"] 
for x in carros:
    print(x)

for indice,carro in enumerate(carros):
    print(f"{indice}:{carro}")

lista3 = ["A","B","C","D","E","F"]
lista_comp = []
for x in lista3:
    if "A" in x:
        lista_comp.append(x)
print(f"{lista_comp}")

lista_comp.clear()
print(f"{lista_comp}")

lista4 = []
lista3.copy()
print(f"{lista3}")
