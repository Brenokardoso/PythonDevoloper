from abc import ABC,abstractmethod

class ControleRemoto(ABC):

    @abstractmethod
    def ligar(self):
        print(f"Está ligado\n")

    @abstractmethod
    def desligar(self):
        print(f"Está desligado\n")

class ControleTv(ControleRemoto):
    def ligar(self):
        print("A TV está ligada\n")

    def desligar(self):
        print("A Tv está desligada\n")


controle = ControleTv()
controle.ligar()
controle.desligar()
