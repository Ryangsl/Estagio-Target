
def fibonacci(numero):
    a, b = 0, 1

    while b <= numero:

        if b == numero:
            return True

        a, b = b, a + b

    return False


numero = int(input("Digite um número: "))
if fibonacci(numero):
    print(f"{numero} pertence à sequência de Fibonacci.")
else:
    print(f"{numero} não pertence à sequência de Fibonacci.")
