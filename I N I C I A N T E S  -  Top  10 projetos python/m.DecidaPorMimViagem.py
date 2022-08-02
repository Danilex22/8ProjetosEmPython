'''
Construir um software que gere/construa perfis de usuários fictícios. 
O software deve gerar parâmetros como: nome, endereço, idade, aniversário, telefon, cidade, estado
e as informações tem que ser cruzadas e fidedignas
deve haver uma base de dados sólida e robusta que evite a formação conflitos    
exportar a informação em documentos txt

Este projeto é baseado/inspirado na Programadora Mariana España Feitosa (aluna do Jhonata DevAprender)
A finalidade é totalmente ***DIDÁTICA***
'''
####DECIDA PARA MIM MINHA PRÓXIMA VIAGEM####
########    Bibliotecas    ########
import pandas as pd
import numpy as np
from numpy import random
import time
import sys


########## Leque de Opções ##########
sul = ['Santa Catarina (SC)', 'Paraná (PR)', 'Rio Grande do Sul (RS)',]
sudeste = ['São Paulo (SP)', 'Minas GErais (MG)', 'Rio de Janeiro (RJ)', 'Espírito Santo (ES)']
centro_oeste = ['Goiás (GO)', 'Mato Grosso (MT)', 'Mato Grosso do Sul (MS)', 'Distrito Federal (DF)']
norte = ['Tocantins (TO)','Roraima (RR)', 'Acre (AC)', 'Amapá (AP)', 'Amazonas (AM)', 'Para (PA)', 'Rondonia (RO)']
nordeste = ['Piaui (PI)', 'Maranhão (MA)', 'Alagoas (AL)', 'Bahia (BA)', 'Rio Grande do Norte (RN)', 'Sergipe (SE)', 'Pernanbuco (PE)', 'Paraíba (PB)']

########## INPUT Descisão Usuário ##########
while True:
    regiao = str(input("""
    #-----------------------------------------#
    |  DECIDA POR MIM A MINHA PRÓXIMA VIAGEM  | 
    #-----------------------------------------#
    Apresentamos abaixo um leque com as 5 maiores 
    macrorregiões do país com destinos turísticos.
    Conte para nós onde você espera/deseja viajar (região)
    e iremos apresentar ***ALEATORIAMENTE *** uma opção 
    de destino turístico no formato: ***Estado (UF)***
    Você pode escolher mais de uma região, basta separar
    as opções por vírgula ( , )
    [1] Região Sul
    [2] Região Sudeste
    [3] Redigão Centro-Oeste
    [4] Região Norte
    [5] Região Nordeste
    Obs. Digite 'exit' para fechar programa.
    Digite a opção que corresponde à sua preferência:   """))
    
    if regiao.lower() == 'exit':
        print("Seu destino foi gerado em um arquivo destino_decidido.txt")
        time.sleep(4)
        sys.exit()

    lista_opcoes = [sul, sudeste, centro_oeste, norte, nordeste]

    # Processamento do dado inserido usuário
    regiao = regiao.split(",")
    for item in range(len(regiao)):
            regiao[item].strip()
            regiao[item] = int(regiao[item])+1
            estados = len(lista_opcoes[regiao[item]])

            # Seleção aleatória gerada pelo algoritimo
            decisao = np.random.randint(0,estados)

            #Imprimir o estado final definido anteriormente
            print('\n Sua região escolhida', regiao[item]+1,'é: ', lista_opcoes[regiao[item]][decisao])

            #Imprimir cada escolha final dentro de um arquivo TXT
            with open('destino_decidido.txt', 'a') as arquivo:
                arquivo.write(lista_opcoes[regiao[item]][decisao] + '\n')
    