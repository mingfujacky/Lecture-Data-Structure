def exponent_loop(base, exp):
    if exp < 0:
        raise ValueError("Exponent must be a non-negative integer.")
    
    result = 1
    for _ in range(exp):
        result *= base
    return result

print(exponent_loop(3, 5))

def exponent_recursive(base, exp):
    if exp < 0:
        raise ValueError("Exponent must be a non-negative integer.")
    if exp == 1:
        return base
    elif exp % 2 == 0:
        result = exponent_recursive(base, exp // 2)
        return result * result
    elif exp % 2 == 1:
        result = exponent_recursive(base, exp // 2)
        return result * result * base
    
print(exponent_recursive(3, 6))
print(exponent_recursive(10, 3))
print(exponent_recursive(17, 10))

def exponent_with_power_rule(base, exp):
    op_stack = []
    while exp > 1:
        if exp % 2 == 0:
            op_stack.append("square")
            exp = exp // 2
        elif exp % 2 == 1:
            op_stack.append("multiply")
            exp = exp - 1
    print(f'{op_stack=}')

    result = base
    while op_stack:    
        operation = op_stack.pop()
        if operation == "square":
            result = result * result
        elif operation == "multiply":
            result = result * base
    return result

print(exponent_with_power_rule(3, 6))
print(exponent_with_power_rule(10, 3))
print(exponent_with_power_rule(17, 10))

