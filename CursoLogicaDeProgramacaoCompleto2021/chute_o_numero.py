import random

valor_minimo = int(input('Entre com o valor mínimo: '))
valor_máximo = int(input('Entre com o valor máximo: '))
valor_aleatorio = random.randint(int(valor_minimo),int(valor_máximo))
acertou = False
while acertou == False:
    chute = int(input('Entre com o valor do chute: '))
    if chute > valor_aleatorio:
        print('Chutou valor acima!')
    elif chute < valor_aleatorio:
        print('Chutou um valor abaixo!')
    else:
        acertou = True
        print('Parabéns, você acertou!!!')
        acertou = True
