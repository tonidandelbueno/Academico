s = float(input('Adicione o seu salario: '))
t= ( s * 11 / 100)

if (t > 318.20):
    d= (s - 318.20)
    print('Seu salário é ', d)

else:
    p= ( s - t)
    print('Seu salário é ', p)