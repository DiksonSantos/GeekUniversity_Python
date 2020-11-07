import math

#Retorna o produto de um container Numerico:

num_v1 = [2, 4, 6, 8]
num_v2 = [2, 4, 6, 8]
num_v3 = [2, 4, 6, 8]

#print(math.prod(num_v1))
#print(math.prod(num_v2))
#print(math.prod(num_v3))

"""
É o produto ou:

2*4*6*8 == 348
"""

produto = 2*4*6*8
#print("Classico: ", produto)


print("(Antigo) Raiz Real: ",math.sqrt(17))
print("(Novo) Raiz Inteira:", math.isqrt(17)) #Retornar a parte Inteira da Raiz Quadrada de um Numero:




#Retorna Distancia Euclidiana Entre Dois Pontos 2D ou 3D:

Pont_3D1 = (12, 50, 40)
Pont_3D2 = (6, 7, 13)


print(math.dist(Pont_3D1, Pont_3D2))

Pont_2D1 = [12, 50]
Pont_2D2 = [6, 7]

print(math.dist(Pont_2D1, Pont_2D2))


#Calcula Média simples:
import statistics
Notas = [4, 6, 9]

#Usando A função Statistics:
R = statistics.mean(Notas)
RF = statistics.fmean(Notas)
print(int(R))
print(RF)

#Metodo "Manual":
soma = 0
acu = 0
for I in Notas:
    soma += I
    acu += 1
print(soma/acu)



#Media Geometrica:
Geo = statistics.geometric_mean(Notas)
print(Geo)


#Encontrar a moda Estatistica:

modal = [2,2,2,3,6,5,5,5,5,8,7,7,4,1,12]
m_Modal = [2,2,2,5,5,5,6,4,8]

x = statistics.mode(modal)
print(x)

j = statistics.multimode(m_Modal)
print(j)
"""
#print(len(j))
if len(j) == 2:
    print("Bimodal")
    if len(j) == 3:
        print("TRI_Modal")
        if len(j) > 4:
            print("Multi Modal")
"""

def moda(j):
    if len(j) == 2:
        print("Bimodal")
    if len(j) == 3:
        print("TRI_Modal")
    if len(j) >= 4:
        print("Multi Modal\ PoliModal")
#H = moda(j)
#print(H)

outra = [2,2,2, 3,3,3, 4,4,4, 5,5,5]

K = moda(outra)

