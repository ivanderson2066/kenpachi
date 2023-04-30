#simulador de ddado
#simular um dado, gerando valor de 1 ate 6
import random

class SimuladorDeDado:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        self.mensaagem = 'voce gostaria de gerar um novo valor dado'

    def iniciar(self):
        resposta = input (self.mensaagem)
        try:
            if resposta == 'sim'or resposta =='s':
                self.GerarValorDoDado()
            elif resposta == 'não' or resposta == 'n':
                 print ('agradecemos sua participação')      
            else:
                 print ('favor digitar apenas sim ou não')
        except:
            print('ocorreu um erro ao receber sua resposta')     
        
    def GerarValorDoDado (self):
            print(random.randint(self.valor_minimo,self.valor_maximo))

simulador = SimuladorDeDado()
simulador.iniciar()