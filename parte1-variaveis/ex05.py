# Exercício 05 - Python
# peça o preço de um produto e a quantidade comrpada. Exiba o valor total, com duas casas decimais.

preco = float(input("Digite o preço do produto: "))
quantidade = int(input("Digite a quantidade comprada: "))

valor_total = preco * quantidade
print("O valor total da compra é: R$", format(valor_total, ".2f"))
