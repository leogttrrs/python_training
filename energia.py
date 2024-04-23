
consumo = int(input())

if consumo <= 30:
    preço = 0.09556 * consumo
elif consumo <= 100:
    preço = (30*0.09556) + (0.16698 * (consumo-30))
elif consumo <= 200:
    preço = ((30 * 0.09556) + (70 * 0.16698)) + (0.25052 * (consumo-100))
else:
    preço = ((30 * 0.09556) + (70 * 0.16698) + (100 * 0.25052)) + (0.27836 * (consumo-200))
print (round(preço,2))
    
