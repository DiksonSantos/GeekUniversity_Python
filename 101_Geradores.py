'''
Um Generator É um Iterator, mas nem todo Iterator é Um Generator.

Generators podem ser criados com Funções geradoras


Doferenças entre ambas:

Funções:                                    Generators:
Usam Return                             Usam yeld
Return -> Só Uma vez                    Yeld -> Varaias vezes
Quando executada Retorna Um valor       Quando executada retorna um Generator

'''

def conta_ate(valor_maximo):
    contador = 1
    while contador <= valor_maximo:
        yield contador # YELD -> 'retorna' Mas continua Aguardando o Proximo NEXT
        contador += 1




#Fulano = conta_ate(5)
#print(Fulano)# <generator object conta_ate at 0x7f2568ab0c78>
'''
print(next(Fulano))
print(next(Fulano))
print(next(Fulano))
print(next(Fulano))
print(next(Fulano))
'''

gen = conta_ate(10)
'''
for num in gen:
    print(num, end=',')
'''

#UM EXEMPLO QUE EU VI NO YOUTUBE:

#Sem o Yeld:
def raiz_quadrada(numero):
    result = []
    for I in numero:
        result.append(I*I)
    return result

#Com Yeld:
def Yraiz_quadrada(numero):
    for I in numero:
        yield (I*I)

Lista = [1,2,3]

Meus_Numeros = Yraiz_quadrada([1,2,3,4,5])
print(next(Meus_Numeros))
print(next(Meus_Numeros))
print(next(Meus_Numeros))
print(next(Meus_Numeros))
print(next(Meus_Numeros))

