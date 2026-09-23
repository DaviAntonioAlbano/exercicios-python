# Exercício 10 - Python
# Peça a idade de uma pessoa e informe se ela já pode votar. A idade mínima é 16 anos.

idade = int(input("Digite a idade da pessoa: "))
if idade >= 16:
    print("Você já pode votar.")
else:
    print(" Você ainda não pode votar.")