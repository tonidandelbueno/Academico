import random
cont=0
sorteado=random.randint(1,10)

while(cont <3):
    cont=cont+1
    n=int(input('Escolha um numero de 1 á 10:'))
    if(n==sorteado):
        print('Parabéns você acetou.')
    elif(n < sorteado):
        print('O numero sorteado é MAIOR.')
    elif(n> sorteado):
        print('O numero sorteado é MENOR.')
print('Acabou sua chance.')