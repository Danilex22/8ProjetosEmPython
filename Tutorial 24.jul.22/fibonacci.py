#Sequência de Fibonacci
'''
a, b = 0, 1
while a < 100:
    print(a)
    a, b = b, a+b
'''
a, b = 0, 1
while a < 100:
    print(a, end=',') #end pode ser usado para evitar uma nova linha após a saída
    a, b = b, a+b