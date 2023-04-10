valA= float ( input('Adicione um valor chamado A: '))
valB= float ( input( 'Adicione um valor chamado B: '))
valC= float ( input('Adicione um valor chamado C: '))

val1= valA+valB
val2= valA+valC

if(val1 < val2):
    print('O valor' , val1, 'é menor.')

else:
    print('O valor', val1, 'é maior.')
