# Funções selecionadas do módulo platform:
# O módulo platform permite acessar os dados dos bastidores da plataforma, por exemplo:
# Informações sobre hardware, sistema operacional e versão do interpretador.

# Também existe uma função que pode mostrar todas as camadas subjacentes de uma só vez, chamada platform. 
# Ela retorna uma string que descreve o ambiente, portanto, sua saída é mais voltada para pessoas do que para processamento automatizado.
from platform import platform

print(platform())
print(platform(1))
print(platform(0, 1))



# A função machine:
# Às vezes você só quer saber o nome genérico do processador que está executando seu SO,
# juntamente com o Python e seu código: a função machine() fornece essas informações.
# Como em outras vezes, a função retorna uma string.
from platform import machine
print(machine())


# A função processor:
# A função processor() retorna uma string que contém o nome real do processador (se possível).
from platform import processor
print(processor())


# A função system:
# A função chamada system() retorna o nome genérico do SO como string.
from platform import system
print(system())


# A função version:
# A função version() fornece a versão do SO como uma string.
from platform import version
print(version())


# As funções python_implementation e python_version_tuple
# Se precisar saber qual a versão do Python que está executando o seu código, 
# você pode confirmar essa informação por meio de diversas funções dedicadas:
"""
Python_implementation() → retorna uma string que indica a implementação do Python 
(espere CPython neste caso, a não ser que você decida usar implementações alternativas do Python)

Python_version_tuple() → retorna uma tupla de três elementos, preenchida com:
- a parte principal da versão do Python;
- a parte menor;
- o número de nível do patch.
"""
from platform import python_implementation, python_version_tuple

print(python_implementation())

for atr in python_version_tuple():
    print(atr)
