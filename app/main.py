import tkinter as tk
import gui
import evalCalculator
import calculator

class MainWindow:
    def __init__(self, root):
        """
        Initialize the main window.

        Parameters:
        - root (tk.Tk): The root window of the application.
        """
        self.root = root
        self.root.title("Fenêtre Principale")

        # Create a label
        self.label = tk.Label(root, text="Choisissez une fenêtre à ouvrir:")
        self.label.pack(pady=10)

        # Create buttons for opening different windows
        self.open_window1_button = tk.Button(root, text="Parser simple", command=self.open_window1)
        self.open_window1_button.pack(pady=5)

        self.open_window2_button = tk.Button(root, text="Parser de eval()", command=self.open_window2)
        self.open_window2_button.pack(pady=5)

    def open_window1(self):
        """
        Open a new window with a simple parser.
        """
        # Create a new instance of the Calculator class
        calculator_window = tk.Toplevel(self.root)
        calculatorParser = calculator.Calculator()
        gui.CalculatorGUI(calculator_window, calculatorParser).configure_screen()

    def open_window2(self):
        """
        Open a new window with an eval-based parser.
        """
        # Create a new instance of the EvalCalculator class
        calculator_window = tk.Toplevel(self.root)
        calculatorParser = evalCalculator.EvalCalculator()
        gui.CalculatorGUI(calculator_window, calculatorParser).configure_screen()

if __name__ == "__main__":
    # Create the main Tkinter window and run the application
    root = tk.Tk()
    app = MainWindow(root)
    root.mainloop()
