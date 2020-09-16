'''
Entendendo o *args
'''

'''O Parametro *args utilizado em uma função, coloca os valores extras informados
como entrada em uma tupla. Então desde já lembre-se que tuplas são imutaveis.
'''
#Ex
#Precisa somar inumeros elementos sem ter que criar inumeras entradas de dados na função
def somatudo(num1,num2,num3):
    return num1+num2+num3

#print(somatudo(1,2,3))

#Para isso usariamos:

def somaMais(*args):
    tot = 0
    for N in args:
        tot += N
    return tot

#Não Importa quantos numeros eu informar nas esntradas da função, ele vai processar todos.
#Do_It = somaMais(1,2,5) #1 + 2 + 5 = 8
#print(Do_It)

def somaEficiente(*args):
    '''Esta função faz o mesmo da de cima, porém é
    Muitissimo mais eficiente (Menos linhas de codigo'''
    return sum(args)

#somador = somaEficiente(1,2,3,4,5) #Somou Todos os elementos da Tupla criada.
#print(somador)

def baguncinha(expo1, expo2, *args):
    print(expo1,expo2)
    return sum(args)

#Bag = baguncinha('Esta', 'Soma', 1,2,3)
#print(Bag) #Só imprimiu os Numeros
#print(baguncinha('oi','Irene',1,2,3))#Esta tbm, mas nenhuma deu pau (BOM).

#print(baguncinha('Alpha', 'Bravo'))# Imprimiu ZERO 0

def verificador(*args):
    if "Gow" in args and "Dikson" in args:
        print('Bom ve-lo de volta')
        return f'Seja Muito Bem Vindo {args}'
    return 'I Am Not Sure who you are :/'    #Aqui é o ELSE

#print(verificador('Gow','Dikson'))
#fulaninho = verificador('Fulano', 'Antony')
#print(fulaninho)

colectioN = [1,2,3]
print(somaEficiente(*colectioN)) #Usando o * antes do nome da Lista/Coleção FUNCIONA
#FUNCIONA COM TUPLAS e LISTAS e DICTs SEM CHAVE-VALOR (SÓ C CHAVE Funciona).

