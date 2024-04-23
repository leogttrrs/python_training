comprimento = float(input())
largura = float(input())
gavetas = int(input())
madeira = input()
m2 = comprimento*largura
preco = m2 * 100
preco += gavetas*30
if m2 > 2:
        preco += 50
if madeira == 'mogno':
    preco += 150
elif madeira == 'carvalho':
    preco += 125
if preco < 200:
    print(200)
else:
    print(f'{preco:.2f}')
