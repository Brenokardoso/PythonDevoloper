class Conta:
    def __init__(self,saldo ,numero_da_agencia):
        self._saldo = saldo                               
        self.numero_da_agencia = numero_da_agencia

    def __str__(self):
        return(f"{self.__class__.__name__} -> {','.join([f'{chave}:{valor}' for chave,valor in self.__dict__.items()])}") 

    def depositar(self,valor):
        self._saldo += valor
        return(self._saldo)

    def sacar(self,valor):
        self._saldo -= valor
        return(self._saldo)
    
    def mostar_saldo(self):
        return(self._saldo)
    




conta = Conta(100,2525)
conta.depositar(40)
conta.sacar(60)
print(f"Agencia = {conta.numero_da_agencia} --> Saldo = {conta.mostar_saldo()}")
