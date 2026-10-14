# 3 - Operações Matemáticas Simples 📐
# Descrição: Vamos solicitar como entrada dois números e depois vamos realizar uma operação simples entre eles.

print("Escolha a operação:")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

operacao = input("Digite o número da operação desejada: ")

if operacao in ("1", "2", "3", "4"):
	numero1 = float(input("Digite o primeiro número: "))
	numero2 = float(input("Digite o segundo número: "))

	if operacao == "1":
		print(f"Soma: {numero1 + numero2}")
	elif operacao == "2":
		print(f"Subtração: {abs(numero1 - numero2)}")
	elif operacao == "3":
		print(f"Multiplicação: {numero1 * numero2}")
	elif numero2 != 0:
		print(f"Divisão: {numero1 / numero2}")
	else:
		print("Divisão: não é possível dividir por zero.")
else:
	print("Opção inválida. Escolha uma opção de 1 a 4.")
