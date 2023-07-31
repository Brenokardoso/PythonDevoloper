class bike:
    def __init__(self,cor,modelo,ano,valor,vel):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        self.vel = vel

    def correr(self):
        vel = int(input("Digite a velocidade da bike:\n"))
        if vel <= 10 :
            print(f"esta elnto")
        elif vel <= 50:
            print(f"Está normal")
        elif vel >= 100:
            print(f"Está correndo muito")

    def parar(self):
        print(f"A bicicleta parou")
    
    def buzina(self):
        print(f"BIIIIIIIIIIIIIIIIIII")


breno = bike("red","monark",1999,1275,12)
print(breno.cor)

breno.correr()
breno.parar()
breno.buzina()