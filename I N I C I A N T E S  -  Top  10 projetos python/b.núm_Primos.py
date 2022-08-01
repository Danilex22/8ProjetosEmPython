''' Números Primos
Construir uma lista de números primos dentre um intervalo de números escolhidos pelo usuário.'''

#Usuário Input de dados
minimo = int(input('Digite o valor mínimo da lista: '))
maximo = int(input('Digite o valor máximo da lista: '))

for n in range(minimo, maximo+1):
    for x in range(2, n):
        if n % x == 0:
            print(n, '=', x, '*', n//x)
            break
    else:
        # loop fell through without finding a factor
        print(n, '= nº Primo')