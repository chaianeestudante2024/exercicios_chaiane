#Programa que pede 10 numeros inteiros e mostra se são pares ou impares:
impar = 0
par = 0

for vezes in range(10):
    numero = int(input("Insira um número: "))

    if numero % 2 == 0:   # dentro do loop → verifica cada número
        par += 1
    else:
        impar += 1

print(f"\nHá {par} números pares")
print(f"Há {impar} números ímpares")
