#simulador de ddado
#simular um dado, gerando valor de 1 ate 6
import random
import tkinter as tk

class SimuladorDeDado:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6

    def gerar_valor_do_dado(self):
        return random.randint(self.valor_minimo, self.valor_maximo)

class InterfaceGrafica:
    def __init__(self, master):
        self.master = master
        master.title('Simulador de Dado')

        self.label = tk.Label(master, text='Clique no botão para gerar um novo valor de dado.')
        self.label.pack()

        self.button = tk.Button(master, text='Gerar Dado', command=self.gerar_dado)
        self.button.pack()

        self.resultado = tk.Label(master, text='', font=('Helvetica', 36))
        self.resultado.pack()

        self.quit_button = tk.Button(master, text='Sair', command=master.quit)
        self.quit_button.pack()

        self.simulador = SimuladorDeDado()

    def gerar_dado(self):
        resultado = self.simulador.gerar_valor_do_dado()
        self.resultado.config(text=str(resultado))

root = tk.Tk()
interface_grafica = InterfaceGrafica(root)
root.mainloop()
