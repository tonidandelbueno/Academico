from operator import truediv


n= float(input('Adigite um valor: '))
t=( n % 2 )

if( t == 0):
    print('O nuemro ', n, 'é par.')
else:
    print('O numero ', n, 'é impar.')