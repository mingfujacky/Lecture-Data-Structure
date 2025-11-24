def factorial_loop(number):
    result = 1
    for i in range(1, number + 1):
        result *= i
    return result

def factorial_recursive(number):
    if number == 1:
        return 1
    else:
        return number * factorial_recursive(number - 1)

print(factorial_loop(5))
print(factorial_recursive(5))