populacao_a = 80000
populacao_b = 200000
taxa_a = 0.03
taxa_b = 0.01
anos = 0

while populacao_a < populacao_b:
    populacao_a = populacao_a + (populacao_a * taxa_a)
    populacao_b = populacao_b  + (populacao_b * taxa_b)
    anos += 1

print(f"A população A {populacao_a} ultrapassou ou igualou a população B {populacao_b}")
print(f"Levou {anos} anos para a população A chegar ao nível da população B")