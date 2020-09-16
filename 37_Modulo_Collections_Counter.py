from collections import Counter
'''A Função Counter enumera as ocorrencias dentro de Tuplas Dicionarios Ou Listas (qualquer 
um destes (ou os ITERAVEIS)'''

lista = (1,1,1,1,1,2,2,2,2,23,3,3,3,3,3,4,4,4,4,45,5,5,5,5,)
res = Counter(lista)
print(res) #Imprimiu -> 1 apareceu 5 vezes. 3= 5 Ocorrencias. E assim por diante

Meu_nome = 'Gow Dikson'
print(Counter(Meu_nome)) #Letra 'o' Aparece 2x no meu nome, o restante 1x

Texto = '''É possível acessar seus cursos da Udemy em diversos dispositivos 
e plataformas , ( PLAtaFORMAS ) tanto em desktops/notebooks Windows e Mac, como dispositivos 
móveis Android e iOS. Para isso, são necessários os requisitos de sistema
 a seguir.'''

#Quantas vezes cada letra aparece na String ou No Texto
print(Counter(Texto))
#Divide o texto em palavras para cada espaço entre elas.
Quant_Palavr = Texto.split()
#Trasnforma tudo em Minusculo
Quant_PalavrLOW= Texto.lower()
#Conta todas aspalavras transformadas em nanicas.
Quantas = Quant_PalavrLOW.count('plataformas')
#Quantidade de palavras em que o texto foi dividido
print(len(Quant_Palavr), "-> É a quantidade de Palavras")
print('Quantas Palavras: ', Quantas)
print(Counter(Quant_Palavr).most_common(3))  #O  .mostcommon com parametro3 mostra as 3 palavras que mais aparecem no Texto.
