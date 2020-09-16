"""
Those are type hints. Various type checkers can use them to determine if you're
using the correct types. In your example, you function is expecting ham of type str,
 and eggs of type str (defaulting to eggs). The final -> str implies that this
  function, should have a return type of str as well.

"""


"""
def cumprimentar(nome: str) -> str:
    return f"Ola {nome}"

print(cumprimentar("Gow"))
"""
#print("\n")


def cabe(texto: str, alinhamento: bool = True) -> str:
    if alinhamento:
        return f"{texto.title()}\n{'-'* len(texto)}"
    else:
        return f"{texto.title()}".center(50, '#')

print(cabe("Gow Dikson"))

print(cabe("Rodrigues dos Santos", False))

print(type(cabe("SouthPower")))


"""
Pra min esta aula não serve de absolutamente quase nada, Por que Quase :
 Só pra não dizer que eu nunca Vi isso, mas não serve pra nada.
"""
