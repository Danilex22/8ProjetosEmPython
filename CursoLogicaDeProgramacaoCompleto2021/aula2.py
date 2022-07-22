#Condicionais
'''
if / elif / else
'''
#E ae Danilo, bora dar uma saída hoje?
#Se eu terminar meu trabalho aqui, eu consigo.

trabalho_terminado = True
if trabalho_terminado == True:
    print('Opa! Bora dar uma saída!')
else:
    print('Não posso sair agora. ')

'''
Ei, você consegue me ajudar a mover essas caixas lá pra fora hoje a tarde?
Se eu estiver livre, sim, mas se não meu irmão pode te ajudar.
'''
estou_livre = False
if estou_livre == True:
    print('Ok! posso ajudá-lo sim...')
else:
    print('Peça ao meu irmão pra te ajudar')
'''
Eu cheguei atrasado na aula, ainda posso entrar?
Se esse não for o seu 3º atraso, pode sim. Caso contrário será suspenso.
'''
numero_de_atrasos =0
if numero_de_atrasos >= 3:
    print('Você está suspenso!')
elif numero_de_atrasos ==1:
    print('Pode entrar, caso tome mais 2 faltas, irá ser suspenso')
elif numero_de_atrasos ==2:
    print('Pode entrar, porém caso tome mais 1 falta, irá ser suspenso')
else:
    print('Pode entrar')
#Projeto 3 - Encontre o maior número entre 2 outros valores

primeiro_valor = int(input('Digite o 1º valor: '))
segundo_valor = int(input('Digite o 2º valor: '))
if primeiro_valor > segundo_valor:
    print( 'O primeiro valor é maior que o 2º')
else:
    print ('O segundo valor é maior que o 1º')
