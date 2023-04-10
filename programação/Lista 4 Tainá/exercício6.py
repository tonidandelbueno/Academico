cont=0
opsao=''
n=int(input('Adicione um valor:'))

while opsao !='n':
    opsao=input('Deseja continualr s/n:')
    while(cont<10):
        cont=cont+1
        t=n*cont
        print(n, 'x', cont ,'=', t)

    if(opsao == 'n'):
        print('Você saio do programa.')
        
    