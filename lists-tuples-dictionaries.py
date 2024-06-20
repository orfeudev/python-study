# lista

# coleção ordenada e mutável de elementos e é definida por []
# Quando usar? quando precisar de uma coleção ordenada de itens que pode ser alterada.

# dica: as listas em python começam pelo índice 0.

lista = ['banana', 'arroz', 'feijao']
print('Lista de compras', lista)

# adicionando um item a lista

lista.append('sorvete')
print('item adicionado: ', lista)

# removendo um item da lista

lista.remove('banana')
print('um item foi removido: ', lista)

# modificando um item:

lista[2] = 'iogurte'
print('A lista final de compras é: ', lista)

# tupla

# coleção ordenada e imutável de elementos
# é definida por ()
# não pode ser alterada, não pode adicionar nem remover elementos.
# use tuplas quando precisar de uma coleção ordenada de itens que não deve ser alterada.

coordenadas = (33.3123, -12.1234)
print("Coordenadas: ", coordenadas)

# dicionario

# coleção não ordenada de pares chave-valor
# sintaxe {}
# quando usar: Use dicionários quando precisar de uma coleção de pares chave-valor, onde cada chave deve ser única.
# neste exemplo irei utilizar um monstro e runas do jogo mobile Summoners War
mob = {
    'monster': 'Chimera',
    'type': 'Fire',
    'awakened': 'Rakan',
    'runes': 'Vampire'+' + '+'Destroy',
    'rune_position': '2 HP%' '4 CD%' '6 HP%'
}

# acessando os valores

print(mob['monster'])
print(mob['type'])
print(mob['awakened'])
print(mob['runes'])
print(mob['rune_position'])

# adcionando um novo par chave-valor

mob['use'] = 'Arena and GVG GOD'

# modificando um valor existente

mob['runes'] = 'Vampire + Energy'

print(mob)

# deletando valores

# del mob['use']  'para não afetar nada que esta acima'

print(mob)






