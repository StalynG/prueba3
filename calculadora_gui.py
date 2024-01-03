import tkinter as tk

class CalculadoraGUI:
    def __init__(self, master):
        self.master = master
        master.title("Calculadora")

        self.entry = tk.Entry(master, width=20, font=('Arial', 14))
        self.entry.grid(row=0, column=0, columnspan=4)

        # Definir botones
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
        ]

        # Crear y colocar botones
        for (text, row, col) in buttons:
            button = tk.Button(master, text=text, width=5, height=2, command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col)

    def on_button_click(self, value):
        current_text = self.entry.get()
        if value == '=':
            try:
                result = eval(current_text)
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except Exception as e:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
        else:
            self.entry.insert(tk.END, value)

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculadoraGUI(root)
    root.mainloop()
