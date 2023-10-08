"""
Exercício 5: Métodos Especiais
Crie uma classe Livro com atributos como titulo, autor e ano. 
Implemente o método especial __str__ para exibir as informações do livro de maneira legível
"""
class Livro:
    def __init__(self, titulo: str, autor: str, ano: int):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano

    def __str__(self):
        return(f"Nome do livro: {self.titulo}") + " - " + str(f"Autor: {self.autor}") + " - " + str(f"ano de lançamento: {self.ano}")
    
livro1 = Livro("1984", "George Orwell", 1949)
print(livro1)