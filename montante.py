capital=float(input('Insira o valor inical de capital: '))
meses=float(input('Insira o número de meses em que a taxa vai ser aplicada sobre o capital: '))
taxa=float(input('Insira um numero de 0 a 100 para representar a porcentagem da taxa de juros compostos: '))
resultado = round(((capital)*((1+ taxa/100))**meses))
print('O resultado aproximado do montante é ',resultado, ' reais.')