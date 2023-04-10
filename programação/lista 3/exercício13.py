from cgi import print_form
from operator import truediv


gA= float( input('Digite o valor do Gral A:'))
gB= float( input('Digite o valor do Gral B:'))
ta= (gA * 1 /3)
tb= (gB * 2 /3)
tt= ( ta+tb)

if(tt >= 6 ):
     print('Parabens você foi aprovado com a medía', tt)
else:
     print('você não foi aprovado pois sua media foi:', tt)

     x=input('gostaria de subistituir o gral A ou o gral B: ')
     gC =float( input('Digite o valor do Gral C:'))
     tcb=(gC * 1 /3 + tb)    
     tca=(ta + gC *2/3)

     if(x == 'a' or x=='A'):

          if (tcb >= 6):
               print('Parabens você foi aprovado com a medía', tcb)
          else:
               print('você não foi aprovado pois sua media foi:', tcb)

     if(x=='b' or x=='B'):
          if(tcb >= 6):
               print('Parabens você foi aprovado com a medía', tca)
          else:
               print('você não foi aprovado pois sua media foi:', tca)