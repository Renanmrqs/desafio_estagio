"""
- Criar uma função em sua linguagem preferida. 
A função deve receber um número N > 1 (validar o input), 
e retornar todos os números primos até o número N. 
EX. p(2) = [2]; p(3) = [2, 3]; p(10) = [2, 3, 5, 7];

--- Criar uma função recursiva que resolva p

--- Criar uma função linear que resolva p
"""

def primo_linear():
    num = valid_input(input('Digite um numero: '))
    if num < 2:
        return 
    lista = []
    n = 1
    while n < num:
        if (num ** 0.5) % n  == 0:
            lista.append(n)
        n += 1
    return lista

def valid_input(n):
    try:
        n_int = int(n)
        if n_int < 0:
            raise ValueError
        return n_int
    except ValueError:
        return 'escreva um numero inteiro'
    
print(primo_linear())