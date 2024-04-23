def eh_primo(n):
    if n <= 1:
        return False
    for teste in range(2, int(n ** 0.5) + 1):
        if n % teste == 0:
            return False
    return True

inicio = int(input())
fim = int(input())
quantidade = 0

for i in range(inicio, fim+1):
    if eh_primo(i):
        quantidade += 1

print(quantidade)
