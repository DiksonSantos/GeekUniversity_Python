'''
O Yield -> Trata elemento por elemento de uma Lista

A ListComprehenssion -> Gera A Lista Inteira para depois fazer em seus elementos o procedimento que lhe é pedido
'''




#Geradores:
'''
def num():
    for num in range(1,10):
        yield num  #Yield é uma variação do return


ge1 = num()
print(type(ge1))
print(next(ge1))
print(next(ge1))
print(next(ge1))


ge2 = (num for num in range(1,10))
print(ge2) #<generator object <genexpr> at 0x7f801dd3bcf0>
print(next(ge2))
print(next(ge2))
'''

print(sum(num for num in range(1,3))) #(1 á 3 = 0, 1, 2 ) = 0+1=1 + 1+2 = 3

import time

#Generation Expression:

gen_inicio = inicio = time.time()
print(sum(num for num in range(100000)))

gen_tempo = time.time() - gen_inicio


#list_comprehension
list_inicio = time.time()
print(sum(num for num in range(100000)))
list_tempo = time.time() - list_inicio

print(f'Generator Expression Levou {gen_tempo}') #Levou MENOS  tempo
print(f'List Comprehenssion Levou {list_tempo}') #Took more time to be done.
