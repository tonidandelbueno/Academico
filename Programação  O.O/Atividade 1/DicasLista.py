# Lista 1 ativiodsade N° 3

class Data:
    # def __init__(self, dia , mes, ano):
    #     self.dia = dia
    #     self.mes = mes
    #     self.ano =ano
        
    def __init__(self):
        self.__dia = 1 #privado
        self._mes = 1 #protegido
        self.ano = 0 #publico

    def alterarDia(self, dia,): #métado de setar o valor do atributo Dia
        self.__dia = dia        

    def retornarDia(self): # Método para retornar o valor do atributo Dia
        return self.__dia

    def exibirData(self):
        print(self.__dia, '/', self._mes, '/', self.ano)

   def retornasStrMes(self, mes)
       if mes == 1:
             return 'janeiro'

        elif mes ==2:
             return 'feveriro'
        
        else:
             return ' lalaala'
   def exibirDataporExtenço(self, cidade):
        mes = retornasStrMes(self._mes)


outraData= Data()
outraData.alterarDia(17)
dia = outraData.retornarDia()

print(dia)

# print(outraData.dia)

print(outraData.retornarDia())

outraData.exibirData()
# outraData.dia = 17

# print(outraData.dia)