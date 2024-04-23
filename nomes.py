nome = input()
nomes = nome.split()
contador = 0
nome_abreviado = ''
for palavra in nomes[1:-1]:
    contador += 1
    if len(palavra) > 3:
        nome_abreviado += (f'{palavra[0]}. ')
    else:
        nome_abreviado += (f'{palavra} ')
        
print(f'{nomes[0]} {nome_abreviado}{nomes[-1]}')