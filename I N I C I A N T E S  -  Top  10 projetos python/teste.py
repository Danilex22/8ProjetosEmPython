import PySimpleGUI as sg

layout = [[sg.Text('Very basic Window')],
          [sg.Text('Click X in titlebar or the Exit button')],
          [sg.Button('Go'), sg.Button('Exit')]]

window = sg.Window('Window Title', layout)

while True:
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break

window.close()