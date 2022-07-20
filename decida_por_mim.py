'''Projeto 5: Decida por mim
Faça uma pergunta para o programa e ele terá que dar uma resposta. 
Projeto 6: GUI do Decida por mim'''
import random
import PySimpleGUI as sg
class DecidaPorMim:
    def __init__(self):
        self.respostas = [
            'Com certeza, você deve fazer isso!',
            'Não sei, você que sabe',
            'Não faz isso não!',
            'Acho que tá na hora certa',
            'Rapaiz, mexe cum isso não...',
            'Moço, deixe de sê besta sôh!',
            'Prestensão no seu caminho',
            'Oia só bem onde esse treim vai te levá',
            'Espia o andá da carrage, e matuta nonde cê vai chegá',
            'primeiro matuta mió no assunto...'
        ]
    def Iniciar(self):
        #Layout
        layout = [
            [sg.Text('Faça sua pergunta aqui:')],
            [sg.Input()],
            [sg.Output(size=(40,15))],
            [sg.Button('Decida por mim')]
        ]
        #criar janela
        self.janela = sg.Window('Decida por mim', layout = layout)
        while True:
            #ler os valores
            self.eventos, self.valores = self.janela.Read()
            #fazer algo com os valores
            if self.eventos == 'Decida por mim':
                print(random.choice(self.respostas))
            

decida = DecidaPorMim()
decida.Iniciar()
