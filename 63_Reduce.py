'''
Assim como map() e filter() a função reduce() recebe como parametro Uma Função
e um iteravel. EX:   ->    reduce(função, dados)
'''

'''
Esta funão funciona da seguinte maneira: 

EX: Pega uma lista lista01 = [r1, r2, r3, r4]
Faz r1+r2 e calcula o resultado destes dois com r3 , e então r1+r2=a1 + r3 =
 (a1+r3)+r4  e assim sucessivalmente até o final. (Pelo que eu entendi).
'''


#Vamos ver um exemplo com Multiplicação que faz muito sentido. (Com conta de + não faz muito...)

from functools import reduce

def mult(x,y):
    um = x
    dois = y
    res = um * dois
    return res

#Ou podemos usar esta lambda tbm (ao invés):
multi = lambda x, y : x*y


lista = [1,2,3,4,5,6]
lista_simples = [1,2,3]# 1x2 = 2  -> 2x3 = 6 ...

#DIFERENTE DO MAP E DO FILTER  nós precisamos usar uma função que receba DOIS PARAMETROS.

teste = reduce(mult, lista_simples)

print(teste)

teste_1 = reduce(multi, lista)
print(teste_1)

'''O REDUCE FUNCIONA COMO SE FOSSE UM 'FOR' a diferença é que ele vai guardando os
valores para usar p/ proximo calculo'''

res = 1
for r in lista:
    res=res  * r
print(res)


'''
O criador da linguagem recomenda 99% das vezes usar o FOR ao inves do Reduce .
'''
