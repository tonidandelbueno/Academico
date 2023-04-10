# Trabalho


def Tabelinha(mat,linhas,colunas):
    for l in range(linhas):
        for c in range(colunas):
            print(mat[l][c],end='\t')
        print()


def imprimirMatriz(mat,linhas,colunas):
    for l in range(linhas):
        for c in range(colunas):
            print(mat[l][c],end=' ')
        print()

def salvarMatriz(nomeArquivo,mat,linhas,colunas):
    arqEscrita = open(nomeArquivo, 'w')
    for l in range(linhas):
        for c in range(colunas):
            arqEscrita.write(mat[l][c] + ' ')
        arqEscrita.write('\n')
    arqEscrita.close()

def salvarMatrizCSV(nomeArquivo,mat,linhas,colunas):
    arqEscrita = open(nomeArquivo, 'w')
    for l in range(linhas):
        for c in range(colunas):
            arqEscrita.write(mat[l][c] + ' ')
        arqEscrita.write('\n')
    arqEscrita.close()

#def importarmatriz()


matAssentos = [] #matriz vazia

for i in range(6): #linhas
    aux = ['-'] * 29
    matAssentos.append(aux)

def getI(letra):
    if letra == 'A' or letra == 'a':
        return 0
    elif letra == 'B'or letra == 'b':
        return 1
    elif letra == 'C'or letra == 'c':
        return 2
    elif letra == 'D'or letra == 'd':
        return 3
    elif letra == 'E'or letra == 'e':
        return 4
    elif letra == 'F'or letra == 'f':
        return 5
    else:
        return -1


#menu
valorb = 500
executivo = valorb * 2.5
economico = valorb * 0.9
emergencia = valorb * 1.1
semreclinagem = valorb * 0.8

valor=0

reservas=0

executivolugares=0
economicolugares=0
emergencialugares=0
semreclinagemlugares=0

sair =False
while sair ==False:
    opção=int(input('1- Carregar dados.\n2- Mostrar o mapa.\n3- Listar preços.\n4- Reserva de asseentos.\n5- liberação de asseentos.\n6- Relatórios.\n7- Salvar dados.\n8- sair.\nDigite uma opção: '))
    
    if opção == 1:
        nomeArq=input('Digite o nome do arquivo: ')
        salvarMatrizCSV(nomeArq,matAssentos,6,29)
        
    if opção == 2:
        imprimirMatriz(matAssentos,6,29)
    if opção == 3:
        tabeladepreços = [['Categoria','Preço','Desconto < 2 anos','Desconto < 12 anos'],
        ['Executivo',executivo,'20%','10%'],
        ['Econômica',economico,'50%','30%'],
        ['Saída',emergencia,'30%','20%'],
        ['Sem Reclinagem',semreclinagem,'70%','50%']]
        aaaaa = Tabelinha(tabeladepreços,5,4)
        print(aaaaa)

    if opção == 4:
        imprimirMatriz(matAssentos,6,29)
        lugares = int(input('Digite o número de assentos a serem reservados: '))
        for i in range(1,lugares+1):
            coluna = input('Digite a fileira: ')
            assento = int(input('Digite o assento: '))
            assento=assento-1
            matAssentos[getI(coluna)][assento] = 'X'
        reservas+=lugares
        imprimirMatriz(matAssentos,6,29)
        
    if opção == 5:
        imprimirMatriz(matAssentos,6,29)
        lugares = int(input('Digite o número de assentos a serem Liberados: '))
        for i in range(1,lugares+1):
            coluna = input('Digite a fileira: ')
            assento = int(input('Digite o assento: '))
            assento-=1
            matAssentos[getI(coluna)][assento] = '-'
        reservas-= lugares
        imprimirMatriz(matAssentos,6,29)
        
    if opção == 6:
        print('Tem',reservas, 'lugares reservados.')
        for i in range(0,6):
            for j in range(0,6):
                if matAssentos[i][j] == 'X':
                    executivolugares+=1
                    valor+=executivo
        for i in range(0,6):
            for j in range(6,10):
                if matAssentos[i][j]=='X':
                    economicolugares+=1
                    valor+=economico
        for i in range(0,6):
            for j in range(13,28):
                if matAssentos[i][j]=='X':
                    economicolugares+=1
                    valor+=economico
        for i in range(0,6):
            for j in range(11,13):
                if matAssentos[i][j]=='X':
                    emergencialugares+=1
                    valor+=emergencia
        for i in range(0,6):
            if matAssentos[i][10]=='X':
                semreclinagemlugares+=1
                valor+=semreclinagem
        for i in range(0,6):
            if matAssentos[i][28]=='X':
                semreclinagemlugares+=1
                valor+=semreclinagem
        print('Lugares da categoria executiva ocupados:',round(100 *executivolugares/36,2))
        print('Lugares da categoria econômica ocupados:',round(100* economicolugares/114,2))
        print('Lugares sem reclinagem ocupados:',round(100*semreclinagemlugares/12,2))
        print('Lugares com saída de emergência ocupados:',round(100*emergencialugares/12,2))
        print('Valor total arrecadado: R$',valor)

    if opção == 7:
        salvarMatrizCSV(nomeArq,matAssentos,6,29)
    if opção == 8:
        sair=True
        print('\nSaindo ....')