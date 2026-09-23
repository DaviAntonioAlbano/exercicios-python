# Exercício 25 - Python
# Dada a lista [3, 7, 1, 9, 4], exiba os itens na ordem inversa.

lista = [3, 7, 1, 9, 4]

for i in range(len(lista) - 1, -1, -1):
    print(lista[i])