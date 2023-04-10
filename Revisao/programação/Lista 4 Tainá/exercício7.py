divisor=int(input('Entre com o valor do divisor:'))
intervaloi=int(input('Início do intervalo:'))
intervalof=int(input('Final do intervalo:'))

for n in range (intervaloi, intervalof):
    n % divisor == 0
        print('Números divisíveis por',divisor,'no intervalo de',intervaloi, 'a', intervalof,':', n)