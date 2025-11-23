#Programa que mostra todos os números primos entre 1 e N:


Divisores = []
Primos = []
NPrimos = []

N = int(input("Insira um número inteiro: "))

for Numero in range(2, N + 1):
    Divisores = []

    for vezes in range(1, Numero + 1):
        if Numero % vezes == 0:
            Divisores.append(vezes)


    if len(Divisores) == 2:
        Primos.append(Numero)
    else:
        NPrimos.append(Numero)

print(f"Números primos até {N}: {Primos}")
print(f"Números não primos até {N}: {NPrimos}")


