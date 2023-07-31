class Pessoa:
    def __init__(self,nome = None,idade = None):
        self.idade = idade
        self.nome = nome

    # def __str__(self):
    #     return f"{self.__class__.__name__} : {', '.join(f'{chave}:{valor}'for chave,valor in self.__dict__.items())}"

    @classmethod
    def data_nascimento(cls,ano,mes,dia,nome):
        print(cls)
        # idade = 2023 - ano
        # return Pessoa(nome,idade)
    
    @staticmethod
    def maior_de_idade(idade):
        return idade >= 18

     


# p = Pessoa("Roberto Carlos",19)
# print(f"{p.nome}-{p.idade}")

p2 = Pessoa.data_nascimento(2002,6,4,"Breno")
# print(f"{p2.nome} - {p2.idade}")