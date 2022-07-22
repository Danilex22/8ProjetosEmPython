#Crie um programa que recebe um número e imprime o seu fatorial
'''
input numero
checar restrições
if numero > 0  if numero = inteiro
fatorial = 1
loop de 1 até numero
    fatorial = fatorial * numero
    print(fatorial)
'''
numero = int(input('Digite um número: '))
if numero > 0:
    fatorial = 1
    for item in range(1,numero+1):
        fatorial = fatorial*item
    print(fatorial)