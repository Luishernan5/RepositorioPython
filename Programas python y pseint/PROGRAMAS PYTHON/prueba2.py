import tkinter as tk
from tkinter import ttk
from fractions import Fraction
import sympy as sp

# Lista para almacenar la operación
operacion = []

# Función para agregar texto a la operación
def agregar_texto(texto):
    operacion.append(texto)
    operacion_texto.set("".join(operacion))

# Función para borrar el último carácter de la operación
def borrar():
    if operacion:
        operacion.pop()
        operacion_texto.set("".join(operacion))

# Función para guardar los números complejos ingresados
def guardar_numeros():
    global z1, z2, z3, z4, z5
    z_values = []
    for i in range(0, len(z_entries), 2):
        real_part = z_entries[i].get()
        imag_part = z_entries[i+1].get()
        z = complex(real_part) + complex(imag_part) * 1j
        z_values.append(z)
    z1, z2, z3, z4, z5 = z_values[:5]

# Función para calcular la operación ingresada
def calcular():
    global z1, z2, z3, z4, z5
    try:
        expr = "".join(operacion)
        resultado = sp.sympify(expr, locals={"z1": z1, "z2": z2, "z3": z3, "z4": z4, "z5": z5})  # Evaluar la expresión con SymPy
        resultado_fraction = sp.nsimplify(resultado)  # Convertir el resultado en una fracción simplificada
        resultado_str = str(resultado_fraction)
        if 'I' in resultado_str:
            parte_real, parte_imaginaria = resultado_fraction.as_real_imag()
            resultado_rectangular.config(text=f"Resultado: {parte_real}{'+' if parte_imaginaria >= 0 else ''}{parte_imaginaria}/{'i' if parte_imaginaria != 1 else ''}", foreground="black")
        else:
            resultado_rectangular.config(text=f"Resultado: {resultado_fraction}", foreground="black")
    except Exception as e:
        print("Excepción al calcular la expresión:", e)
        resultado_rectangular.config(text="Error al calcular la expresión", foreground="black")

# Función para limpiar la pantalla y los campos de entrada
def refrescar():
    operacion.clear()
    operacion_texto.set("")
    resultado_rectangular.config(text="", foreground="black")
    for entry in z_entries:
        entry.delete(0, 'end')

# Función para agregar una operación a la lista y mostrarla en la pantalla de operaciones
def agregar_operacion(operador):
    operacion.append(operador)
    operacion_texto.set("".join(operacion))

# Función para calcular la potencia de un número complejo
def calcular_potencia():
    try:
        expr = "".join(operacion)
        expr_potencia = ""
        base = None
        exponente = None
        for i, char in enumerate(expr):
            if char.isdigit():
                if base is None:
                    base = expr[:i]
                if i == len(expr) - 1:
                    exponente = int(expr[i:])
            elif char == '^':
                if base is not None:
                    exponente = int(expr[i+1:])
                break
            elif base is None:
                expr_potencia += char
        if base is not None and exponente is not None:
            expr_potencia += f"({base}){exponente}"
            resultado = eval(expr_potencia, {"z1": z1, "z2": z2, "z3": z3, "z4": z4, "z5": z5})
            if isinstance(resultado, complex):
                resultado_rectangular.config(text=f"Resultado: {resultado.real} + {resultado.imag}i", foreground="black")
            else:
                resultado_rectangular.config(text=f"Resultado: {resultado}", foreground="black")
        else:
            resultado_rectangular.config(text="Error: Operación inválida", foreground="red")
    except Exception as e:
        print("Excepción al calcular la expresión:", e)
        resultado_rectangular.config(text="Error al calcular la expresión", foreground="black")

# Crear la ventana principal
root = tk.Tk()
root.title("Calculadora de Operaciones Básicas con Números Complejos")

# Definir variable para mostrar la operación
operacion_texto = tk.StringVar()

# Crear entradas para los números complejos
labels_z = []
z_entries = []
for i in range(1, 6):
    label_z = ttk.Label(root, text=f"Número complejo Z{i}:", font=("Times New Roman", 12, "bold"), foreground="brown")
    label_z.grid(row=(i-1)*3, column=0, pady=5, sticky="e")
    labels_z.append(label_z)
    
    # Parte real
    label_z_real = ttk.Label(root, text="Parte real:", font=("Times New Roman", 12, "bold"), foreground="brown")
    label_z_real.grid(row=(i-1)*3, column=1, pady=5, sticky="w")
    entry_z_real = ttk.Entry(root)
    entry_z_real.grid(row=(i-1)*3, column=2, pady=5)
    z_entries.append(entry_z_real)
    
    # Parte imaginaria
    label_z_imag = ttk.Label(root, text="Parte imaginaria:", font=("Times New Roman", 12, "bold"), foreground="brown")
    label_z_imag.grid(row=(i-1)*3 + 1, column=1, pady=5, sticky="w")
    entry_z_imag = ttk.Entry(root)
    entry_z_imag.grid(row=(i-1)*3 + 1, column=2, pady=5)
    z_entries.append(entry_z_imag)

# Etiqueta para mostrar la operación ingresada
label_operacion = ttk.Label(root, text="Operación:", font=("Times New Roman", 12, "bold"), foreground="brown")
label_operacion.grid(row=0, column=4, pady=5, sticky="w")
label_operacion.config(width=20)

# Etiqueta para mostrar el resultado en forma rectangular
resultado_rectangular = ttk.Label(root, text="", font=("Times New Roman", 12), foreground="black")
resultado_rectangular.grid(row=5, column=0, columnspan=3, pady=5, sticky="w")
resultado_rectangular.config(width=30)

# Botones de las operaciones
boton_suma = ttk.Button(root, text="+", command=lambda: agregar_operacion("+"))
boton_suma.grid(row=1, column=4, pady=5)
boton_resta = ttk.Button(root, text="-", command=lambda: agregar_operacion("-"))
boton_resta.grid(row=1, column=5, pady=5)
boton_multiplicacion = ttk.Button(root, text="", command=lambda: agregar_operacion(""))
boton_multiplicacion.grid(row=2, column=4, pady=5)
boton_division = ttk.Button(root, text="/", command=lambda: agregar_operacion("/"))
boton_division.grid(row=2, column=5, pady=5)
boton_potencia = ttk.Button(root, text="^", command=lambda: agregar_operacion("^"))
boton_potencia.grid(row=3, column=4, pady=5)

# Botón para calcular el resultado
boton_calcular = ttk.Button(root, text="Calcular", command=calcular)
boton_calcular.grid(row=4, column=4, columnspan=2, pady=5)

# Botón para limpiar la pantalla y los campos de entrada
boton_limpiar = ttk.Button(root, text="Limpiar", command=refrescar)
boton_limpiar.grid(row=4, column=6, pady=5)

# Estilo para el botón Limpiar
style = ttk.Style()
style.configure("TButton", foreground="brown")

root.mainloop()