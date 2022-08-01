''' Lista de Par ou ímpar
Construir uma lista de números pares ou ímpares de acordo com um intervalo fornecido pelo usuário'''
import PySimpleGUI as sg

class ListaParImpar:
    def __init__(self):
        
        #Layout
        self.layout = [
            [sg.Text('Valor mínimo:'),sg.Input()],
            [sg.Text('Valor máximo:'),sg.Input()],
            [sg.Button('Gerar lista')]
            [sg.Output(size=(100,100))]
            ]
        
    def Iniciar(self):
        #Usuário Input de dados
        self.minimo = int(input('digite o valor mínimo da lista: '))
        self.maximo = int(input('digite o valor máximo da lista: '))
        #janela
        self.janela = sg.Window('Lista Par / ímpar', size=(280,280), layout= self.layout)
        #ler os dados da tela
        self.eventos, self.valores = self.janela.Read()

    def ListaParImpar(self):
        for num in range( self.minimo, self.maximo+1):
            if num % 2 == 0:
                print("= nº Par", self.num)
            continue
            print("= nº ímpar", self.num)
        print(ListaParImpar)    

tela = ListaParImpar()
tela.Iniciar()

