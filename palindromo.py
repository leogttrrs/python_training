string = input()
teste = string.replace(' ', '')
teste2 = teste.replace(',', '')
teste3 = teste2.replace('-', '')
palindromo = teste3 == teste3[::-1]
print(palindromo)
