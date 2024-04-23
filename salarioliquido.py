#Salário líquido
horas=float(input('Insira o número de horas mensais trabalhadas (até 200): '))
extra=float(input('Insira o número de horas extras trabalhadas: '))
dinheiro1 = ((2500*horas)/200)
dinheiro2 = (2500*(1.2*extra))
bruto = (dinheiro1 + dinheiro2)
salario = (0.78*bruto)
print('Considerando que 22% do salário é gasto para IR e INSS, o salário líquido é de ', salario, ' reais.')



