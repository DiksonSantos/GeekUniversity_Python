'''
w -> Cria & Escreve
x -> Exclusivo para criação, se o arquivo já existir Vai dar Erro
r -> Exclusivo para leitura de um arquivo
a -> Abre para a escrita acrecentando o que for escrito a um arquivo já existente.

'''

'''
try:
    with open('Frutas.csv' , 'x') as X:
        X.write("Nada")
except:
    print("Arquivo Já Existe")
'''


'''
#Este é o mesmo codigo anterior, Porem com o A de Append ao inves do W:
with open('Frutas.csv', 'a') as F_:
    while True:
        fruta = str.title(input("Informe Uma Fruta: "))
        if fruta != 'Sair':
            F_.write(fruta)
            F_.write('\n')
        else:
            break
'''


Caixa = open('Frutas.csv', 'r')
print(Caixa.read())

