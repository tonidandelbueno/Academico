n= float(input('Digite o valor da compra:'))


if (n <= 20.00):
    val1= (n * 45 / 100)
    t=(n + val1)
    print('Valor que vai vender é' , t)

elif (n >20 and n <= 50.00):
    val2= (n * 35 / 100)
    tt=(n + val2)
    print('Valor que vai vender é' , tt)

elif( n > 50.00):
    val3= (n * 25 / 100)
    ttt=(n+ val3)
    print('Valor que vai vender é' , ttt)