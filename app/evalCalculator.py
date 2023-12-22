import ast
import math
import operators

class EvalCalculator:
    def __init__(self):
        """
        Initialize the EvalCalculator with an empty expression.

        Attributes:
        - expression (str): The mathematical expression to be evaluated.
        """
        self.expression = ""

    def button_click(self, value):
        """
        Handle button clicks on the calculator.

        Parameters:
        - value (str): The value associated with the clicked button.
        """
        if value == "=":
            try:
                self.evaluate_expression()
            except Exception as e:
                self.expression = "Erreur"
        else:
            self.expression += value

    def translateOperator(self):
        """
        Translate unary operators in the expression.

        This method looks for unary operators in the expression and replaces them with the result of the operation.
        """
        for unaire_operator in operators.UNAIRE:
            if unaire_operator in self.expression:
                temp = self.expression.split(unaire_operator)[-1]
                for binaire_operator in operators.BINAIRE:
                    if binaire_operator in temp:
                        temp = temp.split(binaire_operator)[0]
                result = operators.UNAIRE[unaire_operator](float(temp))
                self.expression = self.expression.replace(unaire_operator + temp, str(result))

    def evaluate_expression(self):
        """
        Evaluate the current expression and update the display.

        This method evaluates the current expression, handling translation of unary operators,
        and replaces some symbols to make the expression compatible with the eval function.
        """
        try:
            # Translate unary operators
            self.translateOperator()

            # Replace symbols for compatibility with eval
            self.expression = self.expression.replace("^", "**")
            self.expression = self.expression.replace("mod", "%")

            # Evaluate the expression using the eval function
            result = eval(self.expression)
            self.expression = str(result)
            return self.expression
        except Exception as e:
            self.expression = "Erreur"
