cont=0
maior=0
menor=0
media=0
while (cont <15):
    cont = cont + 1
    nota= float(input('Digite a ' f'{cont}º nota:'))

    media=media + nota

    if (cont==1 ):
        maior= menor = nota

    if (nota > maior):
        maior = nota

    if (nota < menor):
        menor = nota

print('maior nota é ', maior)

print('menor nota é ', menor)

print('A media da turma é', media/15)
