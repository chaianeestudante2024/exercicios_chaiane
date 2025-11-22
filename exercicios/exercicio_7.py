# PROGRAMA QUE RECE 2 NÚMEROS INTEIROS:
# GERA OS NÚMEROS QUE ESTÃO NO INTERVALO ENTRE ELES:

num_int_1 = int(input("Insira o primeiro número int: "))
num1_int_1 = num_int_1 + 1
num_int_2 = int(input("Insira o segundo número int: "))
for numero in range(num1_int_1,num_int_2):
    print(f"{numero}")