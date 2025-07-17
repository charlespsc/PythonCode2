### No primeiro método:
# Usando o import para o módulo de matemática
import math

# imprimir o valor de sin(½π).
print("imprimir o valor de sin(½π):")
print(math.sin(math.pi/2))

# ---------------------------------------------------------------------------------------------------------------

# Como dois namespaces (o seu e o do módulo) podem coexistir.
import math


def sin(x):
    if 2 * x == pi:
        return 0.99999999
    else:
        return None


pi = 3.14

print("Seu namespace: ")
print(sin(pi/2))

print("Import do módulo, outro namespace: ")
print(math.sin(math.pi/2))

# ---------------------------------------------------------------------------------------------------------------

### No segundo método:
# A sintaxe de import indica precisamente qual entidade (ou entidades) do módulo são aceitáveis no código:
from math import pi

print(math.e)
# irá causar um erro (e é o número de Euler: 2,71828...)

# ---------------------------------------------------------------------------------------------------------------
# Importação seletiva:
from math import sin, pi

print(sin(pi/2))

# ---------------------------------------------------------------------------------------------------------------
# Observe o código no editor. Analise-o com atenção:

"""
linha 1: executar a importação seletiva;
linha 3: usar as entidades importadas e obter o resultado esperado (1.0)
linhas 5 a 12: redefinir o significado de pi e sin; de fato, eles substituem as definições originais (importadas) dentro do namespace do código;
linha 15: retorna 0.99999999, o que confirma nossas conclusões.
"""
from math import sin, pi

print(sin(pi / 2))

pi = 3.14


def sin(x):
    if 2 * x == pi:
        return 0.99999999
    else:
        return None


print(sin(pi / 2))

# ---------------------------------------------------------------------------------------------------------------
"""
Aqui, invertemos a sequência das operações do código:

linhas 1 a 8: definir seu próprio pi e sin;
linha 11: usá-los(0.99999999 aparece na tela)
linha 13: executar a importação; os símbolos importados substituem suas definições anteriores dentro do namespace;
linha 15: retorna 1.0 como resultado.
 """
pi = 3.14

def sin(x):
    if 2 * x == pi:
        return 0.99999999
    else:
        return None

print(sin(pi / 2))

from math import sin, pi

print(sin(pi / 2))

# ---------------------------------------------------------------------------------------------------------------
# No terceiro método:
# A sintaxe de import (*) é uma forma mais agressiva quando comparada com a anterior:
# from module import *

# ---------------------------------------------------------------------------------------------------------------
#A palavra-chave as
# import module as alias

# Aliasing
import math as m

print("Usando aliasing:")    
print(m.sin(m.pi/2))

