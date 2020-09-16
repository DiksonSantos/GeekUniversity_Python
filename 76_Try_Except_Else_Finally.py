'''
Dica -> Toda Entrada de Dados deve ser Tratada.

'''

'''
try:
    num = int(input("Informe Numero: "))
    print(f'Voce digitou {num}')
except ValueError:
    print("É pra digitar Um Numro Inteiro")

#Outra forma de fazer a mesma coisa:
num = 0   #Sem esta VAR aqui, o Print NÃO Identado Não funcionaria.
try:
    num = int(input("Informe Numero: "))
    #print(f'Voce digitou {num}')
except ValueError:
    print("É pra digitar Um Numro Inteiro")

print(f'Voce digitou {num}')
'''

'''
#ELSE:
try:
    num = int(input("Informe Numero: "))
    X = num**3
except ValueError:
    print("É pra digitar Um Numro Inteiro")
else:
    print(f'Voce digitou {X}')
'''

'''
#Finally:
try:
    num = int(input("Informe Numero: "))
except ValueError:
    print("É pra digitar Um Numro Inteiro")
else:
    print(f'Voce digitou {num}')
finally:
    print('Executando o Finally')
'''
'''
#Tudo Errado:
def Dividir(a,b):
    try:
        return a / b
    except ValueError:
        print('Digite Apenas Numeros')



Num1 = int(input('Informe o Primeiro Numero: '))
Num2 = (input('Informe o Segundo Numero: '))

Fulano = Dividir(a=Num1, b=Num2)
print(Fulano)


'''

'''
#Solução Com Tratamento Não Generico:
def Dividir(a,b):
    try:
        return float(a) / float(b)
    except ValueError:
        return 'Apenas Numeros !' #Inteiros !'
    except ZeroDivisionError:
        return 'Impossivel Dividir Por ZERO'

Num1 = (input('Informe o Primeiro Numero: '))
Num2 = (input('Informe o Segundo Numero: '))

print(Dividir(Num1, Num2))
'''
'''
#Solução Com tratamento semi-fenerico:
def Dividir(a,b):
    try:
        return float(a) / float(b)
    except:
        return 'Erro Detectado !'
'''

#Trata Dois tipod e de Erros:
def Dividir(a,b):
    try:
        return float(a) / float(b)
    except (ValueError, ZeroDivisionError) as ERR:
        return f'Deu Pau No Parangolê -> {ERR} !'



Num1 = (input('Informe o Primeiro Numero: '))
Num2 = (input('Informe o Segundo Numero: '))

print(Dividir(Num1, Num2))












