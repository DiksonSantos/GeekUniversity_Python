idade = int(input("Idade: "))

if idade < 18:
    print("Menor de Idade")
if idade == 18:
    print("Maior de Idade")
elif idade >=33 and idade != 34: #Se eu tivesse colocado Somente IF aqui, ele imprimiria ->
    #Maior de Idade & Também "Ficando Veio..."
    #Mas como coloquei ELIF ele só imprime "Ficando..."
    print("ficando Veio hein brow")
if idade == 34 and idade > 18:
    print("Cuidado Cuidado Se Não voce dança")
'''else:
    print("Desconhecido")'''
