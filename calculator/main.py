import tkinter as tk
from tkinter import font as tkfont

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Great Looking Calculator")
        self.root.geometry("400x600")
        self.root.resizable(False, False)

        # Fonts
        self.default_font = tkfont.Font(family="Helvetica", size=16)
        self.display_font = tkfont.Font(family="Helvetica", size=24, weight="bold")

        # Display
        self.display = tk.Entry(self.root, font=self.display_font, bd=10, insertwidth=2, width=14, borderwidth=4, relief="sunken", justify='right')
        self.display.grid(row=0, column=0, columnspan=4, pady=20)

        # Buttons
        buttons = [
            '7', '8', '9', '/', 
            '4', '5', '6', '*', 
            '1', '2', '3', '-', 
            'C', '0', '=', '+'
        ]

        # Layout
        row = 1
        col = 0
        for button in buttons:
            tk.Button(self.root, text=button, font=self.default_font, bg="lightgray", fg="black", height=3, width=9,
                      command=lambda b=button: self.on_button_click(b)).grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
            col += 1
            if col > 3:
                col = 0
                row += 1

        for i in range(4):
            self.root.grid_columnconfigure(i, weight=1)
        for i in range(5):
            self.root.grid_rowconfigure(i, weight=1)

    def on_button_click(self, char):
        if char == 'C':
            self.display.delete(0, tk.END)
        elif char == '=':
            try:
                expression = self.display.get()
                result = eval(expression)
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
            except Exception as e:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
        else:
            current_text = self.display.get()
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, current_text + char)

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
