# gui.py
import tkinter as tk
from calculator import Calculator
import math

# Définition des variables globales
WIDTH, HEIGHT = 400, 700
normal = [
    {"%": "%", "CE": "CE", "C": "C"},
    {"": "", "^": "^", "√": "sqrt", "/": "/"},
    {"7": "7", "8": "8", "9": "9", "x": "*"},
    {"4": "4", "5": "5", "6": "6", "-": "-"},
    {"1": "1", "2": "2", "3": "3", "+": "+"},
    {"": "", "0": "0", ",": ".", "=": "="},
]

scientifique = [
    {"%": "%", "CE": "CE"},
    {"sin": "sin", "cos": "cos", "tan": "tan", "exp": "exp"},
    {"ln": "ln", "log": "log", "x^y": "^", "sqrt": "sqrt"},
    {"π": str(math.pi), "e": str(math.e)},
    {"7": "7", "8": "8", "9": "9", "*": "*"},
    {"4": "4", "5": "5", "6": "6", "-": "-"},
    {"1": "1", "2": "2", "3": "3", "+": "+"},
    {"": "", "0": "0", ",": ".", "=": "="},
]

class CalculatorGUI:
    def __init__(self, root):
        self.root = root
        self.calculator = Calculator()
        
        self.frame2 = tk.Frame(self.root, bg="green", width=WIDTH)
        self.expression_label = tk.Label(self.frame2, text="", font=("Arial", 16))

    def configure_screen(self):
        for i in range(10):
            self.root.grid_rowconfigure(i, weight=1)

        for i in range(4):
            self.root.grid_columnconfigure(i, weight=1)

        menu = tk.Menu(self.root)
        menu.add_command(label="normal", command=lambda: self.change_panel(normal))
        menu.add_command(label="scientifique", command=lambda: self.change_panel(scientifique))
        self.root.config(menu=menu)

        self.expression_label.grid(row=1, column=0, pady=10)
        self.frame2.grid(row=0, column=0, rowspan=2, columnspan=4, sticky="nsew")

        self.change_panel(normal)

    def change_panel(self, panel):
        frame3 = tk.Frame(self.root, bg="blue", width=WIDTH)
        j = 0
        for i, ligne in enumerate(panel):
            for key in ligne.keys():
                btn = tk.Button(frame3, text=key, width=9, height=3, command=lambda v=ligne.get(key): self.button_click(v))
                btn.grid(row=i, column=j, sticky="nsew")
                j += 1
            j = 0

        frame3.grid(row=2, column=0, rowspan=10, columnspan=4, sticky="nsew")

    def button_click(self, value):
        if value == "=":
            result = self.calculator.evaluate_expression()
            self.expression_label.config(text=result)
        elif value == "CE":
            self.calculator.expression = ""
            self.update_expression_label()
        elif value == "C":
            self.calculator.expression = self.calculator.expression[:-1]
            self.update_expression_label()
        else:
            self.calculator.button_click(value)
            self.update_expression_label()

    def update_expression_label(self):
        self.expression_label.config(text=self.calculator.expression)

def main():
    root = tk.Tk()
    root.geometry(f"{WIDTH}x{HEIGHT}")

    calculator_gui = CalculatorGUI(root)
    calculator_gui.configure_screen()

    root.mainloop()

if __name__ == "__main__":
    main()
