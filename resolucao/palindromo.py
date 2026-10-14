# Descrição: Testa se uma palavra é um palíndromo.


def eh_palindromo(palavra):
	palavra = "".join(caractere.lower() for caractere in palavra if caractere.isalnum())
	return palavra == palavra[::-1]



palavra = input("Digite uma palavra: ")
if eh_palindromo(palavra):
    print("É um palíndromo.")
else:
    print("Não é um palíndromo.")

