from timeit import timeit
#import timeit
import _collections

class Calculadora():
    """As variaveis são declaradas aqui"""
    def __init__(self, x,y):
        self.UNO = x
        self.DUO = y


    def soma(self):
        """Esta Classe assim como todas as outras Usam as variaveis declaradas em __init__ da Classe"""
        somar = self.UNO + self.DUO
        return somar
        #print(somar)

    def subtrai(self):
        """Neste caso UNO e DUO"""
        sub = self.UNO - self.DUO
        return sub


s = Calculadora(120, 12)
#Acessamos as funções que lidam com os valores que foram dados á Classe
print("", s.soma(), "\n", s.subtrai())


#Testa quanto tempo cada função gasta para o processamento:
print(timeit('s.subtrai()', globals=globals()))
print(timeit('s.soma()', globals=globals()))

#print(globals())

"""
class Dog:

    def __init__(self, nome, idade):
        self.NOME = nome
        self.IDADE = idade


bob = Dog('Bob', 11)
print(bob.NOME, bob.IDADE)
"""
