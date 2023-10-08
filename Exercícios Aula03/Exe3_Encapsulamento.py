"""
Exercício 3: Encapsulamento
Crie uma classe ContaBancaria com atributos saldo e titular. Implemente métodos para depositas, sacar e exibir o saldo.
"""

class ContaBancaria:
    def __init__(self, titular: str, saldo: float):
        self.titular = titular
        self.saldo = saldo
    
    def __str__(self):
        return(self.titular)+" - "+str(self.saldo)
    
    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            return True
        else:
            return False
        
    def sacar(self, valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            return True
        else:
            return False
        
    def exibir_saldo(self):
        return f"Saldo atual da conta de {self.titular}: R$ {self.saldo: .2f}"

c1 = ContaBancaria("Yann", 1000000.00)
c1.depositar(100)
print(c1.exibir_saldo())
c1.sacar(91100)
print(c1.exibir_saldo())
print(c1)