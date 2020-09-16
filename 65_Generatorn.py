#Usando Generators:

#Generator é mais rápida para processar grandes quantidades:
nomes = ['Dolg', 'Dikson', 'Djon', 'Django', 'Delphi']
res = (nomes[0] == 'D' for nome in nomes)
print(type(res)) # class 'generator


res = [nomes[0] == 'D' for nome in nomes]
print(type(res)) #Class List

from sys import getsizeof

#print(getsizeof('Dikson')) #-> Retorna a qunt de bytes em memoria tem a String

print(getsizeof('Gow_Dikson_Rodrigues_Dos_Santos'))

#Iterando Generator Expressins:

gen = {x*10 for x in range(0, 1000)}
print(gen)
