# Exercício 14 - Python
# Peça um número e exiba sua tabuada de 1 a 10.
num = int(input("Digite um número: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
    