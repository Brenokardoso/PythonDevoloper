import datetime
class Pessoa:
    def __init__(self,nome,ano_do_nascimento):
        self._nome = nome
        self._ano_do_nascimento = ano_do_nascimento
    
    @property
    def nome(self):
        return (self._nome)
    
    @property
    def idade(self):
        self._ano_do_nascimento = int(self._ano_do_nascimento)
        return 2023 - self._ano_do_nascimento
    


pessoa = Pessoa("Breno",2002)

print(f"Nome:{pessoa.nome}\v Idade:{pessoa.idade}")

