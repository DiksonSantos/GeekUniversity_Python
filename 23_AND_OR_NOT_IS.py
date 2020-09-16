'''
Estruturas Logicas
'''

'''
numeros = int(input("Digite_Numero"))
#numeros = [10,20,30]
Mais_Numeros = [10,40,50]

if numeros not in Mais_Numeros:
    print("Não Tem")
 else:
    print("Tem")
'''
'''
for x in numeros:
    if x in Mais_Numeros:
        print("Tem")
    if x not in Mais_Numeros:
        print("Não Tem")
'''
'''
#FAZENDO UMA PIZZA:
requested_toppings =["Anchovas", "Cogumelos","Cheese"]
available_toppings = ["Queijo", "Molho Branco","Anchovas", "Cogumelos"]

for requested_topping in requested_toppings:

    if requested_topping in available_toppings:

        print("Adding " + requested_topping + ".")

    else:
        print("Sorry, we don't have " + requested_topping + ".")

print("\nFinished making your pizza!")
'''
ativo = True
#ativo = False
logado = False
#logado = True

if ativo or logado:
    print("Pronto Para Logar")
if ativo is True:
    print("Ativo no Sistema")
if ativo and logado: #Forem TRUE
    print("Bem Vindo User")

if not ativo:
    print("Ative seu sistema")
if not logado:
    print("Digite sua senha")
