x = int(input("Please enter an integer: "))

if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')
'''
elif é uma abreviação para else if, e é útil para evitar indentação excessiva. Uma sequência if … elif … elif … substitui os comandos switch ou case, encontrados em outras linguagens.
'''