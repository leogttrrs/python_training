
n = int(input())
inicial = 1
inicial2 = 1
soma = inicial + inicial2
for i in range (n):
    fibonacci = soma
    inicial = inicial2
    inicial2 = soma
    soma = inicial + inicial2
print(fibonacci-inicial)
    
