'''
PDB -> Python Debigger
'''
'''
def divide(A, B):
    print(f'Primeiro Termo={A} Segundo_Termo={B}')  #Aqui o PRINT é uma maneira de debugar o Codigo.
    try:
        return float(A) / float(B)
    except(ValueError, TypeError, ZeroDivisionError):
        return 'Valores Inserido = Incorretos.'
NUM1 = int(input("Primeiro Numero: "))
NUM2 = int(input("Segundo Numero: "))


Numero = divide(A=NUM1, B=NUM2)
print(f'{Numero:.2f}')
'''

#  {Variavel_Resposta:.{1f}   Sendo 1 o Numero de casas de pois da virgula.

'''
#FORMAS MAIS PROFISSIONAIS DE SE FAZER O DEBUG USANDO O DEBUGGER:
def divide(A, B):
    try:
        return float(A) / float(B)
    except(ValueError, TypeError, ZeroDivisionError):
        return 'Valores Inserido = Incorretos.'
NUM1 = int(input("Primeiro Numero: "))
NUM2 = int(input("Segundo Numero: "))


Numero = divide(A=NUM1, B=NUM2)
print(f'{Numero:.2f}')
'''

# 1 EXEMPLO COM O PDB:

#Precisamos importar a biblioteca PDB

'''
Comandos do PDB:
-> l = para listar onde estamos no codigo
-> n = proxima linha
-> p = Imprime variavel
-> c = Continua a execução
'''

'''
import pdb

nome = 'Juma'
Especie = 'Onça Pintada'
#pdb.set_trace()
Info = nome +' '+ Especie
Abtat = 'Amazonia Brasileira'
Conclusao = Info + ' Vive Em ' + Abtat
print(Conclusao)
'''

'''
# 2 EXEMPLO COM O PDB:

nome = 'Juma'
Especie = 'Onça Pintada'
import pdb; pdb.set_trace() #Separamos com ; Para Dois comandos na mesma linha.
Info = nome +' '+ Especie
Abtat = 'Amazonia Brasileira'
Conclusao = Info + ' Vive Em ' + Abtat
print(Conclusao)
# Este PDB é usado/testado na hora, e logo depois já é descartado.
'''

'''
# 2 EXEMPLO COM O PDB:

#A partir do Python 3.7 Não se usa mais o PDB, mas sim o BreackPoint

nome = 'Juma'
Especie = 'Onça Pintada'
breakpoint() #AQUI AQUI -> Já cai la no PDB sem precisar importar Nada.
import pdb; pdb.set_trace() #Separamos com ; Para Dois comandos na mesma linha.
Info = nome +' '+ Especie
Abtat = 'Amazonia Brasileira'
Conclusao = Info + ' Vive Em ' + Abtat
print(Conclusao)
'''


def soma(l, n, p, c): #Nunca use variaveis assim. Prefira algo como Num1, Num2 etc ...
    return l+ n+ p+ c #Para evitar problemas.

print(soma(1,3,5,7))

#Como neste caso se as variaveis tiverem o mesmo nome dos comandos do debug -> Utilize
#... o comando P para imprimi-las antes.
