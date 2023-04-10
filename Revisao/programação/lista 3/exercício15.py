n=float(input('Adicione o valor da sua compra:'))
print('1 - À vista em dinheiro.')
print('2 - À vista no cartão de crédito.')
print('3 - Em duas vezes')
print('4 - Em três vezes,')
x=int (input('Adicione o numero referent a opsão:'))
t1=(n *15/100)
t2=( n*10/100)
t4=(n + t2)

if(x == 1):
    ta= (n - t1)
    print('sua compra vai ser de R$', ta)
elif(x== 2):
    tb=(n-t2)
    print('sua compra vai ser de R$', tb)
elif(x== 3):
    t3=(n/2)
    print('sua compra vai ser duas vezes de R$', t3)
elif(x== 4):
    tc=(t4/3)
    print('sua compra vai ser tres vezes de R$', tc)
elif(x!= 1 and x!= 2 and x!= 3 and x!= 4):
    print('Não tem essa opsão.')