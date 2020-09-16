
#Sequencia de fibonacci -> 1, (1, 2) =, (3, {5),= 8}, = 13

#Solução Comum Para Lista de Fibonacci: (No teste usou 449MBs)
def fib_lista(max):
    nums = []
    a, b = 0, 1
    while len(nums) < max:
        nums.append(b)
        a, b = b, a + b
    return nums

#for N in fib_lista(100):
#    print(N)


#Usando Yeld Para Calculo Fibonacci:  (GERADORES)   (No teste Usou 3MBs)
def yfib_gen(max):
    a, b, contador = 0, 1, 0
    while contador < max:
        a, b, = b, a + b
        yield a
        contador += 1

for N in yfib_gen(100):
    print(N)
