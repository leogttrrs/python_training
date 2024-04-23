inicial= input('Secione a escala de temperatura inicial (k, c, f ou r): ')
temperatura = float(input('Selecione a temperatura na escala inicial: '))
final=input('Selecione a escala de temperatura para a qual deseja converter (k, c, f ou r): ')
ftor = temperatura + 459.67
rtof = temperatura - 459.67
ctok = temperatura + 273.15
ktoc = temperatura - 273.15
ctof = (temperatura*1.8 )+ 32
ftoc = (temperatura-32)/1.8
if inicial == 'c' :
    if final == 'k':
        temperatura = ctok
        print(temperatura)
    elif final == 'f':
        temperatura = ctof
        print(temperatura)
    elif final == 'c':
        print(temperatura)
    elif final =='r':
        temperatura = ctof + 459.67
        print(temperatura)
elif inicial == 'k':
    if final == 'c':
        temperatura = ktoc
        print(temperatura)
    elif final == 'f':
        temperatura = ktoc*1.8 + 32
        print(temperatura)
    elif final == 'k':
        print(temperatura)
    elif final == 'r':
        temperatura = ((ktoc*1.8 )+ 32 + 459.67)
        print(temperatura)
elif inicial == 'f':
    if final == 'c':
        temperatura = ftoc
        print(temperatura)
    elif final == 'k':
        temperatura = ftoc + 273.15
        print(temperatura)
    elif final == 'f':
        print(temperatura)
    elif final == 'r':
        temperatura = ftor
        print(temperatura)
elif inicial == 'r':
    if final =='c':
        temperatura = ((rtof-32)/1.8)
        print(temperatura)
    elif final =='f':
        temperatura = rtof
        print(temperatura)
    elif final == 'r':
        print(temperatura)
    elif final == 'k':
        temperatura = ((rtof-32)/1.8)+273.15
        print(temperatura)
    

