class data:
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano



    def imprimirData(self):
        print(self.dia,'/',self.mes,'/',self.ano)
        
    def imprimirDataPorExtenso(self):
        print(cidade, 'dia', self.dia, 'de', self.mes,'de', self.ano,'.')
        
        
    
hj = data('02', '08', '2002')
cidade = input('Adicione a sua cidade:')

hj.imprimirData()

hj.imprimirDataPorExtenso()

