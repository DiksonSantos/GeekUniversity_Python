'''
for num in range(2,17):
    if num == 15:
        break
    else:
        print(num, end="-")
'''
while True:
    command = str.upper(input("Digite Sair Para Encerrar: "))
    if command =='SAIR':
        break
print("Fim")
