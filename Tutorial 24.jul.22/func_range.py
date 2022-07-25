''' Função Range()
iterar sobre sequências numéricas, a função embutida range() é a resposta. Ela gera progressões aritméticas
'''

for i in range(10): #O ponto de parada fornecido nunca é incluído na lista
    print(i,end=',') #argumento end=',' serve para alinhar tudo na horizontal

'''
list(range(5, 10))          #[5, 6, 7, 8, 9]
list(range(0, 10, 3))       #[0, 3, 6, 9]
list(range(-10, -100, -30)) #[-10, -40, -70]
'''
letra = ['a','b','c','d','e','f','g','h']
for i in range(len(letra)):
    print(i, letra[i])