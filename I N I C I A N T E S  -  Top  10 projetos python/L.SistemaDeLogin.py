import PySimpleGUI as sg

#Criar as janelas e estilos (layouts)
# {Loguin /  janela2 / janela3 / janela4 }
def janela_login():
    sg.theme('Reddit')
    layout_login = [
        [sg.Text('Usuário:')],
        [sg.Input(key='usuario')],
        [sg.Text('Senha:')],
        [sg.Input(key='senha')],
        [sg.Button('login')],
        [sg.Text('', key='mensagem')]]
    return sg.Window('Login', layout= layout_login, finalize=True)

def janela_pedido():
    sg.theme('Reddit')
    layout_pedido = [
        [sg.Text('FAZER PEDIDO')],
        [sg.Checkbox('Pizza Pepperoni',key='pizzapepperoni'),sg.Checkbox('Pizza Portuguesa',key='pizzaportuguesa')],
        ]
    return sg.Window('Selecionar o pedido', layout= layout_pedido, finalize=True)

#Criar as janelas iniciais
janela1,janela2 = janela_login, None

#Criar um loop de leitura de eventos
while True:
    window, event, values = sg.read_all_windows()
    #quando a janela for fechada
    if window == janela1 and event == sg.WIN_CLOSED:
        break
    #quando nós queremos ir para a próxima janela
    if window == janela1 and event == 'login':
        senha_correta= '123456'
        usuario_correto= 'danilo'
        usuario = values ['usuario']
        senha = values['senha']
        if senha == senha_correta and usuario == usuario_correto:
            janela_login['mensagem'].update('Login feito com sucesso')
        else:
            janela_login['mensagem'].update('usuário ou senha incorreto')
        janela2 = janela_pedido()
        janela1.hide()
    #quando queremos retornar para a janela anterior
    #fechar a a janela e interromper o processo
    
#Lógica que deve acontecer ao clicar nos botões
#Login
