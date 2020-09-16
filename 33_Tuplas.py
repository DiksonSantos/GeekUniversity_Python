tupla = ("Gow Dikson")
#print(tupla)

tupla_2 = (1,2,3,4,5)
#print(tupla_2.index(3)) #Indice 2 tem o numero 3

tupla_3 = 1,2,3,4,5,6,7,8,  #Mesmo SEM os parenteses É UMA TUPLA

#print(tupla_3)

tupla4 = (4) #Isso não é uma tupla -> SE TIVER UMA VIRGULA É TUPLA

TUPLA5 = (4,) #ISSO É UMA TUPLA

TPL = tuple(range(1,14))
#print(TPL)
'''
#Desempacotamento de tuplas:
tpl = ("Gow", "Dikson", "Rodrigues", "Dos", "Santos")
meu, nome, completo, esta, aqui = tpl
#Mesmo numero de elementos da tupla.
print(meu, nome, completo, esta, aqui) 
'''
'''
#print(sum(tupla_3)) #mas, min , len
tpl_nom = ("Gow ")
tpl_nom_ = "Dikson"
print(tpl_nom + tpl_nom_) #Não consegui imprimir as que tem conteudo numerico.

tuplas8 = (8,9)
tupla9 = (9,10)
#
tupla5 = tuplas8 + tupla9
print(tupla5)
if 8 in tuplas8:
    print(True, "Sim esta")

for indice, valor in enumerate(tupla5):
    print("Indice:",indice, "Valor:",valor)# ,end='-'
'''

meses = ("JAN", 'FEV', 'MAR', 'ABR', 'MAI', 'JUN', 'JUL', 'AGO', 'SET', 'OUT', 'NOV', 'DEZ')
mes = int(input("Digite numero do mes: "))
print(meses[mes-1]) #FENOMENO ESTRANHO COM O INDICE.
