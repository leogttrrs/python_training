sapo, vezes = [int(x) for x in input().split()]
resultado = 'YOU WIN'
alturas = [int(w) for w in input().split()]
for cano in range (len(alturas)-1):
    if abs(alturas[cano] - alturas[cano+1]) > sapo:
        resultado = 'GAME OVER'
        break
print(resultado)
