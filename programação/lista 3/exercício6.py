import random
from sys import implementation
v= input('Digite PAR ou IMPAR:')
n=int(input('Diguite um numero de 0 á 5:'))

s= random.randint (0,5)

t= (s+ n)
tt=( t % 2 )

if(v == 'p'or v== 'P' and tt==0):
    print('Voce ganhou, o numero sorteado foi', s)
else:
    print('A maquina ganhou,o numero sorteado foi', s)

if(v == 'i' or v=='I' and tt!=0 ):
    print('Voce ganhou, o numero sorteado foi', s)
else:
    print('A maquina ganhou,o numero sorteado foi', s)
    