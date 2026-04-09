"""
- Criar uma função em sua linguagem preferida. 
A função deve receber um número N >= 0 (deve validar o input para a função), 
e retornar o valor correspondente deste número na sequência Fibonacci. 
EX. fib(0) =0; fib(1) = 1; fib(2) = 1; fib(3) = 2; fib(5) = 5; fib(6) = 8.
--- Criar uma função recursiva que resolva Fibonacci 
--- Criar uma função linear que resolva Fibonacci
"""
def fibonacci_recursivo():
    num = valid_input(input('Digite um numero: '))
    count = 0
    while True:
        print(f'Fib({count}): {num}')
        count += 1
        if count == 2:
            num += 1
        if count == 6:
            break
    

def valid_input(n):
    try:
        n_int = int(n)
        if n_int < 0:
            raise ValueError
        return n_int
    except ValueError:
        return 'escreva um numero inteiro'
    
    
fibonacci_recursivo()
print('vining')