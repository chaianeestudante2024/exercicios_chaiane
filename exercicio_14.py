#PROGRAMA QUE DETERMINE SE UM NÚMERO É OU NÃO UM NÚMERO PRIMO:

num_int = int(input("Insira o número que deseja saber se é primo ou não: "))

if num_int <1:
    print(f"O numero {num_int} não é um número primo")
else:
    for vezes in range(2,num_int):
        if num_int % 2 == 0:
            print(f"O número não é um {num_int} é primo")
            exit()
print(f"O número {num_int} é um  número primo")
