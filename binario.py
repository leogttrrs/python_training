def converter_binario (numero):
    conversao = ''
    if numero == 0:
        return '0'
    while numero > 0:
        if numero % 2 == 0:
            conversao += '0'
        else:
            conversao += '1'
        numero = numero//2
    return conversao[::-1]

valor = int(input())
print (converter_binario(valor))
