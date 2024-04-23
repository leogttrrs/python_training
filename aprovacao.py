soma=0
reprovado = 0
for i in range (4):
    c = input()
    if c == 'A':
        c = 4
        soma += c
    elif c == 'B':
        c = 3
        soma +=c
    elif c == 'C':
        c = 2
        soma += c
    elif c == 'E':
        c = 0
    if c == 0:
        reprovado +=1
if soma/4 <3:
    aprovado = False
elif reprovado != 0:
    aprovado = False
else:
    aprovado = True
    
print(aprovado)

