pessoa1 = {"Nome":"Breno","idade":28}
print(pessoa1)
print(type(pessoa1))

pessoa2 = dict(nome = "Breno Kardoso",idade = 33,sexo = "M")
print(pessoa2)
print(type(pessoa2))

dados = dict(name = "Frederic Engels",age = 72 ,weight = 92,sexo = "Masculino",cabelo = "crespo",ninja = "não")
dados_2 = {"name":"Algo","Idade" : 22, "tempo" : "muito pouco"}

pessoa1["Nome"] = "Roberto Carlos"
pessoa1["idade"] = 33

print(pessoa1)
print(dados)
print(dados_2)

A = {"teste" : "testado"}
B = dict(teste = "testado")
print(A,B)

dicionario = {"brenopositivo@hotmail.com":{"Nome" : "Breno Kardoso","Idade" : 28,"Tempo":"O Suficiente"}}
print(dicionario)

dicionario["brenopositivo@hotmail.com"]["Nome"] = "James Carron Bacster"
print(dicionario)

for d in dados:
    print(f"{d}:{dados[d]}")

dicionario.clear()
print(dicionario)

print(dict.fromkeys("name"))

#usando uma lista de tuplas para cirar um dicionário:

lista_tuplas = [("nome","Breno"),("idade", 19),("sexo","masculino")]
lista_dicionario = dict(lista_tuplas)
print(lista_dicionario)

#Acabou

#dicionario.get["contatos",84227774] TODO:Observar a função get com mais cuidado masi tarde na resolução de execercicios

dicionario.items()

dicionario.update({"brenopositivo@hotmail.com":{"Nome" :"NOVONOVONOVO","Idade" : 11111,"Tempo":"Pouco dms"}})
print(dicionario)