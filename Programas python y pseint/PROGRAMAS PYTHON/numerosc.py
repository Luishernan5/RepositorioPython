import tkinter as tk
from tkinter import ttk
from fractions import Fraction

def sumar_numeros_complejos(z1, z2):
    resultado = z1 + z2
    resultado_label.config(text="La suma es: " + str(resultado), foreground="black")

def restar_numeros_complejos(z1, z2):
    resultado = z1 - z2
    resultado_label.config(text="La resta es: " + str(resultado), foreground="black")

def multiplicar_numeros_complejos(z1, z2):
    resultado = z1 * z2
    resultado_label.config(text="La multiplicación es: " + str(resultado), foreground="black")

def dividir_numeros_complejos(z1, z2):
    resultado = z1 / z2
    parte_real = Fraction(resultado.real).limit_denominator()
    parte_imaginaria = Fraction(resultado.imag).limit_denominator()
    resultado_label.config(text="La división es: " + str(parte_real) + " + " + str(parte_imaginaria) + "i", foreground="black")

def obtener_numeros_complejos():
    try:
        z1_real = Fraction(entry_z1_real.get())
        z1_imag = Fraction(entry_z1_imag.get())
        z2_real = Fraction(entry_z2_real.get())
        z2_imag = Fraction(entry_z2_imag.get())
        
        z1 = complex(z1_real, z1_imag)
        z2 = complex(z2_real, z2_imag)
        
        return z1, z2
    except ValueError:
        resultado_label.config(text="Error: Ingresa números complejos válidos", foreground="red")
        return None

def boton_suma():
    numeros = obtener_numeros_complejos()
    if numeros:
     sumar_numeros_complejos(*numeros)

def boton_resta():
    numeros = obtener_numeros_complejos()
    if numeros:
        restar_numeros_complejos(*numeros)

def boton_multiplicacion():
    numeros = obtener_numeros_complejos()
    if numeros:
        multiplicar_numeros_complejos(*numeros)

def boton_division():
    numeros = obtener_numeros_complejos()
    if numeros:
        dividir_numeros_complejos(*numeros)

root = tk.Tk()
root.title("Operaciones Básicas de Números Complejos")
root.configure(background='lightgrey')

# Estilo de la interfaz
style = ttk.Style()
style.theme_use("clam")
style.configure("TLabel", font=("Algerian", 16, "bold"), foreground="green")
style.configure("TButton", font=("Arial", 12, "bold"))

# Marco principal
mainframe = ttk.Frame(root, padding="20")
mainframe.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

# Título
titulo_label = ttk.Label(mainframe, text="Operaciones Básicas de Números Complejos", font=("Algerian", 16, "bold"), foreground="cyan")
titulo_label.grid(row=0, column=0, columnspan=5, pady=10)

# Etiquetas y campos de entrada
label_z1 = ttk.Label(mainframe, text="Z1 = ")
label_z1.grid(row=1, column=0, padx=5, pady=5)

entry_z1_real = ttk.Entry(mainframe, width=5)
entry_z1_real.grid(row=1, column=1, padx=5, pady=5)

label_z1_real = ttk.Label(mainframe, text="+", foreground="blue")
label_z1_real.grid(row=1, column=2, padx=5, pady=5)

entry_z1_imag = ttk.Entry(mainframe, width=5)
entry_z1_imag.grid(row=1, column=3, padx=5, pady=5)

label_z1_imag = ttk.Label(mainframe, text="i", foreground="red")
label_z1_imag.grid(row=1, column=4, padx=5, pady=5)

label_z2 = ttk.Label(mainframe, text="Z2 = ")
label_z2.grid(row=2, column=0, padx=5, pady=5)

entry_z2_real = ttk.Entry(mainframe, width=5)
entry_z2_real.grid(row=2, column=1, padx=5, pady=5)

label_z2_real = ttk.Label(mainframe, text="+", foreground="green")
label_z2_real.grid(row=2, column=2, padx=5, pady=5)

entry_z2_imag = ttk.Entry(mainframe, width=5)
entry_z2_imag.grid(row=2, column=3, padx=5, pady=5)

label_z2_imag = ttk.Label(mainframe, text="i", foreground="orange")
label_z2_imag.grid(row=2, column=4, padx=5, pady=5)

# Botones
boton_suma = tk.Button(mainframe, text="Sumar", command=boton_suma, font=("Arial", 12, "bold"), foreground="cyan", background="purple")
boton_suma.grid(row=3, column=0, padx=5, pady=5)

boton_resta = tk.Button(mainframe, text="Restar", command=boton_resta, font=("Arial", 12, "bold"), foreground="magenta", background="yellow")
boton_resta.grid(row=3, column=1, padx=5, pady=5)

boton_multiplicacion = tk.Button(mainframe, text="Multiplicar", command=boton_multiplicacion, font=("Arial", 12, "bold"), foreground="red", background="blue")
boton_multiplicacion.grid(row=3, column=2, padx=5, pady=5)

boton_division = tk.Button(mainframe, text="Dividir", command=boton_division, font=("Arial", 12, "bold"), foreground="orange", background="green")
boton_division.grid(row=3, column=3, padx=5, pady=5)

resultado_label = ttk.Label(mainframe, text="", font=("Arial", 12))
resultado_label.grid(row=4, column=0, columnspan=5, padx=5, pady=5)

root.mainloop()