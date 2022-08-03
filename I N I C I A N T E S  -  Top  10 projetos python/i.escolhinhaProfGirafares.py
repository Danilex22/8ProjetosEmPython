''' Escolinha do professor Girafares
Construir lista de alunos
Construir lista de professores
Construir sistema de loguin, acesso exclusivo aos professores
Construir um 

construir uma lista de alunos,
atribuir suas notas na prova 1,2,3,4,5
atribuir sua lista do total de presenças (mínimo=1; máximo = 100)
construir uma lógica de aprovado ou não aprovado com base no conceito média
'''
import random
from statistics import median
from math import isnan
from itertools import filterfalse
import i.medias_alunos


#### Loguin de Acesso ####
Acesso = input('Escolha seu personagem: ')
if Acesso.lower() == 'girafares':
    print ('Acesso autorizado!')
    print ('Bem-Vindo!{0} ao Sistema de Notas da Escolinha'.format(Acesso))
else:
    print ('Acesso negado!')

#### Composição da Escolinha ####
professor = ['girafares']
alunos = ['kiko','chaves','chiquinha','pópis','nhonho','paty','godinez','eureka','batuta']
print('-------------------------------------------')
print('Quantidade de alunos na turma: ', len(alunos))
print('Lista de Alunos Matriculados: ', alunos)

#### Composição das Notas ####

# ao longo do ano são 4 provas : P1, P2, P3 e P4.
notas_P1 = [round(random.uniform(3,10), 2),round(random.uniform(4,10), 2),round(random.uniform(5,10), 2),round(random.uniform(5,10), 2),round(random.uniform(6,10), 2),round(random.uniform(3,10), 2),round(random.uniform(3,10), 2),round(random.uniform(7,10), 2),round(random.uniform(5,10), 2),]
notas_P2 = [round(random.uniform(3,10), 2),round(random.uniform(4,10), 2),round(random.uniform(5,10), 2),round(random.uniform(5,10), 2),round(random.uniform(6,10), 2),round(random.uniform(3,10), 2),round(random.uniform(3,10), 2),round(random.uniform(7,10), 2),round(random.uniform(5,10), 2),]
notas_P3 = [round(random.uniform(3,10), 2),round(random.uniform(4,10), 2),round(random.uniform(5,10), 2),round(random.uniform(5,10), 2),round(random.uniform(6,10), 2),round(random.uniform(3,10), 2),round(random.uniform(3,10), 2),round(random.uniform(7,10), 2),round(random.uniform(5,10), 2),]
notas_P4 = [round(random.uniform(3,10), 2),round(random.uniform(4,10), 2),round(random.uniform(5,10), 2),round(random.uniform(5,10), 2),round(random.uniform(6,10), 2),round(random.uniform(3,10), 2),round(random.uniform(3,10), 2),round(random.uniform(7,10), 2),round(random.uniform(5,10), 2),]
print('-------------------------------------------')
print('Resultados da 1ª prova:     ', notas_P1)
print('Resultados da 2ª prova:     ', notas_P2)
print('Resultados da 3ª prova:     ', notas_P3)
print('Resultados da 4ª prova:     ', notas_P4)

#### Lista de Presença (ao longo do ano letivo) ####

total_presencas = 80 #qte total de presenças
presencas = [random.randrange(8, 81,2),random.randrange(8, 81,2),random.randrange(8, 81,2),random.randrange(8, 81,2),random.randrange(8, 81,2),random.randrange(8, 81,2),random.randrange(8, 81,2),random.randrange(8, 81,2),random.randrange(8, 81,2),]
print('-------------------------------------------')
print('Lista de quantidade de presenças: ', presencas)

#### FUNÇÃO PARA CONSTRUIR UMA LISTA DE NOTAS nas provas: ####
'''n1 = int(input('1ª nota da sequência: '))
r = int(input('construção das notas da sequência: '))
qte = int(input('nº total de notas: '))
u = n1 +r*(qte-1)
print(f'Todas as notas da prova: ')
def notas_P1(n):
    """Retorna a lista de notas obtidas na prova 1"""
    result = []
    for var in range(n1,u,r):
        print(var)
print(notas_P1(10), end=' ')'''


#### Critérios de aprovação ####
'''
situação= passou direto média >= 8  presenças >=70%
situação= APROVADO      média >=7 e presença >=60%
situação= RECUPERAÇÃO   média >=5 e presença >=50%
situação= REPROVADO     média <5 e presença <50%
situação=matricula excluída <=10% presenças
'''

#### Cálculo da média Global da turma ####
media_P1 = median(notas_P1)
media_P2 = median(notas_P2)
media_P3 = median(notas_P3)
media_P4 = median(notas_P4)
print('-------------------------------------------')
print('A média global da turma na Prova1=   ', media_P1)
print('A média global da turma na Prova2=   ', media_P2)
print('A média global da turma na Prova3=   ', media_P3)
print('A média global da turma na Prova4=   ', media_P4)
print('-------------------------------------------')
#### Para iterar sobre os índices de uma sequência ####
for i in range(len(alunos)):
    print(i, alunos[i])



print('-------------------------------------------')
print('A média do aluno Kiko foi: ', round(media_kiko,2))
print('A média do aluno Chaves foi: ', round(media_chaves,2))
print('A média da aluna Chiquinha foi: ', round(media_chiquinha,2))
print('A média da aluna Pópis foi: ', round(media_popis,2))
print('A média do aluno Nhonho foi: ', round(media_nhonho,2))
print('A média da aluna Paty foi: ', round(media_paty,2))
print('A média do aluno Godinez foi: ', round(media_godinez,2))
print('A média do aluno Eureka foi: ', round(media_eureka,2))
print('A média do aluno Batuta foi: ', round(media_batuta),2)
print('-------------------------------------------')
#### Situação do Aluno relação à Média ####
print('Situação do aluno Kiko :')
if media_kiko >= 8:
    print("APROVADO!!!")
elif media_kiko >= 7:
    print('Aprovado!')
elif media_kiko >=5:
    print('Recuperação')
elif media_kiko < 5:
    print('Reprovado.')

