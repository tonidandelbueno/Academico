cont=0
nome=''
sexo=''

while (cont <11):
    cont=cont+1
    nome=input('Adcione seu nome:')
    sexo=input('Informe seu sexo F/M:')
    idade=int (input('Adicione sue idade:'))
    if(sexo =='m'):
        print('Não está apto para concorrer.')
    elif(idade <=12 and idade >=1):
        print('Está apto a concorrer')
    elif(idade >59):
        print('Está apto a concorrer')
    else:
        print('Não está apto para concorrer')