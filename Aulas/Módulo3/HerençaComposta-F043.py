class Animal:
    def __init__(self,numero_de_patas):
        self.numero_de_patas = numero_de_patas

    def __str__(self):
        return(f"{self.__class__.__name__} -> {','.join([f'{chave}:{valor}' for chave,valor in self.__dict__.items()])}") 



class Mamifero(Animal):
    def __init__(self,cor_do_pelo, **Kw):
        self.cor_do_pelo = cor_do_pelo
        super().__init__(**Kw)
        
    

class Ave(Animal):
    def __init__(self,cor_do_bico, **Kw):
        self.cor_do_bico = cor_do_bico
        super().__init__(**Kw)

class Cachorro(Mamifero):
    pass

class Gato(Mamifero):
    pass

class Leao(Mamifero):
    pass

class Ornitorrinco(Mamifero,Ave):
    def __init__(self, cor_do_bico, cor_do_pelo, numero_de_patas):
        print(Ornitorrinco.__mro__)
        super().__init__(cor_do_pelo = cor_do_pelo, cor_do_bico = cor_do_bico,numero_de_patas = numero_de_patas)

# gato = Gato(numero_de_patas = 4,cor_do_pelo ="Preto")
# print(gato)

ornitorrinco = Ornitorrinco(numero_de_patas =2,cor_do_pelo ="Azul marinho bebê",cor_do_bico ="Amarelo fusca 2003")
print(ornitorrinco)