import os


# 1 - > Descobrir se um arquivo ou Diretorio Existe:
'''
print(os.path.exists('TEXTO_LER.txt')) # -> TRUE

print(os.path.exists('NOVA_7')) # -> TRUE




print(os.path.exists('/home/dikson01/Imagens')) #True
'''

#CRIANDO ARQUIVOS:
'''
#Forma 1:
open('Teste_Criando.txt', 'w') .close()

#Forma 2:
open('Teste_Criado.txt', 'a') .close()
#Outra forma seria com o WITH OPEN() ...
'''

#FORMA 3:
#os.mknod('/home/dikson01/Karalho.txt') #Se o arquivo Já existir da Pau


#CRIANDO PASTAS (Uma Após a Outra):

#os.mkdir('/home/dikson01/DIRETORIO_TST')# CRIOU NO CAMINHO O DIR DIRETORIO_TST
#os.mkdir('/home/dikson01/DIRETORIO_TST/DIR_2__')

#CRIANDO PASTAS (Todas de Uma Vez):

#os.makedirs('/home/dikson01/DIRETORIO_TST/DIR_2__')#Criou as Duas Ultimas Pastas numa tacado Só.

#os.makedirs('/home/dikson01/DIRETORIO_TST/DIR_2__', exist_ok=True)#Caso as pastas Já existam NÃO  da Pau
#...Se já existir, Ele Apenas Ignora Mantendo lá o que já existe (Sem Altera-lo)

#Para RENOMEAR  a estrutura de pastas:
#os.renames('/home/dikson01/DIRETORIO_TST/DIR_2__', '/home/dikson01/TesteDir/DIR_1__')

#RENOMEIA ARQUIVOS:
#os.rename('/home/dikson01/Karalho.txt', '/home/dikson01/KRL.txt')# Renomeia Arquivo.

#DELETAR ARQUIVO:  (NÃO VAI PRA LIXEIRA MORRE DIRETO)  (SÓ APAGA ARQUIVOS, NÃO DIRETORIOS)
#OBS; Se o arquivo estiver aberto ou Sendo Lido por algum software, você tera um erro.

#os.remove('/home/dikson01/KRL.txt')




#REMOVER DIRETORIOS:
#os.rmdir('/home/dikson01/DIRETORIO_TST/DIR_2__')# Removeu o Ultimo
#os.rmdir('/home/dikson01/DIRETORIO_TST')# Removeu o DIRETORIO_TST


'''
Comando Para criar (neste caso) 950 arquivos dentro da pasta 'PASTA':
touch arquivos{1..950}.doc
'''

#Excluiu TODOS os arquivos dentro de 'PASTA'
'''
#Percorrer os arquivos acessados\Escaneados dentro da estrutura de pastas Apontada:
for arquivos in os.scandir('/home/dikson01/PASTA'):
    print(f'{arquivos.name}') #Mostra os nomes dos arquivos dentro da Pasta Apontada
    if arquivos.is_file():#Se Estes Itens Forem Arquivos
        os.remove(arquivos.path)#Apague-os
'''
'''
from send2trash import send2trash

send2trash('/home/dikson01/PASTA/dc.txt')#OK IT WORKS !!!   -> Mandou Pra Lixeira
'''

import os
import tempfile
'''
#Criando Um Diretorio com Arquivo Temporario:
with tempfile.TemporaryDirectory() as tap: #Esta Linha Cria Um diretorio dentro da Pasta /tmp Da Raiz do Sistema Linux.
    print(f'Criei o Diretorio Temporario em {tap}') #Aqui MOSTRA que criou o mesmo
    with open(os.path.join(tap, 'Temporario.txt'),'w') as arquivo:#Cria o 'Temporario.txt' dentro do Diretorio
        arquivo.write('Dikson_Santos\n')# Aqui eu escrevi meu Nome dentro do Arquivo -> 'Temporario.txt'
    '''#Esta linha de baixo é apenas para manter as coisas como elas estão e não perder todo o trabalho das Linhas ANteriores'''
    #input()

'''ASSIM QUE O PROGRAMINHA A CIMA É ENCERRADO A PASTA E O ARQUIVO(S) DENTRO DELA DEIXAM DE EXISTIR.'''

#Este código a Cima possivelmente não funciona no S\O Windows
'''
'''




'''
#Criando Um Arquivo Temporário:
with tempfile.TemporaryFile() as TMP:
    #REPARE QUE TEM UM 'B' depois do Write Quer dizer-> Converter Para Binario.
    #Arquivos Temporarios só recebem dados BINARIOS:
    TMP.write(b'Aqui eis que escrevemos mais e mais e mais\n')
    TMP.seek(0) #Volta ao Inicio do Texto/Arquivo
    print(TMP.read())
'''

arquivo = tempfile.NamedTemporaryFile()
arquivo.write(b'This is Dikson Santos kicking some asses\n') #Não aceita caracteres da lingua portuguesa como 'é'

print(arquivo.name)# mostra o nome que o arquivo vai ter na pasta TMP
print(arquivo.read())

input()# Segura o Codigo em Aberto
arquivo.close()
