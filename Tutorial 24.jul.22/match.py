'''     Instruções match
Uma instrução match pega uma expressão e compara seu valor com padrões sucessivos dados 
como um ou mais blocos case. Isso é superficialmente semelhante a uma instrução switch em
C, Java ou JavaScript (e muitas outras linguagens), mas é mais semelhante à correspondência
de padrões em linguagens como Rust ou Haskell. Apenas o primeiro padrão que corresponder é
executado e também pode extrair componentes (elementos de sequência ou atributos de objeto)
do valor em variáveis.
'''
'''
def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"
            #Observe o último bloco: o “nome da variável” _ atua como um curinga e nunca falha em corresponder. Se nenhum caso corresponder, nenhuma das ramificações será executada.
    print(status)
'''
class Point:
    x: int(input('Digite nº x: '))
    y: int(input('Digite nº y: '))


def where_is(point):
    match point:
        case Point(x=0, y=0):
            print("Origin")
        case Point(x=0, y=y):
            print(f"Y={y}")
        case Point(x=x, y=0):
            print(f"X={x}")
        case Point():
            print("Somewhere else")
        case _:
            print("Not a point")        
print (Point)