# Exercício 24 - Python
# Dada a lista [5, 12, 8, 20, 3, 15], informe quantos itens são maiores que 10.

lista = [5, 12, 8, 20, 3, 15]

maiores_que_10 = 0

for item in lista:
    if item > 10:
        maiores_que_10 += 1
print(f"Quantidade de itens maiores que 10: {maiores_que_10}")
