def calculate(expression):
    # Evaluate the expression and return the result
    return eval(expression)

# Test the calculator
result = int(calculate('2 + 3 * 5/2'))
print(result)
