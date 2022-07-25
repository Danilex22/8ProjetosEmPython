'''
py.exe          rodar/executar interpretador
quit ()         sair do interpretador 
python -c comando [arg] ..., que executa uma ou mais instruções especificadas na posição comando, analogamente à opção de shell -c
python -m módulo [arg] ... que executa o arquivo fonte do módulo como se você tivesse digitado seu caminho completo
# -*- coding: encoding -*-          declarar uma codificação diferente da padrão, uma linha de comentário especial deve ser adicionada como primeira linha do arquivo. onde encoding é uma das codecs válidas com suporte do Python.
# -*- coding: cp1252 -*-        (ex.) codificação Windows-1252
Comentários em Python começam com o caractere cerquilha ‘#’ e estende até o final da linha. 

Usando o Python como uma CALCULADORA: 
operadores: operadores +, -, * e /   parênteses (()) podem ser usados para agrupar expressões
números inteiros (ex. 2, 4, 20) são do tipo int
com parte fracionária (ex. 5.0, 1.6) são do tipo float
Divisão (/) sempre retorna ponto flutuante (float)
//      receber um inteiro como resultado (descartando a parte fracionária) você pode usar o operador //
%       para calcular o resto você pode usar o %
operador ** para calcular potências
sinal de igual ('=') é usado para atribuir um valor a uma variável
variável não é “definida” (não tem um valor atribuído), tentar utilizá-la gerará um erro
ponto flutuante (float); operadores com operandos de diferentes tipos convertem o inteiro para ponto flutuante
o valor da última expressão exibida é atribuída a variável _. Assim, ao utilizar Python como uma calculadora, fica mais fácil prosseguir com os cálculos
Além de int e float, o Python suporta outros tipos de números, tais como Decimal e Fraction
'''
from tkinter import N
#operadores padrões de comparação são os mesmos de C: < (menor que), > (maior que), == (igual), <= (menor ou igual), >= (maior ou igual) e != (diferente)


17 / 3  # classic division returns a float
17 // 3  # floor division discards the fractional part
17 % 3  # the % operator returns the remainder of the division
5 ** 2  # 5 squared
tax = 12.5 / 100
price = 100.50
price * tax
#price + _     _ está repetindo/copiando o último valor
#round(_, 2)   _está repetindo/copiando o último valor
print(sum(range(99))) #soma tudo do 0-99
print(range(510))