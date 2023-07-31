class Passaro:
    def voar(self):
        print("Voando..\n")

class Pardal(Passaro):
    def voar(self):
        print(f"Pardal pode voar\n")

class Avestruz(Passaro):
    def voar(self):
        print("Avestruz não voa \n")

#FIXME:Exemplo ruim de uma herança para "ganhar" o método voar!

class Aviao(Passaro):
    def voar(self):
        print("Apertem os cintos,o avião já está decolando\n")
     
def plano_de_voo(obj):
    obj.voar()

p1 = Pardal()
p2 = Avestruz()
p3 = Aviao()


plano_de_voo(p1)
plano_de_voo(p2)
plano_de_voo(p3)

