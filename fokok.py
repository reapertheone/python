celsius=input('Add meg a homersekletet celsiusban\n')
to=input('Mibe szeretned atvaltani?\n(F)ahrenheit/(K)elvin\n')

C=int(celsius)
F=C*18/10+32
K=C+273

if to=='F'or to=='f':
    print(F)
elif to=='K'or to=='k':
    print(K)
else:
    print('nem tudom ertelmezni')