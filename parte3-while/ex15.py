# Exercício 15 - Python
# Peça números ao usuário até que ele digite 0. Ao final, informe quantos números positivos foram digitados.

positivos = 0
while True:
    num = int(input("Digite um número (0 para parar): "))
    if num == 0:
        break
    if num > 0:
        positivos += 1