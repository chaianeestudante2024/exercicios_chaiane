n = int(input("Insira o valor de n"))

def fibonacci(n):
    serie = []
    a, b = 1, 1
    for _ in range(n):
        serie.append(a)
        a, b = b, a + b
    return serie

serie = fibonacci(n)
print("A seríe  é",serie)
print(f"A seríe foi até o {n} termo que é {serie[-1]}")
