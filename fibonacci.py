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
    num1, num2 = 0, 1
    fib = num1 + num2
    for _ in range(num - 1):
        fib = num1 + num2
        num1 = num2
        num2 = fib
        
    return fib
        

def valid_input(n):
    try:
        n_int = int(n)
        if n_int < 0:
            raise ValueError
        return n_int
    except ValueError:
        return 'escreva um numero inteiro'
    
    
print(fibonacci_recursivo())
