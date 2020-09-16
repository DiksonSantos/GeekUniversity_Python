'''
numeros = [1,2,3]

print('Lista Original: ',numeros)

ret_pop = numeros.pop()

print(f'Retorno de pop= {ret_pop}')#Imprime o que foi retirado da ultima pos da lista.

ret_pr = print('Lista Atualizada ', numeros) #Uma variavel que recebe uma função print

print(f'Retorno de Print: {ret_pr}') #Retornou Nada (NONE)
'''

def quad_7():
    #print(7*7)
    calculo = 7*7
    return calculo

#quadrado = quad_7()
Guarda_num = 1
ret = quad_7()
#quad_7() #Imprime 49
#print(ret+Guarda_num) # 7*7 = 49 + 1 => 50

'''
A diferença do RETURN  para p PRINT numa função, é que com RETURN
podemos usar o resultado\valor retornado para fazer calculos
por exemplo, já com PRINT isso não seria possivel.

Uma Função NÃO Executa NADA A Baixo da palavra RETURN
'''

def nova_fun ():
    variavel = False  #None = 3,2 e True = 4 , False = 'B'
    if variavel:
        return 4
    elif variavel is None:
        return 3.2
    return 'B'

#print(nova_fun())

def outra_fun():
    return 2,3,4,5

#print(outra_fun()) #Retorna Uma Tupla (Ou Desempacota).

from random import random

def joga_moeda():
    #Gera numero randomico entre 0 e 1
    #valor = random()
    if random() > 0.5: #Depois do IF estava escrito valor que era o nome da variavel da linha de cima.
        return 'Cara'
    return 'Coroa'
#Desta maneira a baixo funciona ok:
cabra = joga_moeda()
#print(cabra)

#Desta Outra tbm:
#print(joga_moeda())

def eh_impar(N):
    print("O Numero que você Digitou é:")
    numero = N
    if numero % 2 != 0:
        return "Impar"  #True
    else:
        return ' É PAR'  #False

num = int(input("Numero: "))
Qual = eh_impar(num)
print(Qual)
