'''Comandos break e continue, e cláusula else, nos laços de repetição
comando break, como no C, sai imediatamente do laço de repetição mais interno, 
seja for ou while.
Laços podem ter uma cláusula else, que é executada sempre que o laço se
encerra por exaustão do iterável (no caso do for) ou quando a condição
se torna falsa (no caso do while), mas nunca quando o
laço é interrompido por um break
'''
'''
#Lista de Números Primos
for n in range(2, 12):
    for x in range(2, n):
        if n % x == 0:
            print(n, '=', x, '*', n//x)
            break
    else:
        # loop fell through without finding a factor
        print(n, '= nº Primo')
'''
# Lista de Par/ímpar
for num in range(2, 101):
    if num % 2 == 0:
        print("= nº Par", num)
        continue
    print("= nº ímpar", num)