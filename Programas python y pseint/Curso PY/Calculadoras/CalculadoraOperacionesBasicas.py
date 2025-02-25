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
    label_z = ttk.Label(root, text=f"Número complejo Z{i}:", font=("Arial", 12, "bold"), foreground="black")
    label_z.grid(row=(i-1)*3, column=0, pady=5, sticky="e")
    labels_z.append(label_z)
    
    # Parte real
    label_z_real = ttk.Label(root, text="Parte real:", font=("Arial", 12, "bold"), foreground="black")
    label_z_real.grid(row=(i-1)*3, column=1, pady=5, sticky="w")
    entry_z_real = ttk.Entry(root)
    entry_z_real.grid(row=(i-1)*3, column=2, pady=5)
    z_entries.append(entry_z_real)
    
    # Parte imaginaria
    label_z_imag = ttk.Label(root, text="Parte imaginaria:", font=("Arial", 12, "bold"), foreground="black")
    label_z_imag.grid(row=(i-1)*3 + 1, column=1, pady=5, sticky="w")
    entry_z_imag = ttk.Entry(root)
    entry_z_imag.grid(row=(i-1)*3 + 1, column=2, pady=5)
    z_entries.append(entry_z_imag)

    # Resultado debajo de las entradas de z
    resultado_z = ttk.Label(root, text="", font=("Arial", 12), foreground="black")
    resultado_z.grid(row=(i-1)*3 + 2, column=0, columnspan=3, pady=5, padx=10, sticky="w")

# Etiqueta para mostrar la operación ingresada
etiqueta_operacion = ttk.Label(root, text="Operación:", font=("Arial", 12, "bold"), foreground="black")
etiqueta_operacion.grid(row=16, column=0, pady=5, padx=10, sticky="w")

# Pantalla para mostrar la operación en curso
pantalla_operacion = ttk.Label(root, textvariable=operacion_texto, font=("Arial", 12), foreground="black")
pantalla_operacion.grid(row=16, column=1, columnspan=2, pady=5, padx=10, sticky="w")

# Botón para guardar los números complejos
boton_guardar = ttk.Button(root, text="Guardar Números", command=guardar_numeros)
boton_guardar.grid(row=0, column=4, columnspan=3, pady=5, sticky="ew")

# Botones para manipular los valores de z y realizar operaciones
botones_z = [
    ("z1", lambda: agregar_texto("z1")),
    ("z2", lambda: agregar_texto("z2")),
    ("z3", lambda: agregar_texto("z3")),
    ("z4", lambda: agregar_texto("z4")),
    ("z5", lambda: agregar_texto("z5")),
    ("+", lambda: agregar_operacion("+")),
    ("-", lambda: agregar_operacion("-")),
    ("*", lambda: agregar_operacion("*")),
    ("/", lambda: agregar_operacion("/")),
    ("^", lambda: agregar_operacion("^")),
    ("0", lambda: agregar_texto("0")),
    ("1", lambda: agregar_texto("1")),
    ("2", lambda: agregar_texto("2")),
    ("3", lambda: agregar_texto("3")),
    ("4", lambda: agregar_texto("4")),
    ("5", lambda: agregar_texto("5")),
    ("6", lambda: agregar_texto("6")),
    ("7", lambda: agregar_texto("7")),
    ("8", lambda: agregar_texto("8")),
    ("9", lambda: agregar_texto("9")),
    ("Borrar", borrar),
    ("=", calcular)
]

row = 0
col = 3

# Crear botones
for texto, comando in botones_z:
    ttk.Button(root, text=texto, command=comando).grid(row=row, column=col, padx=5, pady=5)
    row += 1
    if row > 6:
        row = 1
        col += 1

# Botón para limpiar la pantalla y los campos de entrada
boton_refrescar = ttk.Button(root, text="Refrescar", command=refrescar)
boton_refrescar.grid(row=7, column=3, columnspan=3, pady=5, sticky="ew")

# Etiqueta para mostrar el resultado de la operación
resultado_rectangular = ttk.Label(root, text="", font=("Arial", 12, "bold"), foreground="black")
resultado_rectangular.grid(row=17, column=0, columnspan=6, pady=5, padx=10, sticky="w")

root.mainloop()