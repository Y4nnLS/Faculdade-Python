"""
Crie um programa que simule um processo de compra online, lidando com exceções de estoque insuficiente e erros de pagamento.
"""
class Product:
    def __init__(self, name, stock):
        self.name = name
        self.stock = stock
    
    def purchase(self, quantity):
        try:
            if quantity > self.stock:
                raise ValueError("Estoque insuficiente.")
            self.stock -= quantity
            print(f"{quantity} unidades de {self.name} compradas.")
        except ValueError as e:
            print(e)

product = Product("Camiseta", 10)
product.purchase(9)