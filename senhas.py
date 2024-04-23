senha = int(input())
valida = senha == 2002
while not valida:
    print('Senha Invalida')
    senha = int(input())
    valida = senha == 2002

print('Acesso permitido')
