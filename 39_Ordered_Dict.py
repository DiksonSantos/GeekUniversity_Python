#Modulo Collection Ordered Dict
#O PROFESSOR COMEU BOLA GERAL NESSA AULA. FALOU FALOU MAS NÃO DISSE NADA.
#...NADA FEZ SENTIDO AQUI. ELE DEU MEIAS EXPLICAÇÕES.

'''O QUE EU PUDE INTENDER É QUE: UM DICIONARIO COM O COMANDO
ORDEREDDICT VAI PRINTAR OS ELEMENTOS EXATAMENTE NA MESMA ORDEM
EM QUE ELES ESTÃO NA LISTA. NADA MAIS'''

dicionario = {"a":1, 'B':2, "c":3, "d":0}
alfabeto = {"d","h", "z","a"}

print(dicionario)
print(alfabeto)

for chave, valor in dicionario.items():
    print(f"Chave: ", {chave}, "Valor: ",{valor})

from collections import OrderedDict

alfabeto = {"d","h", "z","a"}
dicionario2 = OrderedDict({"d":4,"h":8, "z":23,"a":0})

for I, J in dicionario2.items():
    print(f"Chave: {I}, Valor: {J}")

print(alfabeto)
