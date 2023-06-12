print(set(["a","b","c","d","e","b","e","a","d","f"]))

conjunto1 = {1,2,2,3,4}
conjunto2 = {3,4,5,5,6}

total_conjunto1 = conjunto1.union(conjunto2)
print(total_conjunto1)

total_conjunto2 = conjunto1.intersection(conjunto2)
print(total_conjunto2)

total_conjunto3 = conjunto1.difference(conjunto2)
print(total_conjunto3)

total_conjunto4 = conjunto1.symmetric_difference(total_conjunto2)
print(total_conjunto4)

conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

conjuntos1 = conjunto_a.issubset(conjunto_b)
print(conjuntos1)

conjuntos2 = conjunto_a.issuperset(conjunto_b)
print(conjunto2)

conjunto1.add("teste")
print(conjunto1)

conjunto1.discard("teste")
print(conjunto1)

numeros = {0,1,2,3,4,5,6,7,8,9,10}
print(2 not in numeros)