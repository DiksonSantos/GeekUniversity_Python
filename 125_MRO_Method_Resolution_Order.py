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


#Aqui ele esta escolhendo o cumprimentar da Terra, pois ele esta na primeira posição em relação ao Aquatico
class Pinguim(Terrestre, Aquatico): #A ordem foi invertida em relação ao cod da aula 124.

    def __init__(self, nome):
        super().__init__(nome)




Tux = Pinguim("Tux")

print(Tux.cumprimentar()) #Eu sou Tux do mar  -> Usou o metodo da Classe Aquatico.

"""
Tux is walking
Tux esta nadando
Eu sou Tux do mar
"""

"Primeiro ele vai procurar o Cumprimento na classe Pinguim, Mas como não tem," \
" ele em seguida procura na classe terrestris, depois Aquatico, depois Animal," \
"builtins.object depois -> Repare que é Da classe mais em baixo vai procurando até a" \
" ultima de cima (Ou a primeira escrita nesta folha de códigos" \
"Ou: A procura por uma classe Cumprimentar vai ocorrer Nesta ordem aqui:" \
"Pinguim(Terrestre, Aquatico): ...  "

