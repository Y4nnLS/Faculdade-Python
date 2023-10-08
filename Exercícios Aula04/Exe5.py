"""
Desenvolva um programa de gerenciamento de contas bancárias com classes. Trate exceções ao tentar sacar mais dinheiro do que o saldo disponível.
"""

class ContaBancaria:
    def __init__(self, titular: str, saldo: float):
        self.titular = titular
        self.saldo = saldo
    
    def __str__(self):
        return(f"titular: {self.titular}")+" | "+str(f"Saldo: R${self.saldo}")
    
    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            return True
        else:
            return False
        
    def sacar(self, valor):
        try:
            if valor > self.saldo:
                raise ValueError("Saldo Insuficiente")
            self.saldo -= valor
        except ValueError:
            print("Valor invalido")
        
    def exibir_saldo(self):
        return f"Saldo atual da conta de {self.titular}: R$ {self.saldo: .2f}"

c1 = ContaBancaria("Yann", 1000.00)
c1.depositar(100)
print(c1.exibir_saldo())
c1.sacar(10000)
print(c1.exibir_saldo())
print(c1)