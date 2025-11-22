#PROGRAMA DE CALCULAR ATÉ QUANTOS ANOS A POPULAÇÃO DE A CHEGA EM B:

populacao_a = int(input("Insira o valor da população A: "))
populacao_b = int(input("Insira o valor da população B: "))
taxa_a = float(input("Insira o valor da taxa de crescimento A: "))
taxa_b = float(input("Insira o valor da taxa de crescimento B  "))
anos = 0

while populacao_a < populacao_b:
    populacao_a = populacao_a + (populacao_a * taxa_a)
    populacao_b = populacao_b  + (populacao_b * taxa_b)
    anos += 1

print(f"A população A {populacao_a} ultrapassou ou igualou a população B {populacao_b}")
print(f"Levou {anos} anos para a população A chegar ao nível da população B")