# Existe aleatoriedade verdadeira nos computadores?

# O módulo random oferece alguns mecanismos que permite que você trabalhe com números (pseudoaleatórios).

"""
Apenas os processos físicos completamente fora de nosso controle (como a intensidade da radiação cósmica)
podem ser usados como fonte de dados verdadeiramente aleatórios.
Os dados produzidos por computadores determinísticos não podem de maneira alguma ser considerados aleatórios.
"""
from random import random

for i in range(5):
    print(random())

# ---------------------------------------------------------------------------------------------------------------

from random import randrange, randint

print(randrange(1), end=' ')
print(randrange(0, 1), end=' ')
print(randrange(0, 1, 1), end=' ')
print(randint(0, 1))

# ---------------------------------------------------------------------------------------------------------------

# O programa provavelmente irá gerar um conjunto de números em que alguns elementos não são únicos:
from random import randint

for i in range(10):
    print(randint(1, 10), end=',')


