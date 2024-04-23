massa = float(input('Massa em gramas: '))
tempo = 0
while massa >= 0.5:
    tempo += 50
    massa = massa/2
print(tempo)
