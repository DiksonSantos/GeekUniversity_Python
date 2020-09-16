def cabe(texto: str, alinhamento: bool = True) -> str:   # O 'mypy' Só Funciona com estas sintaxes.
    if alinhamento:
        return f"{texto.title()}\n{'-'* len(texto)}"
    else:
        return f"{texto.title()}".center(50, '#')

print(cabe("Gow Dikson"))

print(cabe("Gow Santos", alinhamento=False))
#O Comando mypy NomeDoArquivo.py Apontou um erro na linha 11 quando usei uma String ao invés de True:
print(cabe("Dikson Santos", alinhamento=True))#160_Tipos_De_Dados_Com_MyPy.py:11: error: Argument "alinhamento" ...

#  CTRL  /   -> Comenta todas as linhas selecionadas.

