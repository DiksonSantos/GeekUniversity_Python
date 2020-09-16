"""
# Writer gera Um Objeto para que possamos escrever num arquivo CSV.
#Writerow -> Escreve Linha Por Linha. Este método Recebe Uma Lista.
from csv import writer

# Aqui na abertura o 'w' Se usado Num mesmo arquivo (Já escrito), vai apaga-lo e Re-escrever Tudo.
# O 'a'  Acrescenta o que for digitado de novo ao que já existe no CSV.
# Com o 'a'  ele também Repetiu o Cabeçalho do arquivo.
with open('filmes.csv', 'a') as Arquivo:
    escritor = writer(Arquivo)
    #Uma variavel iniciada com Nada Dentro.
    filme = None #Esta Var precisa existir antes do Loop While para ser possivel usa-la Lá.
    #Aqui é inserção do cabeçalho (PRIMEIRA_LINHA), Mas, não é obrigatorio.
    #Aqui a Linha do Cabeçalho esta antes do Loop pois o Cabeçalho só é escrito UMA vez.
    escritor.writerow(['Titulo', 'Genero', 'Duração'])
    while filme != 'sair':
        filme = input('Nome Do Filme: ')
        if filme != 'sair':
            genero = input('Informe o Genero Do Filme: ')
            duracao = input("Duração do Filme: ")
            #Recebe estes 3 Inputs como Uma Lista inserindo-as a Cada Linha:
            escritor.writerow([filme, genero, duracao])
"""

# DictWrite  -> Agora ao Inves de Listas, vamos Criar Dicionarios:
from csv import DictWriter
with open('Filmes2.csv', 'w') as Movie:
    cabecalho = ['Titulo', 'Genero', 'Duration']
                                    #Este fieldnames aqui é do tipo Kwargs
    Escritor_CSV = DictWriter(Movie, fieldnames=cabecalho)# Fieldnames é Nome dos Campos, ou COlunas.
    #Metodo Apenas para escrever o Cabeçalho;
    Escritor_CSV.writeheader()
    File_ = None
    while File_ != 'sair':
        File_ = input('Nome Do filme: ')
        if File_ != 'sair':
            Genero = input("Digite o Genero do Filme: ")
            Duration = input("Duração Do Filme: ")
            #As Chaves do Dicionario Devem Ser exatamente iguais ás do Cabeçalho (Ali em cima).
            #Metodo Apenas para escrever as Linhas:
                                #Do_Cabeçalho : Da Var , ...
            Escritor_CSV.writerow({"Titulo": File_, "Genero": Genero, "Duration": Duration})



