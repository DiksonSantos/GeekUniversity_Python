'''
Filter  ->   Filtra dados de uma devida coleção
'''

valores = 1,2,3,4,5,6

#Somou Todos os valores e dividiu pela quantidade de itens de 'valores'
#media = sum(valores) / len(valores)

#print(media)

#
import  statistics

#Dados coletados de algum sensor

dados = [1.3,2.7,0.8,4.1,4.3,-0,1]

#Calculando a media dos dados usando a fun mean()

#Outro método de Calcular a média, porém usando Biblioteca Statistic do Python
media = statistics.mean(dados)
Media_valores = statistics.mean(valores)
#print(round(media),' Media dos Dados (Arredondados)')
#print(media, ' Dados Originais')
#print(Media_valores,' Media dos Valores')

#Assim como a função MAP a FILTER tbm recebe Dois Parametros.
#...Ou seja. Uma Função + Um Iteravel

#CONTINUA EM 9:30min

#Media é uma função que esta contendo a Lista DADOS
res = filter(lambda x: x> media, dados)

'Todos os Valores da Lista DADOS que são maiores que a Média' \
' da Tupla VALORES (Que é 2):'
#print(list(res),' Itens de DADOS MAiores que e Média')

#Filtrar tudo o que for produzido por MEDIA que for MENor que o que Estiver em DADO.
#res = filter(lambda x: x< media, dados)# Lista modificada (Mesmo nome da anterior) ALL OK
'Todos os Valores da Lista DADOS que são MENORES'
#print(list(res),'Itens de DADOS MEnores Que A media')

#Porém assim como em MAPs os resultados só são mostrados Uma vez:
#print(f'Mesmo Resultado: {list(res)}')

#print(type(res))# Class filter
#______________________________________

#REMOÇÃO DE DADOS FALTANTES/VAZIOS:

paises = ['','Australia','Camberra','','Norway', 'Singapura','','Portugal','','Angola']
#print(paises)

Country = filter(None, paises)
#print(list(Country))# OBS: Se as aspas '' contiverem um espaço entre elas, elas vão ser mostradas.

#Outra forma/Maneira
contador = filter(lambda pais: len(pais) > 0, paises)#Valor ZERO numa lista STRING significa False
#print(list(contador))

#Outra forma:
diferente = filter(lambda pais: pais != '', paises)
#print(list(diferente))

#A DIFERENÇA ENTRE MAPs E FILTER É:
'''MAP -> Recebe Dois parametros. Uma Função e um Iteravel E retorna um Objeto,
FILTER -> Quase igual, porem retorna somente os itens pré determinados pela função
que o acompanha. Filter Retorna True e False (Basicamente).
'''
#EXEMPLO MAIS COMPLETO:

usuarios = [
    {'UserName':"Dikson", 'Tweet':['Eu Gosto de Pizza', 'Eu gosto de Yaksoba']},
    {'UserName':"Santos", 'Tweet':['Eu Gosto PCs']},
    {'UserName':"Antony", 'Tweet':[]},
    {'UserName':"Al_Simons",'Tweet':['Eu Gosto de Guerra']}
]

#Filtrar usuarios Inativos (Ou que não twitaram nenhuma vez):
'''Dentro da lista existem dicionarios, Dentro da Chave Tweet onde ZERO for True ou
seja, não houver nada la, ele filtra e Printa.'''
inativos = list(filter(lambda  u:  len(u['Tweet']) == 0, usuarios))
#Vai Mostrar apenas usuarios que não twitaram nada.
#print(inativos)


#Outra Maneira de Fazer Isso:
inativos_ = list(filter(lambda usuario: not usuario['Tweet'] ,usuarios))
#print(inativos)

#COMBINAR FILTER & MAPs:

nomes = ['Veronica', 'Ana', 'Marcia','Katifunda', 'Gow']

#My myself I did It:
for I in nomes:
    if len(I) < 5:
        print(I, ' Nome Com MENOS de 5 Letras') #Imprime só os elemento da lista que tem menos de 5 letras.
    if len(I) > 5:
        print(I, 'Nome com +Mais+ de 5 Letras' )

print('\n'*1)

#METODO COM LAMBDA: (PROFESSOR)
#Mapeou que a frase 'Este Nome é' vai ser usada com cada elemento FILTRADO da lista (que contiver menos de 5 Letras).
#..no caso a primeira LAMBDA é uma função que Concatena a frase. A segunda LAMBDA é a LISTA Filtrada.
LISTA = list(map(lambda nome: f'Este Nome é {nome}', filter(lambda nome: len(nome)<5, nomes)))
#print(list(LISTA), ' Nomes Com Menos de 5 Letras')
for J in LISTA:
    print(J.upper(), 'Com Menos de 5 Letras')
