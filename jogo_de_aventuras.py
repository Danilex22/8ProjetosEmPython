'''Projeto 7 - JOgo de Aventura
Elaborar um jogo de decisões onde eu terei que criar vários finais diferentes de acordo com as respostas 
que forem dadas. Projeto 8: GUI do Jogo de Aventuras'''
#Cenário: estamos em meio a uma guerra de duas nações: Luxim e Sodorna (reino da sombras)
#A vitória final será do reino Luxim (reino da luz) e Sodorna será derrotado em todas as circunstâncias
#Tome as decisões corretas que irão culminar na ADESÃO/ALISTAMENTO ao reino Luxim caso contrário 
#você irá cair/ALISTADO pelo reino Sodorna
import PySimpleGUI as sg
class JogoDeAventura:
    def __init__(self):
        self.perg1 = 'Você nasceu em Sodorna ou Luxim? ' #Luxim (Lux) ou Sodorna (Sod)
        self.perg2 = 'Você prefere conquistar a virtude ou o Poder? ' #virtude (Lux) #poder (Sod)
        self.perg3 = 'Você luta com bravura ou oportunismo? ' #bravura (Lux)  #oportunismo(Sod)
        self.perg4 = 'Qual é seu instrumento de batalha? ' #flecha (Lux) ou espada(Sod)
        self.perg5 = 'Qual é sua posição no campo de batalha? ' #retaguarda (Lux) ou linha de frente(Sod)
        self.destin1 = 'Você será um guerreiro da luz!'
        self.destin2 = 'Você será um líder virtuoso!'
        self.destin3 = 'Você será um guerreiro das sombras!'
        self.destin4 = 'Você não é um guerreiro fiel e confiável!'
        self.destin5 = 'Você irá perecer no campo de batalha.'

    def Iniciar(self):
        #Layout
        layout = [
            [sg.Output(size=(30,10))],
            [sg.Input(size=(25,10), key= 'escolha')],
            [sg.Button('Iniciar'), sg.Button('Responder')]
            
        ]
        #criar a janela
        self.janela = sg.Window('Jogo de Aventuras', layout = layout)
        #ler os dados
        self.LerValores()
        #fazer algo com os dados
        if self.evento == 'Iniciar':
            print(self.perg1)
            self.LerValores()
            if self.valores['escolha'] == 'Luxim' or self.valores['escolha'] == 'Lux':
                print(self.perg2)
                self.LerValores()
                if self.valores['escolha'] == 'virtude':
                    print(self.destin1)
                    self.LerValores()
                elif self.valores['escolha'] == 'poder':
                    print(self.destin3)
                    self.LerValores()
            if self.valores['escolha'] == 'Sodorna' or self.valores['escolha'] == 'Sod':
                print(self.perg3)
                self.LerValores()
                if self.valores['escolha'] == 'bravura':
                    print(self.destin2)
                    self.LerValores()
                if self.valores['escolha'] == 'oportunismo':
                    print(self.destin4)
                    self.LerValores()
            resp3 = print(self.perg4)
            self.LerValores()
            if resp3 == 'flecha':
                print(self.destin1)
                self.LerValores()
            elif resp3 == 'espada':
                print(self.destin3)
                self.LerValores()
            resp4 = print(self.perg5)
            self.LerValores()
            if resp4 == 'retaguarda':
                print(self.destin1)
                self.LerValores()
            if resp4 == 'linha de frente':
                print(self.destin5)
    
    def LerValores(self):
        self.evento, self.valores = self.janela.Read()

jogo = JogoDeAventura()
jogo.Iniciar()    

