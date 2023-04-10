print('             MENU')
print('1- Converter de Real para Euro')
print('2- Converter de Real para Dólar')
print('3- Converter de Euro para Dólar')
print('4- Converter de Euro para Real')
print('5- Converter de Dólar para Euro')
print('6- Converter de Dólar para Real')
n=int (input('Adicione o numero referent a opsão:'))
x=float(input('Adicione o valor:'))

if(n==1):
    e=float(input('Quanto que está valendo o Euro? '))
    t1=(x/e)
    print('O valor é', t1)

elif(n==2):
    d=float(input('Quanto que está valendo o  Dólar?'))
    t2=(x/d)
    print('O valor é', t2)

elif(n==3):
    d=float(input('Quanto que está valendo o  Dólar?'))
    t3=(x/d)
    print('O valor é', t3)

elif(n==4):
    r=float(input('Quanto que está valendo o  Real?'))
    t4=(x/r)
    print('O valor é', t4)

elif(n==5):
    e=float(input('Quanto que está valendo o Euro? '))
    t5=(x*e)
    print('O valor é', t5)

elif(n==6):
    r=float(input('Quanto que está valendo o  Real?'))
    t6=(x*r)
    print('O valor é', t6) 