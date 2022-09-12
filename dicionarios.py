# O comando dicionario_vazio = dict() possui o mesmo efeito do comando abaixo.
dicionario_vazio = {}
print("Dicionário vazio: ", dicionario_vazio)

paises = {'BRA': 'Brasil', 'EUA': 'Estados Unidos', 'FRA': 'França'}
print("Exemplo de dicionário: ", paises)

print("Tipo de um dicionário: ", type(paises))

# Modificando um dicionário.
paises["BRA"] = "Brazil"
paises["FRA"] = "France"

# Adicionando um elemento.
paises["ESP"] = "Espanha"

print("Dicionário modificado: ", paises)

#pesquisando valores em discionarios

print("EUA: ", paises['EUA'])


#vejamos agora como percorrer pares chave-valor em um discionario


paises = {'BRA': 'Brasil', 'EUA': 'Estados Unidos', 'FRA': 'França', 'ESP': 'Espanha'}
for chave, valor in paises.items():
    print(chave + " = " + str(valor))
