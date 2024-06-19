#lista

#coleção ordenada e mutável de elementos e é definida por []
#Quando usar? quando precisar de uma coleção ordenada de itens que pode ser alterada.

#dica: as listas em python começam pelo índice 0.

lista = ['banana','arroz', 'feijao']
print('Lista de compras', lista)

#adicionando um item a lista

lista.append('sorvete')
print('item adicionado: ', lista)

#removendo um item da lista

lista.remove('banana')
print('um item foi removido: ', lista)

#modificando um item:

lista[2] = 'iogurte'
print('A lista final de compras é: ', lista)

#tupla

#coleção ordenada e imutável de elementos
#é definida por ()
#não pode ser alterada, não pode adicionar nem remover elementos.
#Use tuplas quando precisar de uma coleção ordenada de itens que não deve ser alterada.

coordenadas = (33.3123, -12.1234)
print("Coordenadas: ", coordenadas)

#dicionario

#coleção não ordenada de pares chave-valor
#sintaxe {}
#Quando usar: Use dicionários quando precisar de uma coleção de pares chave-valor, onde cada chave deve ser única.


