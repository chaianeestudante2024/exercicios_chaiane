nome = input("Insira seu nome: ")
while len(nome) < 3:
    print(f"O nome '{nome}' tem MENOS ❌ que 3 caracteres")
    nome = input("Insira seu nome novamente: ")
print(f"O nome '{nome}' tem MAIS ✅ que 3 caracteres")

idade = int(input("Insira a sua idade: "))
while idade < 0 or idade > 150:
    print(f"A idade {idade} NÃO ESTÁ ❌ entre 0 e 150")
    idade = int(input("Insira a sua idade novamente: "))
print(f"A idade {idade} ESTÁ ✅ entre 0 e 150")

salario = float(input("Insira seu salário: "))
while salario < 0:
    print(f"O salário {salario} ESTÁ MENOR ❌ QUE 0")
    salario = float(input("Insira seu salário novamente: "))
print(f"O salário {salario} ESTÁ MAIOR ✅ QUE 0")

estado_civil = input("Insira seu estado civil (s, c, v, d): ")
while estado_civil not in ["s", "c", "v", "d"]:
    print(f"O estado civil '{estado_civil}' NÃO ESTÁ ❌ entre os listados (s, c, v, d)")
    estado_civil = input("Insira seu estado civil novamente (s, c, v, d): ")
print(f"O estado civil '{estado_civil}' ESTÁ ✅ entre os listados")
