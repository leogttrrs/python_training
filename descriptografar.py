alfabeto = input().lower()
alfabeto_cifragem = input().lower()
senha = {}
indice = 0
for letra in alfabeto_cifragem:
    senha[letra] = alfabeto[indice]
    indice += 1
frase = input().lower()
frase_descriptografada = ''
for letter in frase:
    if letter in senha:
        frase_descriptografada += senha[letter]
    else:
        frase_descriptografada += letter
print(frase_descriptografada)
