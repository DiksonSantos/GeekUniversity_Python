'''
Permite fazer a atrb e retorno de val numa unica expressão

'''

#Sintax:

# ->  variavel := expressão

print(nome := "Dikson")

#3.7
print(nome, 'Santos')
'''
#3.7
cesta = []
fruta = input('Fruta: ')
while fruta != 'Jaca':
    cesta.append(fruta)
    fruta = input('Informe a fruta: ').capitalize()
    if fruta == 'Jaca':
        print(cesta)
'''

# Python 3.8  -> Uma Economia de Linhas Significativa:
cesta = []
while(fruta := input('Diga Uma Fruta: ').upper()) != 'JACA':
    cesta.append(fruta)

    #Poŕem auqi esta parte NÃO funcionou da mesma forma  :/
    #if fruta == 'JACA':
    #    print(cesta)


