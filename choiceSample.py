# As funções choice e sample
"""
choice(sequence)
sample(sequence, elements_to_choose)

A primeira variante escolhe um elemento "aleatório" da sequência de entrada e o retorna.
Já a segunda monta uma lista (uma amostra) composta do elemento elements_to_choose "sorteado" da sequência inserida.
"""
from random import choice, sample

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(choice(my_list))
print(sample(my_list, 5))
print(sample(my_list, 10))