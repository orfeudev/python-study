# importando a biblioteca statistics

import statistics

# funções internas de python

# abs é uma função que passa o valor absoluto de um número(módulo)
print(abs(-5))

# retorna o maior item de um iterável ou o maior de dois ou mais argumentos
print(max(1, 2, 3, 4, 121))

# retorna o menor item de um iterável ou o menor de dois ou mais argumentos.
print(min(-2, 0, 3, 88))

# arredonda o primeiro número para o numero de casas dado no segundo argumento.
print(round(3.14159, 3))

# soma todos os numeros
print(sum([2, 6, 7, 10, 15]))

# statistics

# mean(): calcula a média aritmética dos dados desejados. A média aritmética é a soma de todos os valores dividida pelo número de valores.
# median(): A mediana é o valor que divide o conjunto de dados ao meio. Para um número ímpar de valores, é o valor do meio. Para um número par, é a média dos dois valores centrais.
# mode(): A moda é o valor que aparece com mais frequência no conjunto de dados.
# stdev(): O desvio padrão é uma medida que expressa o grau de dispersão de um conjunto de dados. Ou seja, o desvio padrão indica o quanto um conjunto de dados é uniforme. Quanto mais próximo de 0 for o desvio padrão, mais homogêneo são os dados.
# variance(): A variância é uma medida de dispersão que verifica a distância entre os valores da média aritmética.

# dados

altura = [1.50, 1.60, 1.70, 1.80, 1.90, 2.00, 2.10, 2.20, 2.30, 2.40]
print(altura)

media = statistics.mean(altura)
print(f'Média = {media}')

mediana = statistics.median(altura)
print(f'Mediana = {mediana}')

moda = statistics.mode(altura)
print(f'Moda = {moda}')

desvio_padrao = statistics.stdev(altura)
print(f'Desvio padrão = {desvio_padrao}')

variancia = statistics.variance(altura)
print(f'Variância = {variancia}')


# dicas de leituras
# books.goalkicker.com/pythonbook
# pythonfluente

