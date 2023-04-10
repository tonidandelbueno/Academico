
aluno=int(input('Quantos alunos quer ver a media? '))
for n in range (aluno):
    a=float(input('Adicione a nota do grau A:'))
    b=float(input('Adicione a nota do grau B:'))
    ta=a*1/3
    tb=b*2/3
    tab=ta+tb
    if(tab>=6):
        print('PARABÉNS, você foi aprovado(a). Nota media:',tab)
    else:
        print('Você foi REPROVADO. Nota media:', tab)
        x=input('Quer substituír a nota do grau A ou B? ')
        c=float(input('Adicione a nota do grau C:'))
        tccb=c*1/3
        tcca=c*2/3
        tbc=tb+tccb
        tac=ta+tcca
    if(x == 'A'or x=='a'):
        if tbc>=6:
            print('PARABÉNS, você foi aprovado(a). Nota media:',tbc)
        else:
            print('Você foi REPROVADO. Nota media:',tbc)
    elif(x=='b'or x=='B'):
        if tac>=6:
            print('PARABÉNS, você foi aprovado(a). Nota media:',tac)
        else:
            print('Você foi REPROVADO. Nota media:',tac)
