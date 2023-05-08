#simulador de ddado
#simular um dado, gerando valor de 1 ate 6
import random

import random

class SimuladorDeDado:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        self.mensagem = 'Você gostaria de gerar um novo valor de dado? Digite "s" para sim ou "n" para não: '

    def iniciar(self):
        while True:
            resposta = input(self.mensagem)
            if resposta.lower() == 's' or resposta.lower() == 'sim':
                self.gerar_valor_do_dado()
            elif resposta.lower() == 'n' or resposta.lower() == 'não':
                print('Agradecemos sua participação!')
                break
            else:
                print('Favor digitar apenas "s" ou "n".')
    
    def gerar_valor_do_dado(self):
        print(random.randint(self.valor_minimo, self.valor_maximo))

simulador = SimuladorDeDado()
simulador.iniciar()
