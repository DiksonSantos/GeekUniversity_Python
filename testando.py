#nome = "Dikson"

#print(f"{nome}")

'''
numeros = int(input("Digite_Numero: "))
#numeros = [10,20,30]
Mais_Numeros = [10,40,50]

if numeros not in Mais_Numeros:
    print("Não Tem")
else:
    print("Tem")
'''
'''
#FAZENDO UMA PIZZA:
requested_toppings =["Queijo de Minas", "Anchovas", "Cogumelos","American Cheese"]
available_toppings = ["Queijo de Minas", "Molho Branco","Anchovas", "Cogumelos"]

for requested_topping in requested_toppings:

    if requested_topping in available_toppings: #Se o que ele pede esta no que nós temos.

        print("Adding " + requested_topping + ".") #Se o que for pedido esta na lista dos disponiveis...

    else:
        print("Sorry, we don't have " + requested_topping + ".")

print("\nFinished making your pizza!")
'''
'''
#Inserindo Itens na posição desejada da lista:
lista = []
lista.insert(1, 'G')
lista.insert(2, 'o')
lista.insert(3, 'w')
#Inserindo Itesn no final da Lista:
lista.extend(" Dikson")
lista.extend(" Santos")
lista_2 = ["-> Graduado", "Em TI"]
##Emendando Uma Lista na Outra:
Soma = lista+lista_2

print(Soma)
print(lista)

for letra in Soma:
    print(letra, end=' ')
'''
#_________________________
'''
#Desempacotamento de tuplas:
tpl = ("Gow", "Dikson", "Rodrigues", "Dos", "Santos")
meu, nome, completo, esta, aqui = tpl #Tem que ser a mesma quantidade de itesn
#Mesmo numero de elementos da tupla.
print(meu, nome, completo, esta, aqui)
'''


#____
Pais = str.upper(input("Nome Do Pais: ")) #Se a chave for um Numero ele não reconhece.
paises = {"EUA":"Estados Unidos", "BR": "Brasil", "EU": "Europa", 'AU':"Australia"}

#Se o que estiver aqui for uma chave na Lista
BR = paises.get(Pais, "Não Encontrado")# O uso da String na frente do 'Pais' Dispensa o IF e ELSE das linhas de baixo.
print(f"Pais: {BR}")
'''if BR:
    print(f"Achei: {BR}")# ...Ele Imprime
else:
    print("Nada")''' #Caso Não <-
#-> O GET serve para evitar que o software de Crach\pau por não encontrar um item na lista.
#____



