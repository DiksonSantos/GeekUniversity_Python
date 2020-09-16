#import random
from random import random

#help(random)

#print(random.random())  #sem os parenteses no final ele só mostra como Objeto.



#for I in range(4):
    #print(round(random()))

from random import uniform

#   GERA APENAS NUMEROS ENTRE 3 & 7  -> TOTAL DE 9 NUMEROS.
#for k in range(0,9):
#    print(int(uniform(3,7)))


from random import randint

#GERA 4 NUMEROS ALEATORIOS ENTRE 1 & 9:
#for Y in range(4):
#    print(randint(1,9), end=' ')



#CHOICE É USADO EM LISTAS NUMERICAS OU NÃO:
#from random import choice
Lista0 = ['pedra', 'papel', 'tesoura']

#print(choice(Lista0))


#SHUFFLE  -> EMBARALHA INFORMAÇÕES:

from random import shuffle

Numeros = [1,2,3,4,5,6,7,8,9]
STRINGS_N = ['1','2','3']
print('',Numeros, end=' ')
shuffle(Numeros)
print('\n',Numeros)

shuffle(Lista0)
print(Lista0)

shuffle(STRINGS_N)
print(STRINGS_N)
