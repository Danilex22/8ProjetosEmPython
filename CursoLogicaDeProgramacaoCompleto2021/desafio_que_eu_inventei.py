'''
Na escolinha do professor Girafares,
você é aluno = True "Acesso Negado!"
você é professor = True "aí segue a sequência da lógica
construir uma lista de alunos,
atribuir suas notas na prova 1,2,3,4,5
atribuir sua lista do total de presenças (mínimo=1; máximo = 100)
construir uma lógica de aprovado ou não aprovado com base no conceito média
passou direto média >= 8  presenças >=70
aprovado média >=7  presença >=60
recuperação média >=5 e presença >=50
reprovado média <5 e presença <50
matricula excluída <=10 presenças
'''
'''
alunos = ['girafares','kiko','chaves','chiquinha','pópis','nhonho','paty','godinez','eureka','batuta']
notasP1 = float([100,5.1,5.2,5.5,])
notasP2 = float([100,5.5,5.6,5.9,])
notasP3 = float([100,5.9,6,6.2,])
notasP4 = float([100,6.0,6.2,6.3,])
notasP5 = float([100,6.9,7,7.5,])
QtePresencas = [100,75,77,78,80,80,50,57,100,10 ]
for aluno in alunos:
    print(aluno)
SeuPersonagem = input('Escolha seu personagem: ')
if SeuPersonagem == 'girafares':
    print ('Acesso autorizado!')
    print ('Bem-Vindo! ao Sistema de Notas da Escolinha')
else:
    print ('Acesso negado!')
'''
