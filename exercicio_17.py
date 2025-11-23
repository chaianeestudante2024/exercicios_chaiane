
N = int(input("Digite a quantidade de notas: "))

soma = 0

for vezes in range(N):
    nota = float(input(f"Digite a nota {vezes + 1}: "))
    soma += nota

# Calcula a média depois do loop
media = soma / N

print(f"A média aritmética das {N} notas é: {media}")
