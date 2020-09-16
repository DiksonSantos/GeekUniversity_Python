def comer(comida, saudavel):
    if saudavel:
        final = 'quero manter a forma.'
    else:
        final = 'Só se vive uma vez'

    return f'Estou comendo {comida} porque {final}'


def dormir(horas):
    if horas > 8:
        return f'Fico Mau Dormindo {horas} Um tanto desses'
    else:
        return f'Continuo Cansado Apos dormir por apenas {horas} horas'



def eh_funny(pessoa):
    comediants = ['Jim Carey', 'Paulinho Gogó', 'Matheus Ceara', 'Batoré']
    if pessoa in comediants:
        return True
    else:
    #Qualquer Outra pessoa que NÃO esteja na Lista, -> resultado vai ser False.
        return False

"""
Pessoa = eh_funny('Jim ')
print(Pessoa)
"""
