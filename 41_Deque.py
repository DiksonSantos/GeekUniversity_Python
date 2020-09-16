#Deque se trata de uma lista de alta performance.

from collections import deque

#Criando Deques:

deq = deque('Dikson_Santos')

print(deq) #Imprimiu cada letra como se fosse um elemento

#Add elementos no deque:

deq.append("Filho") #Add a palavra Filho como se fosse UM elemento.

print(deq)

deq.appendleft("Gow") #Da p add Item no começo da lista
print(deq)

deq.pop() #Removeu Ultimo elemento
print(deq)

print(deq.popleft()) #Exibiu elemento removido do começo (esquerda)
#deq.popleft()
print(deq)
