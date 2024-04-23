a='Ótimo'
b='Bom'
c='Satisfatório'
d='Insuficiente'
p1=float(input('p1: '))
p2=float(input('p2: '))
p3=float(input('p3: '))
naopode = p1 > 10 or p2 > 10 or p3 > 10
while naopode:
    print('Você inseriu uma nota maior que 10. Por favor, tente novamente')
    p1=float(input('p1: '))
    p2=float(input('p2: '))
    p3=float(input('p3: '))
    naopode = p1 > 10 or p2 > 10 or p3 > 10
    
nota = (p1 + p2 + p3) / 3
if nota >= 9:
    print(a)
elif nota >= 7.5:
    print(b)
elif nota >=6:
    print(c)
else:
    print(d)

