
#PROGRAMA QUE PEDE DOIS NÚMEROS:
base_1 = int(input("Insira o primeiro número que será a base: "))
expoente_2 = int(input("Insira o primeiro número que será o expoente: "))

resultado = 1

for contador in range(expoente_2):
    resultado *= base_1

print(f"O resultado será {resultado}")