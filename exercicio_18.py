Pessoa_l = []
Idade_l = []

quantidade = int(input("Quantas pessoas você quer cadastrar? "))

for i in range(1, quantidade +1):
    pessoa = input(f"Digite o nome da pessoa {i}: ")
    idade = int(input(f"Digite a idade da pessoa {i}: "))

    Pessoa_l.append(pessoa)
    Idade_l.append(idade)

media = sum(Idade_l) / len(Pessoa_l)
print(f"A média de idades é de {media}")

if media ==0 or media <=25:
    print("A turma é jovem")
elif media >=26 or media <=60:
    print("A turma é Idosa")
else:
    print("A turma é Idosa")



