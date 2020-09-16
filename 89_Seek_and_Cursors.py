Arquivo = open("TEXTO_LER.txt")
#print(Arquivo.read())

#Arquivo.close()


#MOVIMENTAR O CURSOR PELO TEXTO COM A FUNÇÃO SEEK:
print("_____________________________________________________________________________")
'''É usada para apontar o cursor para determinado
 local no texto. O Parametro (0) por exemplo, define isto.'''
#Nesta cso ZERO significa Começar a Leitura no INICIO DO ARQUIVO
#Arquivo.seek(0)

#Começou A Ler e Imprimir o Texto a partir da Posição 64 em diante.
#Arquivo.seek(64)
#print(Arquivo.read())

#ReadLini -> Cada Print Mostra a linha seguinte do texto.
#print(Arquivo.readline())
#print(Arquivo.readline())
LINHA = Arquivo.readline()
#print(LINHA.split(' ')) #Separando Por Espaços

#ReadlineS  Cada Linha se torna um Item de Uma Lista:
#print(Arquivo.readlines())
print(len(LINHA))

#REAUMO:
# 1-> Abrir Arquivo ->      arquivo = open("nome_do_texto.txt')

#2 ->Trabalhar Arquivo -> print(arquivo.read())

#3 -> Fechar Arquivo arquivo.close()

Arquivo.close()

print(Arquivo.closed)  #CLOSED

#Limitando até onde o arquivo vai ser lido:

Arquivo = open("TEXTO_LER.txt")
print(Arquivo.read(89)) #Até a posição\Caractere numero 89


