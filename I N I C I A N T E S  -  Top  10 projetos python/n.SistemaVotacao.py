from ast import ImportFrom
from rich import print 
import os
#Boas vindas:
print("""
    #---------------------------------#
    | ELEIÇÕES 2022 - Urna Eleitoral  |
    #---------------------------------#
""")
#Constantes
votos_Bolsonaro = 0
votos_Lula = 0
votos_PabloMarsal = 0
# rode eternamente
while True:
    print('#-----------------#')
    #apresente os candidatos
    print(f'[on green]TOTAL BOLSONARO:[/]{votos_Bolsonaro}{os.linesep}[on red]TOTAL Lula:[/]{votos_Lula}{os.linesep}[on yellow]TOTAL Pablo Marsal:[/]{votos_PabloMarsal}')
    print('#-----------------#')
    #permita votar
    try:
        voto = int(input(f'Para quem gostaria de votar?{os.linesep}[1] - Bolsonaro{os.linesep}[2] - Lula{os.linesep}[3] - Pablo Marsal{os.linesep}Digite exit para sair.{os.linesep}Seu voto:  '))
        if voto == 1:
            votos_Bolsonaro += 1
        elif voto == 2:
            votos_Lula += 1
        elif voto == 3:
            votos_PabloMarsal +=1
        elif voto == 'exit':
            exit()
            break
        else:
            pass
    except: 
        print('Digite apenas 1 , 2 ou 3')
    os.system('cls')