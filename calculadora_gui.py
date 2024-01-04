import tkinter as tk
from tkinter import ttk
from calculadora import sumar, restar, multiplicar, dividir

class CalculadoraApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora")

        self.operacion = tk.StringVar()
        self.resultado = tk.StringVar()

        self.crear_interfaz()

    def crear_interfaz(self):
        # Pantalla
        pantalla = ttk.Entry(self.root, textvariable=self.resultado, font=('Arial', 20), justify='right', state='disabled')
        pantalla.grid(row=0, column=0, columnspan=4, sticky='nsew')

        # Botones
        botones = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', 'C', '=', '+'
        ]

        row_val = 1
        col_val = 0

        for boton in botones:
            ttk.Button(self.root, text=boton, command=lambda b=boton: self.click_boton(b)).grid(row=row_val, column=col_val, sticky='nsew')
            col_val += 1

            if col_val > 3:
                col_val = 0
                row_val += 1

        # Ajustar tamaño de las columnas y filas
        for i in range(4):
            self.root.columnconfigure(i, weight=1)
            self.root.rowconfigure(i + 1, weight=1)

    def click_boton(self, valor):
        if valor == '=':
            self.calcular_resultado()
        elif valor == 'C':
            self.resultado.set('')
        else:
            current_text = self.resultado.get()
            self.resultado.set(current_text + valor)

    def calcular_resultado(self):
        expresion = self.resultado.get()

        try:
            resultado = self.evaluar_expresion(expresion)
            self.resultado.set(resultado)
        except Exception as e:
            self.resultado.set('Error')

    def evaluar_expresion(self, expresion):
        try:
            num1, operador, num2 = expresion.split()
            num1, num2 = float(num1), float(num2)

            if operador == '+':
                return sumar(num1, num2)
            elif operador == '-':
                return restar(num1, num2)
            elif operador == '*':
                return multiplicar(num1, num2)
            elif operador == '/':
                return dividir(num1, num2)
            else:
                raise ValueError("Operador no válido")

        except Exception as e:
            raise ValueError("Expresión no válida")

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculadoraApp(root)
    root.mainloop()
