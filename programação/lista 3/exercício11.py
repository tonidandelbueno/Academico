n=float(input('Digite um valor:'))
nota100=int(n/100)
n=n%100
nota50=int(n/50)
n=n%50
nota20=int(n/20)
n=n%20
nota10=int(n/10)
n=n%10
nota5=int(n/5)
n=n%5
nota1=int(n/1)
n=n%1

if (nota100>0):
    print(nota100, 'nota(s) de R$100')
if(nota50 >0):
    print(nota50, 'nota(s) de R$50')
if nota20>0:
    print(nota20, 'nota(s) de R$20')
if nota10>0:
    print(nota10, 'nota(s) de R$10')
if nota5>0:
    print(nota5, 'nota(s) de R$5')
if nota1>0:
    print(nota1,  'nota(s) de R$1')
