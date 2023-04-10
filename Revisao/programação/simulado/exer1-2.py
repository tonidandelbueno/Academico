from doctest import REPORTING_FLAGS


limite_1=int(input('Adicione um numero possitivo:'))
limite_2=int(input('Adicione outro numero possitivo:'))
multiplicador=int(input('Adicione outro numero possitivo:'))
t1=multiplicador*limite_1
t2=multiplicador*limite_2

if (t1>t2):
    print('[',t2,',',t1,']')
else:
    print('[',t1,',',t2,']')