import tkinter as tk
from tkinter import ttk

def calcular_potencia_i(exponente):
    if exponente % 4 == 0:
        return "1"
    elif exponente % 4 == 1:
        return "i"
    elif exponente % 4 == 2:
        return "-1"
    else:
        return "-i"

def boton_calcular_potencia():
    exponente = int(entry_exponente.get())
    resultado = calcular_potencia_i(exponente)
    resultado_label.config(text=f"El resultado de i^{exponente} es: {resultado}", foreground="black")

root = tk.Tk()
root.title("Calculadora de Potencias de i")

mainframe = ttk.Frame(root, padding="20")
mainframe.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

titulo_label = ttk.Label(mainframe, text="Calculadora de Potencias de i", font=("Times New Roman", 16, "bold"), foreground="brown")
titulo_label.grid(row=0, column=0, columnspan=2, pady=10)

label_exponente = ttk.Label(mainframe, text="Exponente:")
label_exponente.grid(row=1, column=0, padx=5, pady=5)

entry_exponente = ttk.Entry(mainframe, width=10)
entry_exponente.grid(row=1, column=1, padx=5, pady=5)

boton_calcular = tk.Button(mainframe, text="Calcular", command=boton_calcular_potencia, font=("Arial", 12, "bold"), foreground="brown", background="orange")
boton_calcular.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

resultado_label = ttk.Label(mainframe, text="", font=("Arial", 12))
resultado_label.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()