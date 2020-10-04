from importlib import metadata

print(metadata)


metadata_pip = metadata.metadata('pip')

"""Mostra todos os dados de PIP como se fosse a TAG de um MP3"""
#print(metadata_pip)

#print(list(metadata_pip))

#Pegando a Metadata de Apenas Um dos itens de PIP:
#print(metadata_pip['Project-URL']) #Mostra um link c/ site do Projeto

print(len(metadata_pip))
print(len(metadata.files('pip')))# 472 Pacotes.

print(len(metadata.files('django'))) #4.347 Pacotes
print(metadata.requires('Django')) #Mostra o que o Django Requer.
