#Gerador de Números Aleatórios
'''
Módulo= random (aleatório em inglês)
import random
FUNÇÕES:
random.random() - gera um número aleatório entre 0 e 1
'''
'''
import random  
print(random.random())
print(10*random.random())
print(round(10*random.random()))
print(round(10*random.random()))
'''
'''
Gerar número aleatório entre 1 e 100:
a= round (100 * random.random() )


random.choice([lista_itens])
'''
'''
numeros_pares = [2, 4, 6, 8 , 10, 12, 14, 16, 18, 20]
print(random.choice(numeros_pares))
lista_de_sorteio = ['danilo', 'laila', 'ágata', 'daiana', 'káthia', 'keithy']
print(random.choice(lista_de_sorteio))
'''

'''
Jogar cara ou coroa
fazer sorteio de uma lista de nomes
escolher uma carta alatória do baralho
gerar nomes de usuários aleatoriamente
gerar senhas seguras
'''
'''
import random
print(random.random()) #Valor de 0,000000000000000 até 1,000000000000
print(random.uniform(5,20)) #Valor decimal do minimo ao maximo
print(random.randint(12,55)) #valor inteiro do minimo ao maximo

frutas = ['melancia', 'melão', 'maçã', 'laranja', 'abacaxi', 'limão']
print(random.choice(frutas))

carta_do_baralho = ['valeti','7copas','espadilha', 'zapi', 'dama paus', 'rei ouro', '3 copas']
random.shuffle(carta_do_baralho)
print(carta_do_baralho)
'''

#Desafio1
#CAra ou Coroa
'''
import random
moeda_a = ('cara')
moeda_b = ('coroa')
opcoes_de_giro = [moeda_a, moeda_b]
resultado_na_mao = random.choice (opcoes_de_giro)
print(resultado_na_mao)
'''

#DEsafio2
#Sorteio de Vencedores por nome
'''
lista_de_sorteio = ['danilo', 'laila', 'ágata', 'daiana', 'káthia', 'keithy']
print(random.choice(lista_de_sorteio))
'''

#Desafio 3
#Escolher aleatoriamente um número decimal de 100 a 999 FAZENDO A CONVERSÃO DELE EM NÚMERO INTEIRO
import random
valor_minimo = int(input('Digite o valor mínimo: '))
valor_maximo = int(input('Digite o valor máximo: '))
print(int(random.uniform(int(valor_minimo),int(valor_maximo))))