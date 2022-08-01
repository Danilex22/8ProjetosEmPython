#Projeto Medidor de Velocidade
'''
Levando em consideração a velocidade máxima da via, 80km/h em determinada rua. Crie um algoritimo que recebe do usuário a velocidade capturada na via, e diga se ele foi ou não multado por excesso de velocidade. Se foi multado por excesso, o algoritimo deve classificar "leve", "grave" ou "gravíssima". Se a velocidade registrada estiver abaixo do teto deve informar "Velocidade Permitida." Caso velocidade registrada for 10km acima do teto, informar: "Velocidade acima do Teto. Infração Leve". Casol velocidade registrada for de até 20 km acima do teto, retornar: "Velocidade acima do teto. Infração Grave". Caso velocidade registrada for acima de 20 km após o teto, retornar: "Velocidade acima do teto. Infração Gravíssima"

# Método 5 Q's para montar um algoritimo:

Analise criticamento o problema e descubra: 
(tente explicar o  problema pra você mesmo em voz alta e peça mais informações/investigue mais até você compreender completamente o problema)

1) Quais são os dados de ENTRADA necessários ? 
Resp. a) Limite da via 
      b) Velocidade registrada
      
2) O que devo fazer com estes dados ?
Resp. receber a velocidade registrada,
      comparar com o limite da via
      atribuir ou não multa
    c) Consequências: "Velocidade permitida"; "Velocidade acima do Teto. Infração Leve"; "Velocidade acima do Teto. Infração Grave"; "Velocidade acima do Teto. Infração Gravíssima"

3) Quais são as restrições deste problema ?
Resp. 
      Velocidade mínima >= 40 Km/h
      Velocidade máxima <= 220 Km/h 

4) Qual é o resultado esperado ?
Resp.  algoritimo deve receber a velocidade registrada e informar uma das 4 consequências possíveis.
5) Qual é a sequência de passos a ser feita para chegar ao resultado esperado?
Limite_maximo;
veloc_registrada
if veloc_registrada<= 80  
  print "Velocidade permitida"
if veloc_registrada<= 90
  print "Velocidade acima do Teto - Infração Leve"
elif veloc_registrada<=110
  print "Velocidade acima do Teto - Infração Grave"
elif veloc_registrada>110
  print "Velocidade acima do Teto - Infração Gravíssima"
'''
Limite_maximo = int(input('Digite a velocidade máxima da via: '))
Limite_minimo = (Limite_maximo*0.4)
veloc_registrada = int(input('Digite sua velocidade capturada: '))
if veloc_registrada < Limite_minimo:
    print ('Velocidade INFERIOR à MÍNIMA da via')
    veloc_registrada = int(input('Digite sua velocidade capturada: '))
elif veloc_registrada <= Limite_maximo:
      print('Velocidade permitida')
      veloc_registrada = int(input('Digite sua velocidade capturada: '))
elif veloc_registrada <= (Limite_maximo+10):
      print ('Velocidade acima do Teto - Infração Leve ')
      veloc_registrada = int(input('Digite sua velocidade capturada: '))
elif veloc_registrada <= (Limite_maximo+20):
      print ('Velocidade acima do Teto - Infração Grave')
      veloc_registrada = int(input('Digite sua velocidade capturada: '))
elif veloc_registrada > (Limite_maximo+20):
      print ('Velocidade acima do Teto - Infração Gravíssima')
