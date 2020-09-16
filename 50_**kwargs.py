'''
Transforma os parametros (Nomeados) da função em um dicionario:
'''

def cores(**kwargs):
    print(kwargs)

#cores(Python="Amarelo", Java='vermelho',html='azul')
# Resultado -> {'Python': 'Amarelo', 'Java': 'vermelho', 'html': 'azul'}

def cores_(**kwargs):
    for Linguagem, cor in kwargs.items():
        print(f'A cor simbolo de {Linguagem.title()} é {cor.title()}')

#cores_(Python="Amarelo", Java='vermelho',html='azul')

def cumprimento_especia(**kwargs):
    if 'Gow' in kwargs and kwargs['Gow'] == 'Python':#-> Se Gow estiver no Dicionario & o Valor de Gow for Python:
        return 'Você é Féra Mesmo!'
    elif 'Gow' in kwargs:#Se Gow Estiver no Dicionario porém Valor informado NÃO é Python:
        return f'{kwargs["Gow"]} Valor Não é Python'
    return 'A Chave Informada NÃO É GOW'# <- Se a Chave Informada á Função NÃO for Gow

'''No caso aqui corresponde ao primeiro IF'''
guardar = cumprimento_especia(Gow='Python') #Chave = Gow & Valor = Python
#print(guardar) #Retorna -> Voce é fera mesmo

'''Se a chave Não for Gow R: I Am not sure...
Ou ELIF (Se Gow não for a chave) I am not sure...'''
guardar1 = cumprimento_especia(Nope='Python')
#print(guardar1)

'''Se Gow dor a chave -> Retorne o valor *Gow_Dikson* logo após o valor informado
depois de *Gow*'''
guardar3 = cumprimento_especia(Gow='Nome')
#print(guardar3) #Mostrou na ordem inversa O valor Depois a Chave da linha de cima.

guardar4 = cumprimento_especia(Gw='Pyt')
#print(guardar4)

VAZIO = cumprimento_especia()
#print(VAZIO)# -> A Chave Informada NÃO É GOW

#_________________

#Ordem para inserção de Elementos nos argumentos de Uma Função:

#-> Parametros Obrigatorios -> idade , nome
#-> *args
# -> Parametros default (Não Obrigatorios)  ->solteiro=False
# -> **kwargs

def minha_funcao(idade, nome, *args, solteiro=False ,**kwargs): #Ordem de declaração dos diferentes tipos de parametros.
    print(f'{nome} tem {idade} anos')
    print(args,' Informações numericas foram pro Args') # **Args
    if solteiro: #Aqui é p lidar com o True & False
        print('Solteiro')
    else:
        print('Casado')
    print(kwargs, "Aqui São os **kwards")

#solteiro esta como False por default. Se eu não inserir nada na função...
#...Este Status vai aparecer como Casado.
#minha_funcao(34,'Dikson', 35.000, 3.500, 36.000, solteiro=True, bom='bom', forte='Sim')

#____

#Desempacotar com kwargs

def mostra_nomes(**kwargs):
    #Respeite os tipod de ASPAS
    return f"{kwargs['NOME']} {kwargs['SOBRENOME']}"#Aqui tem que ser igual Ás CHAVES das listas


nomes = {'NOME':'Boole', 'SOBRENOME':'Head'} #Repare NOME & SOBRENOME são iguais aos que estão ali no RETURN

#print(mostra_nomes(nomes='gow', sobrenome='santos'))
print(mostra_nomes(**nomes))


#_________________________________

def soma_multiplos_Numeros(a,b,c):
    print(a+b+c)
lista = [1,2,3]
dicionario = dict(a=1, b=2, c=3)

soma_multiplos_Numeros(*lista)
soma_multiplos_Numeros(**dicionario)
