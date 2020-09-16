#IMPORTANDO DUAS FUNÇÕES NUMA LINHA:

#from random import random as rdm, randint as rdi

#MANEIRA ORGANIZADA DE FAZER VÁRIOS IMPORTS:

from random import (random,
randint,
shuffle,
choice)

#Conforme feito a cima, UM Por Linha Usando uma TUPPLA.

numeros = [1,2,3,4,5,6,7,8,9]
print(numeros, "Originais")
shuffle(numeros)
print(numeros, 'Embaralhados')
