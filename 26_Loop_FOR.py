'''
lista = ["Um", 2, "Três"]
Lista = ["G","o","w","","D","i","k","s","o","n"]
for Y in Lista:
    print(Y,end="")

print("\n")

numeros = [1,2,3,4,5]
numeros.reverse()
print("\n",numeros)

for indice, letra in enumerate(Lista):
    print(letra, indice)

#Pode descartar um valor usando _ se não for precisar dele...
for _, letra in enumerate(Lista):
    print(letra,end="")
'''
'''
quant = int(input("Quantidade: "))
for n in range(1, quant+1):
    print(quant)
'''
#
'''
print("Informar Ex: Primeiro segundo , terceiro valor de uma sequencia.")
quant = int(input("Quantidade: "))
soma = 0

for n in range(1, quant+1):
    num = int(input(f'Informe o {n} de {quant} Valor: '))
    soma = soma + num
    print(quant)
print(f"A soma dos valores digitados é: {soma}")
'''
import emoji
#
emoj = '\U0001f60d'
amos_2 = '\xF0\x9F\x98\x81'
print()
print(emoj)
for num in range(0,10):
    #A cada laço ele repete a carinha uma vez a mais na linha.
    print(emoji.emojize('\U0001f60d'*num)) # Esta linha esta usando o IMPORT

print(emoji.emojize(amos_2))
print('\x9f')
#  https://apps.timwhitlock.info/emoji/tables/unicode

print(amos_2)
