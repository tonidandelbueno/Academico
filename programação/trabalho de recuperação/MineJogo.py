import random
def dado(): #contador da roleta
    input('RODE A ROLETA!')
    x = random.randint(1,6)
    print('A roleta parou no',x)
    return x

def ehPrimo (n): #numero primo
    primo = True
    for i in range (2,n):
        if (n%i==0):
            primo=False
    return primo


rodada=0
vencer= False
perder=False
j1casa=0
J1filho=0
J1casar=False
J1formou=''
J1loteria=0
J1famoso= False
j1divorsio=False

j2casa=0
J2filho=0
J2casar=False
J2formou=''
J2loteria=0
J2famoso= False
j1status= 0
j2status= 0
j2divorsio=False



while (vencer == False and perder == False):
    rodada = rodada + 1
    print('rodada', rodada, '\n' )

    if j1status==0:

        j1casa = j1casa + dado()
        print('\nJOGADOR 1 CASA:', j1casa)

    
    
    #------------- Executando a Regra do Dado -------------------------------------------------------------------------

        if j1casa == 1 or j1casa == 3 or j1casa == 10 or j1casa == 17:
            print('\n OPSSS!\nRode novamento a roleta!!!!\nSe parar no (1) avance 1 casa;\nSe parar no (3) volte 1 casa.\nSe parar no (6) perde uma rodada.\n')
            casadado = dado()
            if casadado == 1:
                j1casa= j1casa + 1
                print('\nAvance 1 casa\n')
            elif casadado == 3:
                j1casa= j1casa - 1
                print('\nVolte 1 casa\n')
            elif casadado==6:
                j1status=j1status+2
                print('\nFique 1 rodada sem jogar\n')
    #-------------- Executando a Regra Morrer -------------------------------------------------------------------------
        if j1casa == 2 or j1casa == 8 or j1casa == 18:
            perder = True
            print ('\nVocê foi morto por justa causa. \n Game Over para Você!!\n')
            # Extrato da sua vdida
            print('\nEXTRATO\n')
            if J1casar == True:
                print('---Se casou')
            if j1divorsio==True:
                print('---Você se separou')
            if J1famoso == True:
                print('---Você ficou famoso')
            print('---Teve',J1filho,'filhos(as)')
            print('---Se formou em',J1formou)
            print('---Você ganhou na loteria R$',J1loteria)
            
    #---------------Executando a Regra Vencer---------------------------------------------------------------------------
        if j1casa >=21:
            vencer = True
            print('\nPARABÉNS! Você venceu.\n''\nFIM!!!!\n')
            
            print('\nEXTRATO\n')
            if j1casar == True:
                print('---Se casou')
            if j1divorsio==True:
                print('---Você se separou')
            if J1famoso == True:
                print('---Você ficou famoso')
            print('---Teve',J1filho,'filhos(as)')
            print('---Se formou em',j1formou)
            print('---Você ganhou na loteria R$',J1loteria)
    #---------------Executando a Regra de Voltar ao início--------------------------------------------------------------            
        if j1casa == 20:
            j1casa=0
            print('\nVolte para o início!!!!!!!\n')
    #----------------- Executando a Regra de SE FORMAR ---------------------------------------------------           
        if j1casa == 5:
            print('EBA! Você se formou.\nGire a roleta novamente para vermos no que se formou.\n')
            casadado=dado()
            
            if casadado == 1:
                print('\nAdvogado')
                j1formou = 'Advogado'
                
            elif casadado == 2:
                print('\nMedicina')
                j1formou = 'Medicina'
                
            elif casadado == 3:
                print('\nJogos Digitais')
                j1formou = 'Jogos Digitais'
                
            elif casadado == 4:
                print('\nSegurança de Informação')
                j1formou = 'Segurança de Informação'
                
            elif casadado == 5:
                print('\nEducação Fisica')
                j1formou = 'Educação Fisica'
                
            elif casadado == 6:
                print('\nAdministração')
                j1formou = 'Administração'
                
    #----------------- Executando a Regra de FILHO ---------------------------------------------------
        if j1casa == 6 or j1casa == 9 or j1casa == 13:
            print('\nEita!!!\nVocê teve um filho, Rode a roleta novamente.\nMas se parar no 5 vixxxxxxx GANHO GÊMEOS!\nBOA SORTE!\n')
            casadado = dado()

            if casadado == 5:
                J1filho = J1filho + 2
                print('\nTeve GÊMEOS!\n')
            else:
                J1filho = J1filho + 1
                print('\nTeve apenas 1 filho!\n')
    #----------------- Executando a Regra de CASAR ---------------------------------------------------
        if j1casa == 7 or j1casa == 16:
            print('\nVocê se casou\nPARABÉNS aos ponbinhos')
            j1casar = True
        if j1casa == 12:
            if casar ==True:
                print('\nVocê deixou a toalha molhada na cama\nCom essa atidude ocasiono uma separação.\n')
                j1casar = False
                j1divorsio=True
    #----------------- Executando a Regra de LOTERIA ---------------------------------------------------
        if j1casa== 14:
            print('\nVocê ganhou na loteria!!\nRode a roleta para vermos quanto ganhou.\n')
            casadado=dado()
            
            if casadado== 1:
                print('\nVocê ganhou R$ 2,50')
                j1loteria = 2.50
            elif casadado == 2:
                print('\nVocê ganhou R$5.000,00')
                j1loteria = 5000.00
            elif casadado == 3:
                print('\nVocê ganhou R$50.000,00')
                j1loteria = 50000.00
            elif casadado == 4:
                print('\nVocê ganhou R$500.000,00')
                j1loteria = 500000.00 
            elif casadado == 5:
                print('\nVocê ganhou R$5.000.000,00')
                j1loteria = 5000000.00
            elif casadado == 6:
                print('\nVocê ganhou R$100.000.000,00')
                j1loteria = 100000000.00
    #----------------- Executando a Regra de FAMOSO ---------------------------------------------------
        if j1casa == 15:
            print('\nOLHA SÓÓÓÓÓÓÓ!!!\nVocê ficou FAMOSO!.\nFIU!FIUUUUUU!\n')
            j1famoso=True
    #----------------- Executando a Regra de MATEMATICA ---------------------------------------------------
        if j1casa == 4 or j1casa == 11 or j1casa == 19:
            print('\nDesafio!!!\nRode novamente a roleta para vermos o que sai.\n')
            casadado = dado()
            if casadado ==1:
                print('\nNumeros primos até 100:\n')
                for i in range(2,101):
                    x=ehPrimo(i)
                    if x == True:
                        print(i)
                
            elif casadado == 2:
                print('\nSomatorio de 1 até 10')
                soma=1+2+3+4+5+6+7+8+9+10
                print('\nO resultado do Somatorio é',soma,'\n')
                
            elif casadado == 3: 
                print('\nSérie de Fibonacci até o décimo elemento\n')
                t1=0
                t2=1
                cont=3
                print(t1)
                print(t2)
                while(cont<=10):
                    t3=t1+t2
                    t1=t2
                    t2=t3
                    cont+=1
                    print(t3)
                
            elif casadado == 4:
                print('\nA área de um circulo de raio 2,5\n')
                circulo= 3.142 * (2.5 * 2)
                print('\nÁrea = π . r2\n3,142 . 2,5²\nO resultado',circulo,'cm\n')
                
                
            elif casadado == 5:
                print('\nFatorial de 5\n')
                fatorial5=5*4*3*2*1
                
                print('\nO fatorial de 5 é',fatorial5,'\n')
                
            elif casadado == 6:
                print('\n5 primeiros numeros divisivel por 2 e 5\n')
                
                print('\n(5) primeiros numeros divisiveis por 2\n')
                
                for i in range(2,11,2):
                    print('\n',i)
                    
                print('\n(5) primeiros numeros divisiveis por 5\n')
                
                for e in range (5,30,5):
                    print('\n',e)



