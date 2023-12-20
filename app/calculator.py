# calculator.py
import math
import re

class Calculator:
    def __init__(self):
        self.expression = ""
        self.operators = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '**': lambda x, y: x**y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: x / y,
            'sin': lambda x: math.sin(x),
            'cos': lambda x: math.cos(x),
            'tan': lambda x: math.tan(x),
            'ln': lambda x: math.log(x),
            'log': lambda x: math.log10(x),
            'sqrt': lambda x: math.sqrt(x),
            'exp': lambda x: math.exp(x),
            'pi': lambda: math.pi,
            'e': lambda: math.e,
        }

    def button_click(self, value):
        if value == "=":
            self.evaluate_expression()
        else:
            self.expression += value

    def evaluate_expression(self):
        try:
            for operator in self.operators.keys():
                if operator in self.expression:
                    result = self.evaluate_with_operator(operator)
                    print(f"Résultat : {result}")
                    self.expression = str(result)
                    return self.expression

            # Si aucun opérateur spécifique n'est trouvé, évaluer normalement
            result = eval(self.expression)
            print(f"Résultat : {result}")
            self.expression = str(result)
            return self.expression
        except Exception as e:
            print(f"Erreur d'évaluation : {e}")
        finally:
            self.expression = ""

    def evaluate_with_operator(self, operator):
        match operator:
            case '+':
                return self.evaluate_binary_operator(operator, self.operators[operator])
            case '-':
                return self.evaluate_binary_operator(operator, self.operators[operator])
            case '**':
                return self.evaluate_binary_operator(operator, self.operators[operator])
            case '*':
                return self.evaluate_binary_operator(operator, self.operators[operator])
            case '/':
                return self.evaluate_binary_operator(operator, self.operators[operator])
            case 'sin':
                return self.evaluate_unary_operator(operator, self.operators[operator])
            case 'cos':
                return self.evaluate_unary_operator(operator, self.operators[operator])
            case 'tan':
                return self.evaluate_unary_operator(operator, self.operators[operator])
            case 'ln':
                return self.evaluate_unary_operator(operator, self.operators[operator])
            case 'log':
                return self.evaluate_unary_operator(operator, self.operators[operator])
            case 'sqrt':
                return self.evaluate_unary_operator(operator, self.operators[operator])
            case 'exp':
                return self.evaluate_unary_operator(operator, self.operators[operator])
            case 'pi':
                return self.operators[operator]()
            case 'e':
                return self.operators[operator]()
            case _:
                raise ValueError(f"Opérateur non pris en charge : {operator}")

    def evaluate_binary_operator(self, operator, operation):
        print("evaluate by binary operator")
        parts = self.expression.split(operator)
        if len(parts) == 2:
            x, y = map(float, parts)
            return operation(x, y)
        else:
            raise ValueError(f"Erreur d'évaluation avec l'opérateur {operator}")

    def evaluate_unary_operator(self, operator, operation):
        print("evaluate by unary operator")
        part = self.expression[len(operator):]
        x = float(part)
        return operation(x)

