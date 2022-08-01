#Sequência de Fibonacci
'''
a, b = 0, 1
while a < 100:
    print(a)
    a, b = b, a+b
'''
'''
a, b = 0, 1
while a < 100:
    print(a, end=',') #end pode ser usado para evitar uma nova linha após a saída
    a, b = b, a+b
'''
def fib(n):    # write Fibonacci series up to n
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

# Now call the function we just defined:
fib(2000)
