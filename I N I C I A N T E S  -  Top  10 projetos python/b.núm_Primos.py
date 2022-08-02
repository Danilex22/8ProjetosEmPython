''' Números Primos
Construir uma lista de números primos dentre um intervalo de números escolhidos pelo usuário.'''
import PySimpleGUI as sg
#layout
layout = [  [sg.Text('Digite o valor mínimo da lista: '), sg.InputText()],
            [sg.Text('Digite o valor máximo da lista: '), sg.InputText()],
            [sg.Output()],
            [sg.OK(), sg.Cancel()]]

#Usuário Input de dados
minimo = int(input('Digite o valor mínimo da lista: '))
maximo = int(input('Digite o valor máximo da lista: '))

#janela
janela = sg.Window('Números Primos', layout)
#fazer alguma coisa com os dados
while True:
    event, Values = janela.read()
    for n in range(minimo, maximo+1):
        for x in range(2, n):
            if n % x == 0:
                print(n, '=', x, '*', n//x)
                break
        else:
            # loop fell through without finding a factor
            print(n, '= nº Primo')
    if event in (sg.WIN_CLOSED, 'Cancel'):
        break

janela.close()
