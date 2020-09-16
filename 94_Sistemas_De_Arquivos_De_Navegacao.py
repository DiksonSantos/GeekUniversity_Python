'''
Sistema de Arquivos e Navegação

Para manipular arquivos do sistema operacional (como pastas etc) precisamos
fazer o import do modulo OS

os -> Operation Sistem
'''

import os

# getcwd()  -> Significa Current Work Directory

#print(os.getcwd()) #->Mostra/Imprime o Diretorio Atual ->  /home/dikson01/PycharmProjects/guppe


#-> O que esta entre parenteses é o comando CHDIR é para mudar de pasta
os.chdir('..')

#print(os.getcwd())


os.chdir('/') #-> Voltei Pra Raiz
#print(os.getcwd())


os.chdir('/home/dikson01/') #-> Fui pra o Diretorio Atual
#print(os.getcwd())



#Pasta Original, ou Dos arquivos deste Curso:
os.chdir('/home/dikson01/PycharmProjects/guppe/')
#print(os.getcwd())


#Identificando O S/O usando este Modulo:
#print(os.name) #Posix  (???)


#Mais informações a respeito do SO usado no momento:
'''#posix.uname_result(sysname='Linux', nodename='notebook-debian',
 release='4.19.0-6-amd64', version='#1 SMP Debian 4.19.67-2+deb10u2 (2019-11-11)',
  machine='x86_64')'''
#print(os.uname())


#Mostra Linux como SO :
import sys
#print(sys.platform)








'''
#Imprime o Caminho Atual:
print(os.getcwd())

#No caso Aqui teriamos que criar (Pelo Prompt) a Pasta NOVA_7 para então apontarmos para ela
#A Pasta ONE_MORE esta dentro de NOVA_7 Também foi criada usando o Prompt:
res = os.path.join(os.getcwd(), 'NOVA_7', 'ONE_MORE')

#Mudou para a variavel RES que contém o Caminho apontado.
os.chdir(res)

#Resultado -> Mostrou o caminho anterior , mas, agora apontado para dentro da pasta NOVA_7:
print(os.getcwd())
'''

#Listar diretorios:
#print(len(os.listdir('/'))) #28 Pastas dentro de '/'


print(list(os.scandir('/home'))) #Depois de eu Usar o List -> Mostrou o que tem dentro de 'home' -> 'Dikson'
