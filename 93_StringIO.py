'''
Para ler ou escrever arquivos do S/O é preciso permissão, De Leitura OU Escrita.

StringIO -> Utilizado para ler e criar arquivos em memoria.
'''

from io import *

'''
Podemos criar um arquivo em memoria já com uma String Inserida, ou mesmo vazio
para inserirmos Texto depois
'''

Mensagem = 'Somente Uma String Normal'

#Isto é equivalente a
arquivo = StringIO(Mensagem)
#Isto, são a 'mesma coisa':
#Arquiv = open('Arquivo.txt', 'w')

#As regras de utilização são as mesmas.

#Imprime ...
print(arquivo.read())
