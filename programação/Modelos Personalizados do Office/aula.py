from operator import truediv
import random
n1= random.randint(1,10)
n2= int( input('Digite um nro de 1 a 10: '))
acertou = False
if(n1 == n2):
    acertou = True

print(acertou)
if (acertou == True):

    print('você acertou')
else:
    print(' voc~e errou')
    print ( 'o numero sorteado era ' , n1)
