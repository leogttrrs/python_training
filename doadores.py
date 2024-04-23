num_calouros = int(input())
calouros = set()
iguais = 0
for calouro in range (num_calouros):
    calouros.add(input())

num_doadores = int(input())
doadores= set()
for i in range(num_doadores):
    doador = input()
    if doador in calouros:
        iguais += 1
    doadores.add(doador)

porcentagem = iguais/num_calouros
print(porcentagem)

