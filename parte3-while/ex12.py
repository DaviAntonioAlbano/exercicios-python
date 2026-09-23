# Exercício 12 - Python
# Peça números ao usuário e vá somando. Quando ele digitar 0, pare e exiba a soma.

soma = 0
while True:
    num = int(input("Digite um número (0 para parar): "))
    if num == 0:
        break
    soma += num
print(f"A soma dos números digitados é: {soma}")