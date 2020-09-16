'''Para não precisar-mos usar o camando CLOSE ou CLOSED, podemos usar
o bloco WITH e identar tudo o que estivermos trabalhando (txt), assim
só dentro do bloco é que o arquivo estara aberto e disponível'''

with open("TEXTO_LER.txt") as TX:
    print(TX.read())

#SE TENTAR IPRIMIR AQUI FORA, ELE INFORMA QUE O ARQUIV JÁ ESTA FECHADO
#print(TX.read())

