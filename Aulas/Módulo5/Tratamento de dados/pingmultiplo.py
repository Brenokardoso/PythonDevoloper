import os
import time

with open("Aulas/Módulo5/Tratamento de dados/hosts.txt") as file:
    dump = file.read()


for x in dump.split():
    os.system(f"ping -c 4 {x}") # No linux vc usa -c para numero de pacotes a ser serem enviados
    time.sleep(5) # da um tempo 