
"""
Testes TDD
Existem cursos especificos para Testes de Software .

O professor não falou muita coisa com coisa.

"""

class Gato:

    def __init__(self, nome):
        self.__Nome = nome

    @property
    def nome(self):
        return self.__Nome


    def miar(self):
        print(self.__Nome, " Esta Miando")


Felix = Gato("Felix")

Felix.miar()

print(Felix.nome)

