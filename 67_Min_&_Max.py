'''
Min & Max
Max() Retorna o Maior valor de um Iteravel
'''


lista =[ 1,2,9,6,3,7]
dicionario = {"a":36,"b":45,"c8":8,"d":21,"e":98}



#print(max(lista))

#print(min(dicionario.values())) #retornou o Menor Valor contido numa chave
#print(min(dicionario.keys())) #no caso Mostrou a MENOR letra do alfabeto. "a"

#entrada = int(input("Valor_1: ")), int(input("Valor_2: ")), int(input("Valor_3: "))

#maximo = max(entrada)

#print(f"Valor Maximo: {maximo},\n Valor Minimo: {min(entrada)}")


Nomes = ['Dikson_Santos', 'Smith', 'Jim','Morrison', 'Sweager', 'Dantas']

Lambida_Maxima = (max(Nomes, key=lambda  Nomes: len(Nomes)))# Exibe o nome Mais Comprido da Lista
#print(Lambida_Maxima)

Lambida_Minima = (min(Nomes, key=lambda  Nomes: len(Nomes)))# O mais curto da lista.1
#print(Lambida_Minima)

#DICA DA AULA: SEGURE CTRL E CLIQUE EM CIMA DE UMA FUNÇÃO COMO 'MAX' E O PYCHARM MOSTRA TODA A DOCUMENTAÇÃO DELA.

musicas = [
    {'titulo': 'Poly','tocou':3},
    {'titulo': 'StairwayToHeaven','tocou':4},
    {'titulo': 'EvenFLow','tocou':5},
    {'titulo': 'Alive','tocou':4},
    {'titulo': 'SimplyTheBest','tocou':6},
    {'titulo': 'The Best Around','tocou':7},
    {'titulo': 'Five To One','tocou':20}
]
'''Devido ao fato de estarmos usando MAX, podemos usar o KEY= que pode
 receber uma função Lambda. musica: musica É como um I in J , Usando a chave 'tocou'.
'''
#print(max(musicas, key=lambda musica: musica['tocou'])['titulo'])#Traz só o Titulo da Musica que Mais tocou.

#print(min(musicas, key=lambda musica: musica['tocou'])['titulo'])#..da que menos...

#print(min(musicas, key=lambda musica: musica['tocou'])['tocou'])#Só a quantidade de tocadas.


#Para conseguirmos a chave que tem o maior valor:
maxim = 0
for musica in musicas:
    if musica['tocou'] > maxim: #SE UMA DAS CHAVES (NO CASO A 'TOCOU') FOR MAIRO QUEO NUMERO QUE ESTIVER NA VAR "maxim", "maxim" recebe "tocou"
        maxim = musica['tocou']

#PARA IMPRIMIR O TITULO NA MUSICA QUE TEM O NUMERO IGUAL AO QUE ESTA NA VAR "MAXIM"
for musica in musicas:
    if musica['tocou'] == maxim:
        print(musica['titulo'])

#Conseguir a com Menor valor:
mim = 999
for musica in musicas:
    if musica['tocou'] < mim:
        mim = musica['tocou']
#Mesmo esquema:
for musica in musicas:
    if musica['tocou'] == mim:
        print(musica['titulo'])

'''
É o mesmo que o anterior: musica: musica Da expressão Lambda
Aqui é o FOR musica in musicas:
'''
