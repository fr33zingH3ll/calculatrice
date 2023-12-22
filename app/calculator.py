from mathics.core.definitions import Definitions
from mathics.core.evaluation import Evaluation
from mathics.core.parser import MathicsSingleLineFeeder, parse

definitions = Definitions(add_builtin=True)

class Calculator:
    """Classe représentant une calculatrice basique avec des opérations binaires et unaires."""

    def __init__(self):
        """Initialise une instance de la calculatrice."""
        self.expression = ""  # Expression en cours d'évaluation

    def button_click(self, value):
        """Gère le clic sur un bouton de la calculatrice."""
        if value == "=":
            self.evaluate_expression()
        else:
            self.expression += value

    def evaluate_expression(self):
       evaluation = Evaluation(definitions=definitions, catch_interrupt=False)
       expr = parse(definitions, MathicsSingleLineFeeder(f"N[{self.expression}]"))
       result = expr.evaluate(evaluation)
       self.expression = str(result)
       return self.expression
