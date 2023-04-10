print('se não á dependentes com os termos de idade adicione 0 (zero)!!!')
pa= float(input('Quantas pessoas são dependentes, menor que 10 anos?'))
pb= float(input('Quantas pessoas são dependentes, de 10 á 30?'))
pc= float(input('Quantas pessoas são dependentes, de 31 á 60?'))
pd= float(input('Quantas pessoas são dependentes, mair de 60?'))
pt=300
pt=pt+(pa*100)
pt=pt+(pb*220)
pt=pt+(pc*395)
pt=pt+(pd*480)

print('Seu plano de saúde sera de R$',pt)