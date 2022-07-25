'''STRINGS
aspas simples ('...') ou duplas ("...") manipular strings (sequências de caracteres), que podem ser expressas de diversas formas. Elas podem ser delimitadas por 
função print() produz uma saída mais legível, ao omitir as aspas e ao imprimir caracteres escapados e especiais:
\n produz uma nova linha dentro das aspas simples ('...') ou duplas ("...") SÓ NA FUNÇÃO print()
r antes da primeira aspa print(r'C:\some\name')  # note the r before the quote (se vc tirar o r vai quebrar a linha)
C:\some\name

strings literais podem abranger várias linhas. Uma maneira é usar as aspas triplas: """...""" ou aspas triplas
Strings podem ser concatenadas (coladas) com o operador +, e repetidas com *
é possível "colar" uma variável com uma outra string  utilizando operador +
'''

print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")
print("""
        Py + thon               100 * 'ar
""")
print('Py' 'thon')
print(5*'abcdef')
print('frases extensas e com continuação ' 
      'podem ser quebradas '
      'através de aspas simples '
      'somadas umas às outras')
print('caso vc queira \n'
     'adicionar uma linha \n'
     'dentro da mesma string\n'
     'utilize a \n'
     'contrabarra + n')

firstName = 'Danilo'
secondName = 'Tiago'
thirdName = 'Chaga'
print(firstName+secondName+'da'+thirdName)
print(firstName+'\n'+secondName+'\n'+'da'+'\n'+thirdName)
print("""
Danilo   
    Tiago
        da
          Chaga
""")
print(10*(firstName+'\n'+secondName+'\n'+'da'+'\n'+thirdName+'\n'))
print( firstName[0]+'\n'+firstName[1]+'\n'+firstName[2]+'\n'+firstName[3]+'\n'+firstName[4]+'\n'+firstName[5]+'\n')
print( firstName[-6]+'\n'+firstName[-5]+'\n'+firstName[-4]+'\n'+firstName[-3]+'\n'+firstName[-2]+'\n'+firstName[-1]+'\n')
print(firstName[0:2])  # characters from position 0 (included) to 2 (excluded)
print(firstName[2:5]) # characters from position 2 (included) to 5 (excluded)
print(firstName[:2]) # character from the beginning to position 2 (excluded)
print(firstName[4:])  # characters from position 4 (included) to the end
print(firstName[-2:])  # characters from the second-last (included) to the end

print("""
 +---+---+---+---+---+---+
 | D | a | n | i | l | o |
 +---+---+---+---+---+---+
 0   1   2   3   4   5   6
-6  -5  -4  -3  -2  -1
""")

print("""
        +---+---+---+---+---+---+ 
          D | a | n | i | l | o   
        +---+---+---+---+---+---+
""")