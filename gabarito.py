resposta = input()
gabarito = input()
acertos = 0
contador = 0
while contador < len(resposta):
    if resposta[contador] == gabarito[contador]:
        acertos += 1
    contador += 1
print(acertos)
