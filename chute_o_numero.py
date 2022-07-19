'''Projeto 3: Chute o Número
Objetivo: criar um algoritimo que gera um valor aleatório e eu tenho que ficar tentando o número até acerta.
Projeto 4: GUI do Chute o Número'''
import random
class ChuteONumero:
    def __init__(self):
        self.valor_aleatorio = 0
        self.valor_minimo =1
        self.valor_maximo = 100
        self.tentar_novamente = True
        
    def Iniciar(self):
        self.GerarNumeroAleatorio()
        self.PedirValorAleatorio()
        try:
            while self.tentar_novamente == True:
                if int(self.valor_do_chute)> self.valor_aleatorio:
                    print("Chute um valor mais baixo!")
                    self.PedirValorAleatorio()
                elif int(self.valor_do_chute) < self.valor_aleatorio:
                    print('Chute um valor mais alto!')
                    self.PedirValorAleatorio()
                elif self.valor_do_chute == self.valor_aleatorio:
                    self.tentar_novamente = False
                    print('Parabéns você acertou!')
        except:
            print('Favor digitar apenas números!')

    def PedirValorAleatorio(self):
        self.valor_do_chute = int(input('Chute um número: '))    
    def GerarNumeroAleatorio(self):
        self.valor_aleatorio = random.randint(self.valor_minimo, self.valor_maximo)

chute = ChuteONumero()
chute.Iniciar()
