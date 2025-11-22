#GERADOR DE TABUADA
#GERA A TABUADA DE QUALQUER NÚMERO INTEIRO:

#Pergunta ao usúario:
num_tabuada = int(input("Insira o número que deseja ver a tabuada: "))

#Título:
print(f"Tabuada de {num_tabuada}:")

#Contas:
for num in range(1,11):
    conta_1 = num_tabuada * num
    print(f"{num_tabuada} * {num} = {conta_1}")
