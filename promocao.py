preco_original=float(input())
superior1k = preco_original - 1000
if preco_original < 500:
    preco_final = 0.8 * preco_original
elif preco_original < 1000:
    preco_final = 0.7 * preco_original
else:
    preco_final = (0.55 * superior1k) + (0.7 * (abs(preco_original - superior1k)))
    
print (round(preco_final,2))
