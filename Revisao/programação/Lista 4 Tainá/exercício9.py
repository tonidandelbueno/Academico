
cont=0
fim=True

while(fim):
    nome=input('Nome:')
    
    if(nome =='fim'):
        print('O número de advogadas ou advogados é', cont)
        fim=False

    if(nome != 'fim'):
        profissão=input('profissão:')

    if(profissão== 'advogado' or profissão=='advogada'):
        cont=cont+1
       