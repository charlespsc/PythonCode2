# Módulo de números de Fibonacci

def fib(n):
    """Escreve a série de Fibonacci até n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

def fib2(n):
    """Retorna a série de Fibonacci até n."""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result


# Prática no TERMINAL do IDE #
### Type "help", "copyright", "credits" or "license" for more information.
# >>> import fibo
# >>> fibo.fib(1000)
# 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 
# >>> fibo.fib2(100)
# [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# >>> fibo.__name__
# 'fibo'
# >>> fib = fibo.fib
# >>> fib(500)
# 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 
# >>> fib(100)
# 0 1 1 2 3 5 8 13 21 34 55 89 
# >>> fib(1000)
# 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 
# >>> 