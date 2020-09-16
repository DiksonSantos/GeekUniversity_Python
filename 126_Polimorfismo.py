"""
Polimorfismos -> Objetos com muitas formas/comportamentos
"""

class Animal(object):

    def __init__(self, nome):
        self.__Nome = nome

    def falar(self):
        # raise serve para lançar exceções'''
        raise NotImplementedError('A classe filha precisa implementar este método')

    def comer(self):
        print(f'{self.__Nome} esta comendo...')


class Cachorro(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f'{self._Animal__Nome} fala Au AU')

class Gato(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f'{self._Animal__Nome } fala Miau MIAU')


class Rato(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        pass


#teste:

Tom =Gato('Tom-Cat')
Tom.falar()
Tom.comer()
print('\n')
Pluto = Cachorro('Pluto')
Pluto.falar()
Pluto.comer()
print('\n__________')
Mikey = Rato('Mikey Mouse')
Mikey.falar()
Mikey.comer()
