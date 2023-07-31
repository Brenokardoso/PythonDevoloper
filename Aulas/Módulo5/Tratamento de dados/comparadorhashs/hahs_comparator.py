import hashlib

arquivo1 = '/home/brenoads/Área de Trabalho/Python Developer/Aulas/Módulo5/Tratamento de dados/comparadorhashs/txt1.txt'
arquivo2 = 'Aulas/Módulo5/Tratamento de dados/comparadorhashs/txt2.txt'

hash1 = hashlib.new("ripemd160") # define  o tipo de algoritimo que será usado pelo hash
hash2 = hashlib.new("ripemd160")

hash1.update(open(arquivo1, 'rb').read()) # qual dado será transmitido
hash2.update(open(arquivo2, 'rb').read()) # qual dado será transmitido 

if hash1.digest() == hash2.digest():
    print(f"O valor de hash1 = {hash1.digest()} \nO valor de hash2 = {hash2.digest()}")
else:
    print("N/C")