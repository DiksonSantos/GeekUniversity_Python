'''
clique em 'Terminal' (ali em baixo) e digite PIP (em minuscula) para ele mostrar
todas as opções de uso.
'''


'''
Instalei o pacote COLORAMA COM O COMANDO -> 'pip install --upgrade pip'
e, pip install colorama.
'''

'''
from colorama import (init, Fore, Back, Style)

print(Fore.LIGHTGREEN_EX + "Gow Dikson Santos.")

print(Fore.MAGENTA + "Magenta")

print(Fore.LIGHTBLUE_EX + 'Azul')
'''

#INSTALEI O PYPDF -> Para criar arquivos PDF aqui no PyCharm:
#Deu tudo ERRADO ESSE MODULO MALDITO, MAS NÃO ESQUENTA NÃO COM ESTA BOSTA ...

import pyPdf

PDF = pyPdf.generate('<h1>Meu Primeiro PDF em Paython</h1>')

with open('Teste_De_Arquivo_PDF_Em_Python', 'wb') as FULL:
    FULL.write(PDF)

#______________________________________________________________
