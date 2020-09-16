"""
Comma separated Values  -> Valores separados por virgulas.

Porém estes arquivos podem ser separados por outros delimitadores além da virgula.

1;2;3;4
1,2,3
1.2.3.4
1:2:3:4

Fonte de dataSets: http://www.dados.gov.br/dataset
"""

Arqui = open('original.csv', 'r')
X = Arqui.read()
#print(X)

#print(X.split('\n'))

Arqui.close()

"""
with open('Dikson.csv', 'r') as Abre:
    C = Abre.read()
    print(C)
    print(C.split('\n')[1:]) # Mostra da linha 2 em diante.
"""


from csv import reader
"""
with open('Dikson.csv') as FILE:
    LER_CSV = reader(FILE)
    for Linha in LER_CSV:
        #Cada Linha é uma lista;
        print(f'Nome: {Linha[1]} Idade: {Linha[1]}')
"""

"""
with open('Dikson.csv') as FILE:
    LER_CSV = reader(FILE)
    next #Pula o Cabeçalho.(LER_CSV)
    for Linha in LER_CSV:
        #Cada Linha é uma lista;
        print(f'Nome: {Linha[0]}- Idade: {Linha[1]}') #No Caso [0] é o primeiro Item Da Linha, [1] é o segndo da linha
"""

#DictReader:

from csv import DictReader

with open('original.csv') as Objeto:
    Ler = DictReader(Objeto, delimiter=',')#Coloquei o delimiter, mas funciona igual sem ele. Pois separar por virgula é o padrão.
    for L in Ler:
        #Cada Linha é um Order Dict
        #"Nome,País,Altura (em cm)" É exatamente o que esta no cabeçalho do arquivo:
        print(f'{L["Nome"]} nasceu no(a)(s) {L["País"]} e mede {L["Altura (em cm)"]}')


