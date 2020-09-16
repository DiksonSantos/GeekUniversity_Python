"""
Pickle é o Processo de Transformação de Um Objeto Python em um Objeto Binario
e Vice-Versa.
Também conhecido como Serialização/Deserialização.
"""

import pickle

class Animal:

    def __init__(self, nome):
        self.__nome = nome

    def comer(self):
        print(f'{self.__nome} Esta Comendo')

    @property
    #Faz com que um valor restrito por Dunder __ possa se tornar um método, acessivel por
    #ponto .   Ou:  .metodo  -> .nome la em baixo\fora da classe.
    def nome(self):
        return self.__nome



class Gato(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def mia(self):
        print(f'{self.nome}, esta Miando')

class Cachorro(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def late(self):
        print(f'{self.nome} esta latindo.')

"""
#ESTA É A ESCRITA E CRIAÇÃO DE UM ARQUIVO BINARIO OU PICKLE:
Felix = Gato('Felix')
Pluto = Cachorro("Pluto")
with open('animais.pickle', 'wb') as FILE:
    #Pickle Binariza Dump ->Passa(Esses dois Objetos como Uma Tupla) e Grava em FILE
    pickle.dump((Felix, Pluto), FILE)
"""

#AGORA A LEITURA E DESBINARIZAÇÃO DO MESMO:

#                    RB -> Leitura Binaria.
with open('animais.pickle', 'rb') as Arquivo:
    gato, cachorro = pickle.load(Arquivo)
    print(f'O Gato Chama-se {gato.nome}')
    gato.mia()
    print(f'O Tipo do Gato é {type(gato)}')

    print(f'O Cachorrinho chama-se {cachorro.nome}')
    cachorro.late()
    print(f'O Tipo do Gato é {type(cachorro)}')
