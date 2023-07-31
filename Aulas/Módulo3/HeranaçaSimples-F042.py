class Veiculo:
    def  __init__(self,cor,placa,numero_de_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_de_rodas = numero_de_rodas
        print(f"{self.__class__.__name__}-->{','.join([f'{chave}:{valor}' for chave,valor in self.__dict__.items()])}")

    
    def __str__(self):
        return print(f"{self.__class__.__name__}:{','.join([f'{chave}:{valor}' for chave,valor in self.__dict__.items()])}")
    

    def ligar_motor(self):
        print("Ligando o motor...")
        return (print("O motor está ligado vrum vrum\n"))
    
    
    
    
class Motocicleta(Veiculo):
    pass

class Carro(Veiculo):
    pass

class Caminhão(Veiculo):
    def __init__(self, cor, placa, numero_de_rodas, carregado):
        super().__init__(cor,placa,numero_de_rodas)
        self.carregado = carregado
    
    def esta_carregado(self):
        if self.carregado == True:
            print(f"Eu estou carregado\n") 
        else:
            print("EU Não estou carregado\n")


# moto = Motocicleta("Amarela",4002-8922,4)
# print(moto)
# moto.ligar_motor()

# carro = Carro("Vermelho","BRN-8721",5)
# carro.ligar_motor()

caminhao = Caminhão("Roxo","CKR-2334",8,True)
caminhao.ligar_motor()
caminhao.esta_carregado()
