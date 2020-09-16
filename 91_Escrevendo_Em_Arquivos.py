'''
Existe abertura para a escrita OU para a leitura de arquivos.
'''

'''
#Escrita:
with open('Novo_Texto.txt', 'w') as File_:
    File_.write('Primeira Linha escrita no txt em andamento\n')
    File_.write("Mais Uma linha aqui\n ")
    File_.write('Fechamento do txt')
'''

'''
Abrindo o arquivo com o parametro W , se ele não existir, ele passa a existir,
caso ele já exista, ele será subsitituido a cada vez que o parametro w
for usado na abertura.
'''

'''
with open('Novo_Texto.txt', 'r') as LER:
    print(LER.read())
'''

with open('Frutas.csv', 'w') as F_:
    while True:
        fruta = str.title(input("Informe Uma Fruta: "))
        if fruta != 'Sair':
            F_.write(fruta)
            F_.write('\n')
        else:
            break

