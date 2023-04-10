import random

input('Vamos jogar dado.')
n=int(input('Escolha a face do daddo de 4,6,8,10,12 e 16: '))

if (n == 4):
    d4= random.randint (1, 4)
    print('O numero sorteado foi ', d4)
elif(n == 6):
    d6= random.randint (1, 6)
    print('O numero sorteado foi ', d6)
elif(n==8):
    d8= random.randint(1, 8)
    print('O numero sorteado foi ', d8)
elif(n==10):
    d10=random.randint (1, 10)
    print('O numero sorteado foi ', d10)
elif(n==12):
    d12= random.randint (1, 12)
    print('O numero sorteado foi ', d12)
elif(n==16):
    d16=random.randint(1, 16)
    print('O numero sorteado foi ', d16)