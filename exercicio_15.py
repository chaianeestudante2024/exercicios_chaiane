#PROGRAMA QUE DETERMINE SE UM NÚMERO É OU NÃO UM NÚMERO PRIMO:

num_int = int(input("Insira o número que deseja saber se é primo ou não: "))

divisores = []
if num_int <1:
    print(f"O numero {num_int} não é um número primo")
else:
    for vezes in range(2,num_int):
        if num_int % vezes == 0:
            divisores.append(vezes)


    if len(divisores) == 0:
        print(f"O número {num_int} é primo")
    else:
        print(f"O número {num_int} não é primo")
        print(f"Ele é divisível por: {divisores}")