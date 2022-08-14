import PySimpleGUI as sg

class FatorialDoNumero:
    def __init__(self):
        #Usuário Input de dados
        self.numero = int(input('Digite o Número do fatorial: '))
                        
    def Iniciar(self):
        #Layout
        self.layout = [
            [sg.Text('Nº Fatorial:'),sg.Input()],
            [sg.Button('Gerar fatorial')],
            [sg.Output(size=(20,10))],
            [sg.Button('Exit')]
            ]

    def FatorialDoNumero(self):
        try:
            while True:
                #janela
                    self.janela = sg.Window('Fatorial do Número', layout= self.layout)
                    #ler os dados da tela
                    self.eventos, self.valores = self.janela.Read()
                    for num in range( self.minimo, self.maximo+1):
                        if self.numero > 0:
                            fatorial = 1
                            for item in range(1, self.numero + 1):
                                fatorial = fatorial * item
                            print(fatorial)                    
                        if self.eventos == sg.WIN_CLOSED or self.eventos == 'Exit':
                            break
        except:
                print('Favor digitar apenas números!')
                self.Iniciar()        

        self.Window.close()
tela = FatorialDoNumero()
tela.Iniciar()




