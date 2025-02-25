import tkinter as tk
from tkinter import ttk
import cmath

# Definición de la variable operacion
operacion = []

def forma_polar(num_complejo):
    magnitud = abs(num_complejo)
    angulo_rad = cmath.phase(num_complejo)
    angulo_grados = angulo_rad * (180 / cmath.pi)
    
    # Redondear los grados a enteros si son números cercanos
    angulo_grados_entero = round(angulo_grados)
    
    return [magnitud, angulo_grados_entero, angulo_rad]

def forma_rectangular(num_complejo):
    return f"{num_complejo.real} + {num_complejo.imag}j"

def agregar_texto(texto):
    if texto.isdigit() or texto.startswith('z'):
        operacion.append(texto)
    elif texto == "^":
        operacion.append("")  # Usar '' para el operador de potencia en la expresión evaluada
    else:
        operacion.append(" " + texto + " ")
    operacion_texto.set("".join(operacion))

def borrar():
    if operacion:
        operacion.pop()
        operacion_texto.set("".join(operacion))

def guardar_numeros():
    global z1, z2, z3, z4, z5
    z_values = []
    for i in range(0, len(z_entries), 2):
        real_part = z_entries[i].get()
        imag_part = z_entries[i+1].get()
        z = complex(real_part) + complex(imag_part) * 1j
        z_values.append(z)
    z1, z2, z3, z4, z5 = z_values[:5]
    print("Valores de z1, z2, z3, z4, z5:", z1, z2, z3, z4, z5)

def calcular():
    global z1, z2, z3, z4, z5
    try:
        expr = "".join(operacion)
        print("Expresión a evaluar:", expr)
        resultado = complex(eval(expr, {"z1": z1, "z2": z2, "z3": z3, "z4": z4, "z5": z5}))  # Evaluar y convertir a número complejo
        
        if isinstance(resultado, complex):
            forma_polar_resultado = forma_polar(resultado)
            magnitud, grados, radianes = forma_polar_resultado
            
            resultado_polar.config(text=f"Magnitud: {magnitud}\nGrados: {grados}\nRadianes: {radianes}", foreground="black")
            resultado_rectangular.config(text=f"Rectangular: {forma_rectangular(resultado)}", foreground="black")
        else:
            resultado_polar.config(text="Error: El resultado no es un número complejo", foreground="black")
            resultado_rectangular.config(text="", foreground="black")
    except Exception as e:
        print("Excepción al calcular la expresión:", e)
        resultado_polar.config(text="Error al calcular la expresión", foreground="black")
        resultado_rectangular.config(text="", foreground="black")

def refrescar():
    operacion.clear()
    operacion_texto.set("")
    resultado_polar.config(text="", foreground="black")
    resultado_rectangular.config(text="", foreground="black")
    for entry in z_entries:
        entry.delete(0, 'end')

root = tk.Tk()
root.title("Calculadora de Forma Polar")

# Definición de la variable operacion_texto
operacion_texto = tk.StringVar()

# Creación de las entradas para los números complejos
labels_z = []
z_entries = []
for i in range(1, 6):
    label_z = ttk.Label(root, text=f"Número complejo Z{i}:", font=("Times New Roman", 12, "bold"), foreground="black")
    label_z.grid(row=(i-1)*2, column=0, pady=5, sticky="e")
    labels_z.append(label_z)
    
    label_z_real = ttk.Label(root, text="Parte real:", font=("Times New Roman", 12, "bold"), foreground="black")
    label_z_real.grid(row=(i-1)*2, column=1, pady=5, sticky="w")
    entry_z_real = ttk.Entry(root)
    entry_z_real.grid(row=(i-1)*2, column=2, pady=5)
    z_entries.append(entry_z_real)
    
    label_z_imag = ttk.Label(root, text="Parte imaginaria:", font=("Times New Roman", 12, "bold"), foreground="black")
    label_z_imag.grid(row=(i-1)*2 + 1, column=1, pady=5, sticky="w")
    entry_z_imag = ttk.Entry(root)
    entry_z_imag.grid(row=(i-1)*2 + 1, column=2, pady=5)
    z_entries.append(entry_z_imag)

# Botones para manipular los valores de z y realizar operaciones
botones_z = [
    ("z1", lambda: agregar_texto("z1")),
    ("z2", lambda: agregar_texto("z2")),
    ("z3", lambda: agregar_texto("z3")),
    ("z4", lambda: agregar_texto("z4")),
    ("z5", lambda: agregar_texto("z5")),
    ("+", lambda: agregar_texto("+")),
    ("-", lambda: agregar_texto("-")),
    ("", lambda: agregar_texto("")),
    ("/", lambda: agregar_texto("/")),
    ("^", lambda: agregar_texto("^")),
    ("(", lambda: agregar_texto("(")),
    (")", lambda: agregar_texto(")")),
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

row = 12
col = 3

# Crear un estilo personalizado para los botones
style = ttk.Style()

style.configure("Custom.TButton", font=("Arial", 12), foreground="black", background="yellow")
style.configure("Red.TButton", font=("Arial", 12, "bold"), foreground="black", background="red")

# Crear los botones con el estilo personalizado
for texto, comando in botones_z:
    ttk.Button(root, text=texto, command=comando, style="Custom.TButton").grid(row=row, column=col, padx=5, pady=5)
    row += 1
    if row > 17:
        row = 12
        col += 1

# Botón para guardar los números complejos
boton_guardar = ttk.Button(root, text="Guardar Números", command=guardar_numeros, style="Red.TButton")
boton_guardar.grid(row=11, column=0, columnspan=3, pady=5, sticky="ew")

# Botón para refrescar la pantalla y limpiar los valores
boton_refrescar = ttk.Button(root, text="Refrescar", command=refrescar, style="Custom.TButton")
boton_refrescar.grid(row=11, column=4, columnspan=3, pady=5, sticky="ew")

# Etiqueta para mostrar la operación y el resultado en forma polar
ttk.Label(root, textvariable=operacion_texto, font=("Courier New", 12, "bold"), foreground="black").grid(row=12, column=0, columnspan=6, pady=5, padx=10, sticky="w")

# Resultado en forma polar
resultado_polar = ttk.Label(root, text="", font=("Times New Roman", 12, "bold"), foreground="black")
resultado_polar.grid(row=13, column=0, columnspan=6, pady=5, padx=10, sticky="w")

# Resultado en forma rectangular
resultado_rectangular = ttk.Label(root, text="", font=("Times New Roman", 12, "bold"), foreground="black")
resultado_rectangular.grid(row=14, column=0, columnspan=6, pady=5, padx=10, sticky="w")

root.mainloop()