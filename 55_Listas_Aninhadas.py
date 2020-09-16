'''Listas Aninhadas'''

#Exemplos

#Uma Lista de Listas:   -> Dei ENTER depois das Virgulas, Mas é uma lista 'Linear'
listas = [[1,2,3],
          [4,5,6],
          [7,8,9]] #Ou uma Matriz 3x3

#print(type(listas))# class List

'''
dicio = {'Dikson': 'Santos', 'Luciene': 'Chaves'}
for D, R_ in dicio.items():
    print(f'Nome: { D}, Sobrenome: { R_}')
'''

#Imprimindo Linha e Coluna:
#print(listas[0][2]) #Linha ZERO elemento 2  (Ou o 3 de 0,1,'2')

#Linha 1 que é na verdade a Segunda Linha (depois da ZERO)+Elemento 2 que é o '6'
#print(listas[1][2])

'''
# Loop no Loop
for bloco in listas:  #PERCORRE OS BLOCOS
    for elemento in bloco: #PERCORRE OS ELEMENTOS DOS BLOCOS
        print(elemento, end=' - ') #IMPRIME OS ELEMENTOS
    #print(bloco)
'''

#Uma_Linha = ([(valor) for valor in listas] for lista in listas)
#print(Uma_Linha)

#Com Uma Linha Apenas (DA P/ USAR O ,END= NO FINAL)
# 1 PERCORRE OS BLOCOS C/ PRIMEIRO FOR | 2 PERCORRE OS ELEMENTOS COM O SEGUNDO FOR.
#[[print(valor,end='->') for valor in lista] for lista in listas]

#ASSIM ELE MANTEM/MOSTRA OS COUCHETES:
Nada = [[(valor) for valor in lista] for lista in listas]
#print(Nada,end='')


#https://www.vooo.pro/insights/tutorial-compreensao-de-listas-python-com-exemplos/
'''
#O PRIMEIRO RANGE DEFINE A QUANTIDADE DE ELEMENTOS
#O SEGUNDO RANGE DEFINE A QUANTIDADE DE BLOCOS
TABULEIRO = [[numero for numero in range(1, 4)] for valor in range(1,4)]
print(TABULEIRO)

for bloco in TABULEIRO:
    for elemento in bloco:
        print(elemento,end=' ')
'''
#GERANDO JOGADAS P/JOGO DA VELHA:
#Se o numero gerado pelo FOR for PAR preencha com 'X' | Se IMPAR preencha com 0
velha = [['X' if numero % 2 == 0 else 'O' for numero in range(1,4)] for valor in range(1,4)]
#print(velha)


#GERANDO VALORES INICIAIS:
print([['*' for I in range(1,4)] for J in range(1,4)])

