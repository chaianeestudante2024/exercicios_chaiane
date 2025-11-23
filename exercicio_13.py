#PROGRAMA QUE CALCULA O FATORIAL DE UM NÚMERO:

numero = int(input("Insira um numéro para fazer fatorial: "))

fatorial = 1
for vezes in range(1, numero + 1):
    fatorial *= vezes


print(f"O fatorial do {numero} é {fatorial}")