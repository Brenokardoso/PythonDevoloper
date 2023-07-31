from threading import Thread
from time import sleep

def carro(vel,plt):
    trajeto = 0
    while trajeto <= 100:
        print(f"Piloto : {plt} , Trajeto : {trajeto} ")
        trajeto += vel
        sleep(0.6)
    print("\n")

# def carro2(vel):
#     trajeto = 0
#     while trajeto <= 100:
#         print(f"Carro2 : {trajeto}")
#         trajeto += vel

# carro1(10)
# carro2(20)

t_carro1 = Thread(target = carro, args = [1,"Breno Kardoso"])
t_carro2 = Thread(target = carro, args = [3,"Roberto Carlos"])

t_carro1.start()
t_carro2.start()
