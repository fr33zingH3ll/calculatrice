import math
import re

class Calculator:
    """Classe représentant une calculatrice basique avec des opérations binaires et unaires."""

    def __init__(self):
        """Initialise une instance de la calculatrice."""
        self.expression = ""  # Expression en cours d'évaluation
        # Dictionnaires d'opérations binaires et unaires
        self.binaire = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '^': lambda x, y: x**y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: x / y,
        }
        self.unaire = {
            'sin': lambda x: math.sin(x),
            'cos': lambda x: math.cos(x),
            'tan': lambda x: math.tan(x),
            'ln': lambda x: math.log(x),
            'log': lambda x: math.log10(x),
            'sqrt': lambda x: math.sqrt(x),
            'exp': lambda x: math.exp(x),
        }
        self.operators = {**self.binaire, **self.unaire}

    def button_click(self, value):
        """Gère le clic sur un bouton de la calculatrice."""
        if value == "=":
            self.evaluate_expression()
        else:
            self.expression += value

    def evaluate_expression(self):
        """Évalue l'expression actuelle et renvoie le résultat."""
        for operator in self.operators.keys():
            try:
                result = self.evaluate_with_operator(operator)
                print(f"Résultat : {result}")
                self.expression = str(result)
                return self.expression
            except Exception as e:
                pass

    def evaluate_with_operator(self, operator):
        """Évalue l'expression avec un opérateur spécifié."""
        if operator in self.binaire:
            return self.evaluate_binary_operator(operator, self.binaire[operator])
        elif operator in self.unaire:
            return self.evaluate_unary_operator(operator, self.unaire[operator])
        else:
            raise ValueError(f"Opérateur non pris en charge : {operator}")

    def evaluate_binary_operator(self, operator, operation):
        """Évalue une opération binaire dans l'expression."""
        parts = self.expression.split(operator)
        if len(parts) == 2:
            x, y = map(float, parts)
            return operation(x, y)
        else:
            raise ValueError(f"Erreur d'évaluation avec l'opérateur {operator}")

    def evaluate_unary_operator(self, operator, operation):
        """Évalue une opération unaire dans l'expression."""
        if self.expression[:len(operator)] != operator:
            raise ValueError("Mauvais opérateur")
        part = self.expression[len(operator):]
        x = float(part)
        return operation(x)
