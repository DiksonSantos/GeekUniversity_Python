'''
Funções de maior grandesa -> Higher Order Functions - HOF



São funcões que retornam outras funções

Ou funções que podem ser passadas como argumentos para Outras funções.
'''

'''
def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a /b

def calcula(num1, num2, funcao):
    return funcao(num1, num2)

#TESTANDO:

objeto = calcula(10,10,somar)
print(objeto)

Objeto2 = calcula(20,30, subtrair)
print(Objeto2)

'''

'''
#NESTED FUNCTIONS:


#Funções dentro de funções Inner Functions ou Funções Internas


from random import choice

def cumprimento(pessoa): #Esta é a função Mãe
    def humor(): #Função Filha
        return choice(('E ai ', 'Suma Daqui ', 'Hey You I like you! ')) #Conteudo da Função Filha
    return humor() + pessoa #Retorno Da Função Mãe -> Retorna a Função FILHA + o Argumento da Funão MÃE

#TESTANDO:
Fulano = cumprimento('Dikson')
print(Fulano)
'''

'''
#Retornando Funções de Outras Funções:

from  random import  choice

def faz_me_rir():
    def rir():
        return choice(('kkk', 'hahaha', 'yayaya'))
    return rir



laughing = faz_me_rir()
print(laughing())
'''

#Funções Internas Podem Acessar o Escopo de Funções mais Externas -> Ou A DEF interna pode Acessar
#... os argumentos da DEF Mãe.

from random import choice

def faz_me_rir_mais_ainda(person):
    def dando_risada():
        risada = choice(('huahuahua', 'lolololo', 'qqqqqq'))
        return f'{risada}, {person}' #AQUI EU ESTOU ACESSANDO O ARGUMENTO DA FUNÇÃO PRINCIPAL
    return dando_risada() #AQUI ACESSO O PRODUTO DA FUNÇÃO INTERNA QUE USA A FUN PRINCIPAL

CICRANO = faz_me_rir_mais_ainda('hualhuey')
print(CICRANO)
