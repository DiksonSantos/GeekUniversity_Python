receita = {'jan': 100, 'Fev':200, 'Mar': 300, 'Abr': 450}
'''
for chave in receita: #Selecionando somente as chaves
    print(chave)
'''
'''
for chave in receita: #Selecionando Somente o Valor das Chaves
    print(receita[chave])
'''

for valor in receita:
    print(receita[valor])

#Era mais facil e legilvel\Logico fazer o seguinte:
for I in receita.values():
    print(I)

#Agora a Junção dos Dois metodos do Professor:
#Poderia usar somente o metodo 'items'... mas ...
for chave in receita:
    print(f'{chave}  : {receita[chave]}')  #Isso é muito mais bagunçado, e da no mesmo.

#Este seria o meu Jeito de resolver isto:
for I, J in receita.items():
    print(f"Chave-> {I}, Valores-> {J}")


soma = sum(receita.values())
#sum(receita.values())
#print(sum(receita.values()))
print(soma," É a soma de todos os Elementos.")

maximo = max(receita.values())
print(maximo," É o Maior Valor na lista")

minimo = min(receita.values())
print(minimo, "É o Minimo Valor da Lista")
