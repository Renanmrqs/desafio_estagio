"""
- Criar uma função em sua linguagem preferida. 
A função deve receber um número N > 1 (validar o input), 
e retornar todos os números primos até o número N. 
EX. p(2) = [2]; p(3) = [2, 3]; p(10) = [2, 3, 5, 7];

--- Criar uma função recursiva que resolva p

--- Criar uma função linear que resolva p
"""

def primo_linear():
    usuario_input = valid_input(input('Digite um numero: '))
    if usuario_input < 2:
        return 
    lista = []
    
    for num in range(2, usuario_input + 1):
        fleguer = True
        for divisor in range(2, (num)):
            if num % divisor == 0:
                fleguer = False
                break
        if fleguer == True:
            lista.append(num)    
        
    return lista

def monta_primo(atual, limite, lista):
    
    if atual > limite:
        return lista
    
    if test_primo(atual, 2) == True:
        lista.append(atual)
        
    return monta_primo(atual + 1, limite, lista)

def test_primo(num, divisor):
    if divisor == num:
        return True
    
    if num % divisor == 0:
        return False
    
    return test_primo(num, divisor + 1)

def valid_input(n):
    try:
        n_int = int(n)
        if n_int < 0:
            raise ValueError
        return n_int
    except ValueError:
        return 'escreva um numero inteiro'
    


usuario_input = valid_input(input('Digite um numero: '))
resultado = monta_primo(2, usuario_input, [])
print(resultado)