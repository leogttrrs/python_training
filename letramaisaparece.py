frase = input()
frase = frase.replace(' ','')
contadormaior = 0
alfabeto = 'abcdefghijklmnopqrstuvwxyz'
for letter in alfabeto:
    if frase.count(letter) > contadormaior:
        maior_ocorrencia = letter
        contadormaior = frase.count(letter)
print(maior_ocorrencia)
