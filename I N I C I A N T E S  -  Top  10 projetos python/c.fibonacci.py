#Sequência de Fibonacci
from multiprocessing import Event
from multiprocessing.sharedctypes import Value
import PySimpleGUI as sg

#layout
layout = [  [sg.Text('Digite o valor máximo: '), sg.InputText()],
            [sg.OK(), sg.Cancel()]]
#janela
janela = sg.Window('Sequência de Fibonacci', layout= layout)
#fazer algo com os dados
while True:
    Event, values = janela.read()
    def fib(n):    # write Fibonacci series up to n
        """Print a Fibonacci series up to n."""
        a, b = 0, 1
        while a < n:
            print(a, end=' ')
            a, b = b, a+b
        print()
        fib(input('Digite o valor máximo: '))
    if Event in (sg.WIN_CLOSED,'Cancel'):
        break
# Now call the function we just defined:

janela.close()
