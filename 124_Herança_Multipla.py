
"""
Herança multipla é a possibilidade de Uma classe herdar Atributos\Metodos
de Muitas classes diferentes.
"""

class Base1:
    pass

class Base2:
    pass

class Base3:
    pass

#Isso é Herança multipla.
class Multi(Base1, Base2, Base3):
    pass

#____________

class Base1:
    pass

class Base2(Base1):
    pass

class Base3(Base2):
    pass

#Aqui esta acontecendo a mesma coisa que ali em cima:
#Mas; A Base3 Possui a 1 & 2, Neste Caso é uma derivação Indireta.
class Multi(Base3):
    pass



class Animal:

    def __init__(self, nome):
        self.__Nome = nome

    def cumprimentar(self):
        return f'Meu nome é {self.__Nome} '

class Aquatico(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def nadar(self):
        '''Maneira não mais popular de se fazer acesso a atributos.'''
        return f'{self._Animal__Nome} esta nadando'

    def cumprimentar(self):
        return f'Eu sou {self._Animal__Nome} do mar'


class Terrestre(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def andar(self):
        return f'{self._Animal__Nome} is walking'

    def cumprimentar(self):  #Classe sendo reescrita aqui. (Mesmo nome la em cima).
        return f'Eu sou {self._Animal__Nome} terrestrisss'

class Pinguim(Aquatico, Terrestre):

    def __init__(self, nome):
        super().__init__(nome)





#testando:

Baleia = Aquatico('Wally')
print(Baleia.nadar())
print(Baleia.cumprimentar())

Tatu = Terrestre('Bola')
print(Tatu.cumprimentar())


PD = Animal('Elefante')
print(PD.cumprimentar())

Tux = Pinguim("Tux")
print(Tux.andar())
print(Tux.nadar())
# Se inverter Desta Ordem -> 'Terrestre, Aquatico' Para esta -> 'Aquatico, Terrestre' R: 'Eu sou o Tux do mar'
print(Tux.cumprimentar()) #Eu sou Tux terrestrisss  -> Usou o metodo da Classe Terrestre.


#Objeto é instancia de....
#Tudo True.
print(f'Tux é instancia de Pinguim? {isinstance(Tux, Pinguim)}')
print(f'Tux é instancia de Pinguim? {isinstance(Tux, Aquatico)}')
print(f'Tux é instancia de Pinguim? {isinstance(Tux, Terrestre)}')
print(f'Tux é instancia de Pinguim? {isinstance(Tux, Animal)}')
print(f'Tux é instancia de Pinguim? {isinstance(Tux, object)}')
