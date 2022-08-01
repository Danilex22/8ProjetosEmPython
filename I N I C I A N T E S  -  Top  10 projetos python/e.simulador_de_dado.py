'''Projeto 1: Simulador de dados
objetivo: exibir um valor de 1 até 6 sempre que rodar o programa
Projeto 2: GUI do simular de dados'''
from logging import exception
import random
import PySimpleGUI as sg

class SimuladorDeDado:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        self.mensagem = 'Você gostaria de jogar os dados?'
        #Layout
        self.layout = [
            [sg.Text('Jogar o dado?')],
            [sg.Button('Sim'),sg.Button('Não')]
            ]
            
    def Iniciar(self):
        #criar uma janela
        self.janela = sg.Window('Simulador de Dados', size=(280,70), layout= self.layout)
        #ler os valores na tela
        self.eventos, self.valores = self.janela.Read()
        #fazer alguma coisa com esses valores
        try:
                    if self.eventos == 'Sim' or self.eventos == 's':
                        self.GerarValorDoDado()
                    elif self.eventos == 'Não' or self.eventos == 'n':
                        print('Agradecemos sua participação')
                    else:
                        print('Favor digitar sim ou não')
        except:
                print('Ocorreu um erro ao receber sua resposta')
            

    def GerarValorDoDado(self):
        print(random.randint(self.valor_minimo,self.valor_maximo))

simulador = SimuladorDeDado()
simulador.Iniciar()