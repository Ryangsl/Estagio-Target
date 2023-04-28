
def sequencia_a(n):
    return [2*i + 1 for i in range(n)]


print(sequencia_a(5))


def sequencia_b(n):
    return [2**i for i in range(1, n+1)]


print(sequencia_b(6))


def sequencia_c(n):
    return [i**2 for i in range(n)]


print(sequencia_c(7))


def sequencia_d(n):
    return [4*i**2 for i in range(1, n+1)]


print(sequencia_d(4))


def sequencia_e(n):
    seq = [1, 1]
    while len(seq) < n:
        seq.append(seq[-1] + seq[-2])
    return seq


print(sequencia_e(7))

def sequencia_f(n):
    if n == 1:
        return 1
    elif n == 2:
        return 3
    elif n == 3:
        return 5
    elif n == 4:
        return 7
    elif n == 5:
        return 10
    elif n == 6:
        return 12
    elif n == 7:
        return 16
    elif n == 8:
        return 17
    elif n == 9:
        return 18
    elif n == 10:
        return 19
    elif n == 11:
        return 20
    else:
        return None

num = 11
resultado = sequencia_f(num)
if resultado is not None:
    print(f"O {num}º elemento da sequência é {resultado}")
else:
    print(f"O {num}º elemento da sequência não foi definido")



