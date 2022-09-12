# Cria uma lista sem nenhum elemento.

# A expressão lista_vazia = list() possui o mesmo efeito.

lista_vazia = []
print("Lista vazia: ", lista_vazia)
print("Tipo de uma lista: ", type(lista_vazia))

lista_inteiros = [10, 20, 30, 40]
print("Lista de inteiros: ", lista_inteiros)

lista_tipos_diferentes = ["George", "Orwell", 1984]
print("Lista de elementos com tipos diferentes: ", lista_tipos_diferentes)

lista_aninhada = [1, [2, [3, [4]]], 5]
print("Lista aninhada: ", lista_aninhada)

matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Matriz 3x3: ", matriz)

# A sintaxe abaixo será explicada posteriormente.
print("Matriz impressa de outra forma:")
for lista in matriz:
    for elemento in lista:
        print(elemento, end=' ')
    print()
    
#percorrendo lista


# Sintaxe da função range().

inicio = 0
fim = 100
passo = 10

# Convertendo um intervalo em uma lista.
print(list(range(inicio, fim, passo)))


# Ordenando listas.
lista = [7, 25, 2, 3, 30, 7, 80, 100, -1, 15]
print("Lista não ordenada: ", lista)

lista.sort()
print("Lista ordenada: ", lista)

lista.sort(reverse=True)
print("Lista ordenada em ordem decrescente: ", lista)



# Ordenando listas.
lista = [7, 2, 3, 7, -1, 9]
print("Lista original antes da ordenação: ", lista)

lista_ordenada = sorted(lista)
print("Lista ordenada: ", lista_ordenada)

print("A lista original permanece inalterada: ", lista)

#modificando lista

# Cria uma lista vazia.
lista = []

print("Lista vazia", lista)

# Adiciona elementos no final da lista.
lista.append("P")
lista.append("Y")
lista.append("T")
lista.append("H")
lista.append("O")
lista.append("N")

print(lista)

lista.insert(1,"y")
lista.insert(4,"o")
print(lista)
lista.remove("O")
print(lista)

del lista[1]
print("removendo um elemento", lista)


# agora criando uma lista dentro no for 
frutas = ['laranja', 'banana', 'abacate', 'manga']
plurais_frutas = []
for fruta in frutas:
    plural = fruta + 's'
    plurais_frutas += [plural]
print(plurais_frutas)



# Converte uma string em uma lista.
s = list("Ordem e Progresso")
print(s)

# Converte uma lista em uma string.
l = ['O', 'r', 'd', 'e', 'm', ' ', 'e', ' ', 'P', 'r', 'o', 'g', 'r', 'e', 's', 's', 'o']
print(''.join(l))