#=======================JOGADOR 2 =========================================================================
    if j2status==0:
        j2casa = j2casa + dado()
        print('\nJOGADOR 2 CASA:', j2casa)

    #------------- Executando a Regra do Dado -------------------------------------------------------------------------

        if j2casa == 1 or j2casa == 3 or j2casa == 10 or j2casa == 17:
            print('\n OPSSS!\nRode novamento a roleta!!!!\nSe parar no (1) avance 1 casa;\nSe parar no (3) volte 1 casa.\nSe parar no (6) perde uma rodada.\n')
            casadado = dado()
            if casadado == 1:
                j2casa= j2casa + 1
                print('\nAvance 1 casa.\n')
            elif casadado == 3:
                j2casa= j2casa - 1
                print('\nVolte 1 casa.\n')
            elif casadado==6:
                j2status+=2
                print('\nFique 1 rodada sem jogar\n')
    #-------------- Executando a Regra Morrer -------------------------------------------------------------------------
        if j2casa == 2 or j2casa == 8 or j2casa == 18:
            perder = True
            print ('\nVocê foi morto por justa causa. \n Game Over para Você!!\n')
            # Extrato da sua vida
            
            print('\nEXTRATO\n')
            if J2casar == True:
                print('---Se casou')
            if j2divorsio==True:
                print('---Você se separou')
            if J1famoso == True:
                print('---Você ficou famoso')
            print('---Teve',J2filho,'filhos(as)')
            print('---Se formou em',J2formou)
            print('---Você ganhou na loteria R$',J2loteria,'\n')
            
    #---------------Executando a Regra Vencer---------------------------------------------------------------------------
        if j2casa >=21:
            vencer = True
            print('\nPARABÉNS! Você venceu.\n''\nFIM!!!!\n')
            
            print('\nEXTRATO\n')
            if j2casar == True:
                print('---Se casou')
            if j2divorsio==True:
                print('---Você se separou')
            if J1famoso == True:
                print('---Você ficou famoso')
            print('---Teve',J2filho,'filhos(as)')
            print('---Se formou em',J2formou)
            print('---Você ganhou na loteria R$',J2loteria,'\n')
            
    #---------------Executando a Regra de Voltar ao início--------------------------------------------------------------            
        if j2casa == 20:
            j2casa=0
            print('\nVolte para o início!!!!!!!\n')
    #----------------- Executando a Regra de SE FORMAR ---------------------------------------------------           
        if j2casa == 5:
            print('EBA! Você se formou.\nGire a roleta novamente para vermos no que se formou.\n')
            casadado=dado()
            
            if casadado == 1:
                print('\nAdvogado\n')
                j2formou = 'Advogado'
                
            elif casadado == 2:
                print('\nMedicina\n')
                j2formou = 'Medicina'
                
            elif casadado == 3:
                print('\nJogos Digitais\n')
                j2formou = 'Jogos Digitais'
                
            elif casadado == 4:
                print('\nSegurança de Informação\n')
                j2formou = 'Segurança de Informação'
                
            elif casadado == 5:
                print('\nEducação Fisica\n')
                j2formou = 'Educação Fisica'
                
            elif casadado == 6:
                print('\nAdministração\n')
                j2formou = 'Administração'
                
    #----------------- Executando a Regra de FILHO ---------------------------------------------------
        if j2casa == 6 or j2casa == 9 or j2casa == 13:
            print('\nEita!!!\nVocê teve um filho, Rode a roleta novamente.\nMas se parar no 5 vixxxxxxx GANHO GÊMIOS!\nBOA SORTE!\n')
            casadado = dado()
            if casadado == 5:
                J2filho = J2filho + 2
                print('\nTeve GÊMIOS!\n')
            else:
                J2filho = J2filho + 1
                print('\nTeve apenas 1 filho!\n')
    #----------------- Executando a Regra de CASAR ---------------------------------------------------
        if j2casa == 7 or j2casa == 16:
            print('\nVocê se casou\nPARABÉNS aos ponbinhos\n')
            casar = True
        if j2casa == 12:
            if j2casar ==True:
                print('\nVocê deixou a toalha molhada na cama\nCom essa atidude ocasiono uma separação.\n')
                j2casar = False
                j2divorsio=True
    #----------------- Executando a Regra de LOTERIA ---------------------------------------------------
        if j2casa== 14:
            print('\nVocê ganhou na loteria!!\nRode a roleta para vermos quanto ganhou.\n')
            casadado=dado()
            
            if casadado== 1:
                print('\nVocê ganhou R$ 2,50')
                j2loteria = 2.50
            elif casadado == 2:
                print('\nVocê ganhou R$5.000,00')
                j2loteria = 5000.00
            elif casadado == 3:
                print('\nVocê ganhou R$50.000,00')
                j2loteria = 50000.00
            elif casadado == 4:
                print('\nVocê ganhou R$500.000,00')
                j2loteria = 500000.00 
            elif casadado == 5:
                print('\nVocê ganhou R$5.000.000,00')
                j2loteria = 5000000.00
            elif casadado == 6:
                print('\nVocê ganhou R$100.000.000,00')
                j2loteria = 100000000.00
    #----------------- Executando a Regra de FAMOSO ---------------------------------------------------
        if j2casa == 15:
            print('\nOLHA SÓÓÓÓÓÓÓ!!!\nVocê ficou FAMOSO!.\nFIU!FIUUUUUU!\n')
            j2famoso=True
    #----------------- Executando a Regra de MATEMATICA ---------------------------------------------------
        if j2casa == 4 or j2casa == 11 or j2casa == 19:
            print('\nDesafio!!!\nRode novamente a roleta para vermos o que sai.\n')
            casadado = dado()
            if casadado ==1:
                print('\n Numeros primos até 100:\n')
                for i in range(2,101):
                    x=ehPrimo(i)
                    if x == True:
                        print(i)
            
            elif casadado == 2:
                print('\nSomatorio de 1 até 10\n')
                soma=1+2+3+4+5+6+7+8+9+10
                print('\nO resultado do Somatorio é',soma,'\n')
                
            elif casadado == 3: 
                print('\nsérie de Fibonacci até o décimo elemento\n')
                t1=0
                t2=1
                cont=3
                print(t1)
                print(t2)
                while(cont<=10):
                    t3=t1+t2
                    t1=t2
                    t2=t3
                    cont+=1
                    print(t3)
                
            elif casadado == 4:
                print('\nA área de um circulo de raio 2,5\n')
                circulo= 3.142 * (2.5 * 2)
                print('\nÁrea = π . r2\n3,142 . 2,5²\nO resultado',circulo,'cm\n')
                
                
            elif casadado == 5:
                print('\nFatorial de 5')
                fatorial5=5*4*3*2*1
                print('\nO fatorial de 5 é',fatorial5,'\n')
                
            elif casadado == 6:
                print('\n5 primeiros n divisivel por 2 e 5\n')
                print('\n(5) primeiros numeros divisiveis por 2\n')
                for i in range(2,11,2):
                    print('\n',i)
                print('\n(5) primeiros numeros divisiveis por 5\n')
                for e in range (5,30,5):
                    print('\n',e)



    if j1status>0:
        j1status=j1status-1

    if j2status>0:
        j2status=j2status-1




