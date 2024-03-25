def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input("Digite um número inteiro:"))
resultado = fibonacci(n)

print(f"O {n}-ésimo termo da sequência de Fibonacci é {resultado}.")

