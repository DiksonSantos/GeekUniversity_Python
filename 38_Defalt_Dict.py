#Default Dict

#dicionario = {'curso': 'Python & R', 'curso_2': "Bancos de Dados", 'Curso_3': 'Estatistica'}

#Imprime o Conteudo de Curso_3 = Estatistica
#print(dicionario['Curso_3']) #Caso eu digitasse um valor inesistente ia dar erro

#Ao criar o Default Dict podemos informar um valor Default utilisando um 'Lambda'
#...caso informarmos uma chave inexistente, esta chave sera criada e o valor Default
#...atribuido a ela.
#-> 'Lambdas' são funções sem nome que não recebem parametros de entrada.

from collections import defaultdict

dicionarios = defaultdict(lambda: 0)

dicionarios['curso']= 'Progamação' #Ad chave+valor

dicionarios['02'] #Como aqui não foi adicionado nenhum Valor, ele mostra 0 no print

print(dicionarios)

#Aqui a diferença -> Ele apresentara o valor 0 (ZERO) da Lambda
print(dicionarios['Outro']) #Se fosse um Dicionario comum ia dar pau -> keyerror

