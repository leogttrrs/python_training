def fatorial (valor):
    total = 1
    while valor >= 2:
        total *= valor
        valor -= 1
    return total
n = int(input())
print (fatorial(n))
