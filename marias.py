numero_de_nomes = int(input())
marias = 0
for i in range (numero_de_nomes):
    nome = input()
    if 'Maria ' in nome and 'Maria' == nome[-5:]:
        marias += nome.count('Maria ') + 1
    elif 'Maria ' in nome:
        marias += nome.count('Maria ')
    elif 'Maria' == nome [-5:]:
        marias += 1
print(marias)
