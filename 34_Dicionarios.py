'''
paises = {"EUA:":"Estados Unidos", "BR:": "Brasil", "EU:": "Europa", 1:"Australia"}
#Metodos -> .item , .key , .value
for chave, valor in paises.items():
    print(chave, valor)
print(" _________________________")
for chave in paises.keys():
    print(chave)
print("___________________________")
for valor in paises.values():
    print(valor)
# https://www.w3schools.com/python/python_ref_dictionary.asp

print(paises[1], "-> Valor Através da Chave")

#ACESSAR VIA GET
print(paises.get("BR:"))
'''
'''
paises = {"EUA":"Estados Unidos", "BR": "Brasil", "EU": "Europa", 1:"Australia"}

BR = paises.get('BR4', 'Nada encontrado')
if BR:
    print("Achei")
else:
    print("Nada")
'''
'''
for c, p in paises.items():
    print(c,p)
'''
'''
#Podemos definir uma resposta padrão caso não encontremos o item na lista
paises = {"EUA":"Estados Unidos", "BR": "Brasil", "EU": "Europa", "AU":"Australia"}

country = str.upper(input("Digite o Pais: "))
pais = paises.get(country,'Not Found Não deu') #Caso não encontre o 1 argumento, substitue pelo segundo
print(f"Encontrado o: {pais}")
'''
#CONTINUA EM 30:35MIN
'''
paises = {"EUA":"Estados Unidos", "BR": "Brasil", "EU": "Europa", "AU":"Australia"}
print("BR" in paises) #Resultado é TRUE
print("RU" in paises)
'''

'''
#ACEITA QQ TIPO DE DADO
Localidades = {
    (35.6895, 4040): 'Esc em Tokyo',
    (40.7128, 8080): 'Esc em NY',
    (37.6895, 6060): 'Esc SP',
}
print(type(Localidades))
#print(Localidades)

for U, J in Localidades.items():
    print(U, J)
for N in Localidades.keys():
    print(N, "Chave")
for I in Localidades.values():
    print("Valor", I)
'''

'''
#Adicionae itens Num Dicionario:
receita = {'jan': 100, 'Fev':200, 'Mar': 300}

receita['abr'] = 300 #Forma de ADD item ao final deste Dict

Nova = {'mai': 450} #Cria uma variavel com um novo dicionario

receita.update(Nova) #Com o metodo Update Adicionamos este novo Dict ao anterior.

receita.update({'Jun':500}) #Outra forma de fazer.


#Atualizando dados num Dict
#1
receita['mai'] = 2.000 #Ele Atualizou o mês de MAIO
receita['JUL'] = 4.000 #Assim ele cria um Novo

Remov_Mar = receita.pop('Mar')

#receita.update({'Mar':2.500}) #Mar aqui seria como um novo item, e não mais o antigo Mar sendo atualizado.
del receita['Fev'] #Não da mais pra recuperar como no POP

for I, J in receita.items():
    print(I, J)
#Não podemos ter chaves repetidas.
#______________
'''
#
'''
# 1 - Poderiamos Utilizar uma Lista para iss? Sim

carrinho = [] #Lista vazia

prod1 = ['PS1', 1.240, 1,'R$']
prod2 = ['Jogo', 1, 140,"R$"]
carrinho.append(prod1), carrinho.append(prod2)

#print(carrinho)


#PODERIAMOS UZAR UM DICT P ISSO? SIM:
carrinho = []
prod0 = {'nome': 'PS2', 'Quant': 1, 'Price': 2.300}
prod3 = {'nome':'Godovar 4', 'Quant': 1, 'Price': 150}
carrinho.append(prod0)
carrinho.append(prod3)
for c in carrinho:
    print(c) #Facilita na visualização  & É mais facil para Add prod e remover tbm.
'''

'''
#Cleaning o DICt

D = dict(a=1, b=2, c=3)
print(D)


#Copiando Dict

Novo = D.copy()
print(Novo, "Copia")
Novo['d'] = 4
print(Novo," Adicionou")

D.clear()
print(D, "Esvaziou")

#Shallow Copy:
D = dict(a=1, b=2, c=3)
new = D

new['d'] = 5
print(new, "5 Recebido")
'''

#Forma Unuzual de criar Dicts:

Other = {}.fromkeys(['A','B', 'C'], "Desconhecido") #Chaves São A , B e C ,
#...os valores delas São 'Desconhecido'.

Other['A'] = 'CONHECIDO'
Other['B'] = 'SEI SEI '

Mais_Um = {}.fromkeys(range(0,4),"Eu_Sei_Python" )
for M in Mais_Um:
    print(M,end="-")
print('\n')
#print(Other)
print(Mais_Um)
