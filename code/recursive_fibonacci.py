# Recursive Fibonacci implementation and iterative version with debug prints
# 1, 1, 2, 3, 5, 8, 13, 21, ...

def fibonacci_loop(number):
    a, b = 1, 1
    print(f'a: {a}, b: {b}')

    for _ in range(1, number):
        a, b = b, a + b
        print(f'a: {a}, b: {b}')
    return a

def fibonacci_recursive(number):
    print('fibonacci(%s) called.' % number)
    if number == 1 or number == 2:
        print('fibonacci(%s) called.' % number)
        return 1
    else:
        print('Calling fibonacci(%s) and fibonacci(%s).' % (number-1, number-2))
        result = fibonacci_recursive(number - 1) + fibonacci_recursive(number - 2)
        print('fibonacci(%s) returning %s.' % (number, result))
        return result
    
print(fibonacci_loop(8))
print('-'*40)
print(fibonacci_recursive(8))