# Fibonacci numbers module

def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

def fib2(n):   # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result

''' COMO CONSTRUIR MÓDULOS
Importe esse módulo com o seguinte comando:

>>> import d.fibo
This does not add the names of the functions defined in fibo directly to the current namespace (see Escopos e espaços de nomes do Python for more details); it only adds the module name fibo there. Using the module name you can access the functions:

>>> fibo.fib(1000)
...0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987
>>> fibo.fib2(100)
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
>>> fibo.__name__
'fibo'
Se pretender usar uma função muitas vezes, você pode atribui-lá a um nome local:

>>>
>>> fib = fibo.fib
>>> fib(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
'''