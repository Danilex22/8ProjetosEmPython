'''LISTAS
[ ] Inclui diversas estruturas de dados compostas, usadas para agrupar outros valores. A mais versátil é list (lista), que pode ser escrita como uma lista de valores (itens) separados por vírgula, entre colchetes
'''
notas = [8.5,5.1,6.2,7.5,4.3,2.5,10,8.7,6.5,3.5,1.35]
print(notas [:])
print(notas[10]) #imprimir um item só
print(notas[5]) #exibir um único item da lista
print(notas[9]) #exibir um único item da lista
print(notas[4]) #exibir um único item da lista
print(notas[1]) #exibir um único item da lista
print(notas[-9]) #exibir um único item da lista (contagem regressiva)
print(notas[-3]) #exibir um único item da lista (contagem regressiva)
print(notas[-0]) #exibir um único item da lista (contagem regressiva)
print(notas[-4]) #exibir um único item da lista (contagem regressiva)
print(notas[-5]) #exibir um único item da lista (contagem regressiva)
print(notas [-5:]) #exibir um certo trecho da lista
#listas também suportam operações como concatenação (colar novos itens)
# nome_da_lista + [1,2,3,a,b,c,...]
print(notas [:])
notas.append(10) #Adição/acréscimo no final da lista
print(notas [:])
#é permitido substituir/adicionar/excluir valores pelo índice
notas [0] = 10 #substituir valor pelo índice
notas [-5]= 1.5 #alteração de item na lista pelo seu índice regressivo
notas [8] = [] #excluir o item da posição 8
notas [4:6] = [] #isso irá EXCLUIR os itens 4 até 6
print(notas)
notas [0] = 5.8
notas + [7.88,8.88,9.88,10]
notas [6] = 7.5
notas [7:9] = []
print(notas [:])
notas [4:5] =[]
notas [:] = []
print(notas)
notas = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]
print(notas)
notas+[11, 12, 13, 14, 15]
print(notas)
notas[4]=77
print(notas)
notas.append(11)
print(notas)
notas + [12,13,14]
print(notas)
notas [3:8] = []
print(notas)
len(notas) #exibir qte de itens na lista
print(len(notas)) #exibir qte de itens na lista