'''
ARQUIVOS RELACIONADOS COM ESTE:
Pacotes do 1 ao 4
1 & 2 em Pacote_Python
e 3 & 4 em 'Sub_Pacote'
'''

#Aaqui da certo o Pacote 1 & 2  ,  Sub_Pacote    {Os 3 & 4 estão na mérda}
from Pacote_Python import Pacote_1

print(Pacote_1.funcao_1(1,3)) #AQUI É A FUNÇÃO NO ARQUIVO
print(Pacote_1.pi) #AQUI É UMA VARIAVEL.


from Pacote_Python import (Pacote_1,
                           Pacote_2, Sub_Pacote)

print(Pacote_2.funcao2()) #'Programação em Python'


#AI SIM , AGORA SIM:
from Pacote_Python.Sub_Pacote import Pacote__3, Pacote__4

print(Pacote__3.funcao3())

print(Pacote__4.funcao4())


