'''
Map serve para mapear valores para uma função.

'''

import  math

def are(r):
    '''Calcula area de um circulo com Raio r'''
    return math.pi * (r ** 2)


#print(are(2))
#print(are(5.3))


Lista_Raios = [2,5,7.1,0.3,10,44]

#Forma Comum:
areas = []
for R in Lista_Raios:
    areas.append(are(R))
    #print(areas)
#print(areas)


#FORMA 2 Usanso o Map:

#Map é uma Função -> recebe dois parametros
#O primeiro argumento é uma Função, o Segundo é um Iteraval (lista Dic etc...).
#map(fun, iter)
areas = map(are, Lista_Raios)
'''
print(areas)
print(type(areas)) #Class Map
print(list(areas))# Primeira Utilização do Resultado.
'''
#Devido ao resultado já ter sido Mostrado/Utilizado no Print de Cima, ele já não fica mais Visivel/Disponivel aqui.
print(tuple(areas),"Look Here")

'''
# Python program to demonstrate working 
# of map. 
  
# Return double of n 
def addition(n): 
    return n + n 
  
# We double all numbers using map() 
numbers = (1, 2, 3, 4) 
result = map(addition, numbers) 
print(list(result)) 
'''

#MAP APLICA UMA FUNÇÃO A CADA ELEMENTO DE UMA LISTA.


#Mais Um Exemplo:

#Isso é uma Lista Contendo Tuplas
cidades = [('Berlin', 29),('Cairo',36), ('Buenos Aires', 19), ('Los Angeles',26)
,('Tokyo',27), ('New York',28), ('Londres',22)]
#print(cidades)


'''
for C in cidades:
    print(C)
'''
#Agora Digamos que precisemos converter os grau Celsius em Fahrenheit
#A formula de conversão é a seguinte -> F = 9/5 * C + 32     -> Onde C é o Grau Celsius

def conv_cel_to_Fahren(Temp):
    prod = 9/5 * Temp + 32
    return prod

Teste = conv_cel_to_Fahren(1)
print(Teste," Fahrenheite")

#Agora Uma Lambda com a mesma finalidade:

#O que esta entre () é o que vai ser retornado Ex: dado[0] é 'Berlin', dado[1] é a Temperatura
#... Aplicamos a formula (9/5) * dado[1] -> Que é a temperatura + 32
c_Para_f = lambda dado: (dado[0], round(9/5) * dado[1] + 32) #o ROUND é pra arredondar os valores.

#Converti Pra lista + Usamos a Fun MAPs com A função Criada + a Lista.
# Especificou que a função Vai ser usada na Lista CIDADES (??) Acho que sim..
#ACABO DE CHAGAR A CONCLUSÃO DE QUE A FUNC MAP SÓ FUNCIONA COM LAMBDAS, E NÃO COM DEFs
print(list(map(c_Para_f, cidades)))

'''O resultado é a exibição de uma lista com as Tuplas já com suas temperaturas 
convertidas em Fahrenheit  LINDO ISSO. -_- 
'''
#https://wiki.portugal-a-programar.pt/dev_geral:python:lambda
