"""
São todos os metodos que usam o Dunder __
->    __init__

"""

"""
    def __repr__(self):
#Estamos Sobrescrevendo a Função interna que mostraria o endereço de memoria <__main__.Livro object at 0x7f5026b31588>
#Trocando esta funcionalidade por esta aqui que Devolve a Var Local titulo.
        '''Com esta Função ele simplesmente mostra o titulo e não aquele endereço de memoria'''
        print(f'Quantidade de páginas: {self.paginas}')
        return self.titulo
"""

class Livro:

    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __str__(self):
        '''Faz o mesmo que a __repr__  aparentemente PORÉM, __str__ TEM PRIORIDADE
        SE HOUVER OS DOIS METODOS NA CLASSE, O __str__ VAI SER USADO E NÃO O __repr__'''
        #print(f'{self.titulo}')
        #return f'{self.paginas}'
        return self.titulo

    def __repr__(self):
#Estamos Sobrescrevendo a Função interna que mostraria o endereço de memoria <__main__.Livro object at 0x7f5026b31588>
#Trocando esta funcionalidade por esta aqui que Devolve a Var Local titulo.
        '''Com esta Função ele simplesmente mostra o titulo e não aquele endereço de memoria'''
        #print(f'Quantidade de páginas: {self.paginas}')
        return f'{self.titulo}, Escrito Por {self.autor}'

    def __len__(self):
        '''Definindo ou Re-escrevendo que LEN dentro desta Classe vai contar o numero de páginas.
        Se tentasse usa-lo sem re-escreve-lo, não daria certo.'''
        #print(self.paginas)
        return len(self.titulo)

    def __del__(self):
        '''Ao meu ver Esta função não serve para NADA'''
        print('Um Objeto do tipo Livro foi deletado da memoria')


    def __add__(self, outro):
        '''Esta sobrescrição possibilita Juntar Dois *Livros* , pois naturalmente o Python
        Só junta numeros ou duas Strings etc..., mas não Dois Objetos'''
        return f'{self} - {outro}'

    #                Outro no caso é o Numero de Vezes a ser multiplicado o Objeto Livro (Neste Caso).
    def __mul__(self, Outro):
        '''Se o Outro for inteiro OK
        Esta função serve para meramente multiplicar o titulo do livro'''
        if isinstance(Outro, int):
            msg = ' '
            for N in range(Outro): #Dependendo do valor de Outro, é o numero de 'voltas' que o FOR vai dar.
                msg += ' ' +str(self)# O Self é o Livro, e esta sendo convertido para String para poder ser Multiplicado.
            return msg
        return 'Não Posso Multiplicar' #Se o'Outro' Não for Inteiro...

Livro1 = Livro('Memorias de Um Sarg de Mil', 'Dom Casmurro', 400)
print(Livro1) # Sem a função __repr__   -> <__main__.Livro object at 0x7f5026b31588>

IL2 = Livro('Python on a Crach Course', 'Guido Von ROssun', 650)
print(IL2)

#print(len(Livro1))
#del Livro1 #Se deletar o Livro Um aqui, Daqui pra baixo Cracha tudo.

print(len(Livro1))
print(len(IL2), 'ggg')

#Usando o ADD
print(Livro1 + IL2, 'Aqui')

print(IL2 * 5)
