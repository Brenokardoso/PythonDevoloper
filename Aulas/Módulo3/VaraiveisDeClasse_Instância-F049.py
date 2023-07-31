class Escola:
    escola = " School DIO"

    def __init__(self,nome,numero):
        self.nome = nome 
        self.numero = numero

    def __str__(self):
        return f"{self.nome} - {self.numero} - {self.escola}"
    
def mostrarobj(*objs):
    for obj in objs:
        print(obj)

def mostar_normal(arg):
    for a in arg:
        print(a)

Br = Escola("Breno",32323)
Gi = Escola("Gi",12121)
Hg = Escola("Higor",23321)
lista = [Br,Hg,Gi]

mostrarobj(Br,Gi,Hg)
mostar_normal(lista)