notas = [float(x) for x in input().split()]
notas.remove(min(notas))
notas.remove(max(notas))
soma = 0
for nota in notas:
    soma += nota
print(f'{soma:.1f}')
