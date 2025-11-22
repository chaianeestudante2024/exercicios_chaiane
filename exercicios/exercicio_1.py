
#DIGITAR UM VALOR DE NOTA VÁLIDO:

valor = int(input("Digite uma nota entre 0-10: "))

while valor < 0 or valor > 10:
    print("O valor é inválido ❌")
    print("Insira um valor válido entre 0-10")
    valor = int(input("Digite uma nota entre 0-10: "))

else:
    print("O valor é válido ✅")
