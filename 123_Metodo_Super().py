"""
Metodo SUper() se refere a super Classe.
"""


class Animal:

    def __init__(self, nome, especie):
        self.__Nome = nome
        self.__Especis = especie

    def faz_som(self, som):
        print(f'O {self.__Nome}, faz o som {som}')



class Gato(Animal):

    def __init__(self, nome, especie, raca):
        #Metodo de herança 1:
        #Animal.__init__(self, nome, especie)
        #METODO RECOMENDAVEL DE HERDAR ATRIBUTOS DA CLASSE:
        super().__init__(nome, especie) #Aqui não precisa do SELF dentro dos ().
        super().faz_som('mia mia mia')
        self.__Raca = raca


Felix = Gato('Felix', 'Felino', 'Angora')
Felix.faz_som('Miau') # Usa a função DEf faz som.


"""
Com SUPER(). conseguimos fazer acesso a qualquer elemento da classe Principal
"""
