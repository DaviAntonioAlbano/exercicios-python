# Exercício 09 - Python.
# # Peça a média de um estudante e classifique: 6 ou mais é Aprovado; de 4 a 5,9 é Recuperação; abaixo de 4 é Reprovado.

media = float(input("Digite a média do estudante: "))

if media >= 6:
    print("O estudante está aprovado.")
elif media >= 4:
    print("O estudante está em recuperação.")
else:
    print("O estudante está reprovado.")