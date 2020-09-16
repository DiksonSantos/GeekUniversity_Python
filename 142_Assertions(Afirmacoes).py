"""
Checagens / Questionamentos

Usamos para checar se expressoes no codigo são validas ou não.

Podemos personalizar mensagens de erro.

SE UM PROGRAMA PYTHON FOR EXECUTADO COM O PARAMETRO -O, NENHU ASSERTION
SERÁ VALIDADO. OU SEJA , TODAS AS VALIDAÇÕES JÁ ERAM...
"""
#USANDO O ASSERT QUASE COMO SE FOSSE UM IF:
def soma_num_pos(a, b):
    assert a > 0 and b > 0, 'Numeros Precisam Ser Positivos'
    return a + b


oBJETO = soma_num_pos(2, 6)

print(oBJETO)

#Obj2 = soma_num_pos(2, -3) #Exibe a mensagem dentre o Erro -> 'Numeros Precisam Ser Positivos'
#print(Obj2)


def comer(comida):
    assert comida in (
        'pizza',
        'hamburguer',
        'batata_frita'
    ), \
        "A Comida tem que ser Fast Food"  #Mensagem que vai aparecer Dentre as de erro, Caso O que for Digitado não esteja na Lista.
    return f'Eu estou comendo {comida}'


Comida = input("Comida: ")
Obj3 = comer(Comida)
print(Obj3)

"""
Se você executar no terminal o Programa Python com -O (Menos Ó Maiusculo antes do nome do 
arquivo .PY ) -> Todos os ASSERTS não vão funcionar, e nenhuma mensagem de erro vai
ser mostrada na tela. Tudo vai rodar como se tudo estivesse OK. 
"""
