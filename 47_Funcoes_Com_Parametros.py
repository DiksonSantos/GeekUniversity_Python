#Default Parametres função:

'''
#O Parametro Default só pode estar na segunda posição da função.
#Se não for informado o segundo numero, ele por default será 2
def quad(numero, pot=2):
    return numero** pot


print(quad(1,2))
print(quad(2))
print(quad(2,3)) # 2*2=4 + 2*4=8   => 2.2.2
'''
#nome = str(input("Nome: "))
#idade = int(input("Idade: "))
#profiss = str(input("Profissão: "))

'''
def mostra_infor( nome=nome,  Myself=False):
    if nome == 'Dikson' and Myself:
        return 'Seja Bem Vindo!'
    elif nome == 'Dikson':
        return 'I think Wrong'
    return f'Olá { nome}'

#print(mostra_infor('Dikson',True)) #R: Seja bem vindo
#print(mostra_infor('Dikson')) #R: I think Wrong
#print(mostra_infor(nome,False))#R: I think Wrong
print(mostra_infor(nome,True))#R: Seja Bem Vindo
'''

'''
def soma(num1, num2):
    return num1 + num2

def subtrair(num1, num2):
    return num1 - num2

def mat(num1, num2, fun=soma):
    #Esta função Não faria nada não fosse o Terceiro argumento
    return fun(num1, num2)


print(mat(2,3)) #Aqui ela Fez a Soma por Default
print(mat(3,2, subtrair)) # Aqui substituimos o Default(Adição) por outra Função(Subtração).
'''

#ESCOPO:
'''
Variaveis locais e Globais ... já aprendi...
  31min
'''

'''
total = 0

def incrementa():
    global total #Declara/Avisa que queremos usar a variavel Global.
    for I in range(1,6): #De 1 a 6 = 5x => Por 5x a var recebe 1 
        total += 1
    return total

print(incrementa())
'''

#Funções Declaradas dentro de funções:

def fora():
    contador = 0
    def dentro():
        nonlocal contador #Nonlocal são variaveis Não globais, e Pertencem a Outras Funções.
        for Y in range(0,8): # De 0 a 8 São 8 posições
            contador = contador + 1
        return contador
    return dentro()


print(fora())


