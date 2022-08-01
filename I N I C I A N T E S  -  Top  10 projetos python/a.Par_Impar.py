''' Lista de Par ou ímpar
Construir uma lista de números pares ou ímpares de acordo com um intervalo fornecido pelo usuário'''
import PySimpleGUI as sg

class ListaParImpar:
    def __init__(self):
        #Usuário Input de dados
        self.minimo = int(input('digite o valor mínimo da lista: '))
        self.maximo = int(input('digite o valor máximo da lista: '))
                        
    def Iniciar(self):
        #Layout
        self.layout = [
            [sg.Text('Valor mínimo:'),sg.Input()],
            [sg.Text('Valor máximo:'),sg.Input()],
            [sg.Button('Gerar lista'), sg.Button('Exit')]
            ]
        #janela
        self.janela = sg.Window('Lista Par / ímpar', layout= self.layout)
        #ler os dados da tela
        self.eventos, self.valores = self.janela.Read()

    def ListaParImpar(self):
        try:
            while True:
                for num in range( self.minimo, self.maximo+1):
                    if num % 2 == 0:
                        print("= nº Par", self.num)
                        continue
                    print("= nº ímpar", self.num)
                    if self.eventos == sg.WIN_CLOSED or self.eventos == 'Exit':
                        break
        except:
            print('Favor digitar apenas números!')
            self.Iniciar()        

        self.Window.close()
tela = ListaParImpar()
tela.Iniciar()

