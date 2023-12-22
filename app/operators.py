import math

# Dictionary of binary operators and their corresponding lambda functions
BINAIRE = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '^': lambda x, y: x ** y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y,
    'mod': lambda x, y: x % y,
    '%': lambda x, y: x*y/100
}

# Dictionary of unary operators and their corresponding lambda functions
UNAIRE = {
    'sin': lambda x: math.sin(x),
    'cos': lambda x: math.cos(x),
    'tan': lambda x: math.tan(x),
    'ln': lambda x: math.log(x),
    'log': lambda x: math.log10(x),
    'sqrt': lambda x: math.sqrt(x),
    'exp': lambda x: math.exp(x)
}

# Combined dictionary of all operators
OPERATORS = {**BINAIRE, **UNAIRE}
