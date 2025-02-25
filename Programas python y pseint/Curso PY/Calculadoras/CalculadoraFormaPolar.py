import tkinter as tk
from tkinter import ttk
import cmath
import fractions

operacion = []
def forma_polar_decimal(num_complejo):
    magnitud = f"√{num_complejo.real ** 2 + num_complejo.imag ** 2}"
    angulo_rad = cmath.phase(num_complejo)
    angulo_grados = angulo_rad * (180 / cmath.pi)
    angulo_grados_entero = round(angulo_grados)
    return [magnitud, angulo_grados_entero, angulo_rad]
def forma_polar_fraccion(num_complejo):
    magnitud = f"√{num_complejo.real ** 2 + num_complejo.imag ** 2}"
    angulo_rad = cmath.phase(num_complejo)
    angulo_grados = angulo_rad * (180 / cmath.pi)
    # Redondear los grados a enteros si son números cercanos
    angulo_grados_entero = round(angulo_grados)
    angulo_fraccion = fractions.Fraction(angulo_rad / cmath.pi).limit_denominator()
    angulo_str = f"{angulo_fraccion.numerator}π/{angulo_fraccion.denominator}" if angulo_fraccion != 0 else "0"
    return [magnitud, angulo_grados_entero, angulo_str]
def forma_rectangular(num_complejo):
    return f"{num_complejo.real} + {num_complejo.imag}j"
def agregar_texto(texto):
    if texto.isdigit() or texto.startswith('z'):
        operacion.append(texto)
    elif texto == "^":
        operacion.append("**")  
    elif texto == "√":
        operacion.append("**0.5")
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
def calcular():
    global z1, z2, z3, z4, z5
    try:
        expr = "".join(operacion)
        resultado = complex(eval(expr, {"z1": z1, "z2": z2, "z3": z3, "z4": z4, "z5": z5}))  
        if isinstance(resultado, complex):
            forma_polar_decimal_resultado = forma_polar_decimal(resultado)
            forma_polar_fraccion_resultado = forma_polar_fraccion(resultado)
            magnitud_decimal, grados_decimal, radianes_decimal = forma_polar_decimal_resultado
            magnitud_fraccion, grados_fraccion, radianes_fraccion = forma_polar_fraccion_resultado
            
            resultado_polar_decimal.config(text=f"Magnitud: {magnitud_decimal}\nGrados: {grados_decimal}\nRadianes: {radianes_decimal}", foreground="black")
            resultado_polar_fraccion.config(text=f"Magnitud: {magnitud_fraccion}\nGrados: {grados_fraccion}\nRadianes: {radianes_fraccion}", foreground="black")
            resultado_rectangular.config(text=f"Rectangular: {forma_rectangular(resultado)}", foreground="black")
        else:
            resultado_polar_decimal.config(text="Error: El resultado no es un número complejo", foreground="black")
            resultado_polar_fraccion.config(text="Error: El resultado no es un número complejo", foreground="black")
            resultado_rectangular.config(text="", foreground="black")
    except Exception as e:
        print("Excepción al calcular la expresión:", e)
        resultado_polar_decimal.config(text="Error al calcular la expresión", foreground="black")
        resultado_polar_fraccion.config(text="Error al calcular la expresión", foreground="black")
        resultado_rectangular.config(text="",        foreground="black")
def refrescar():
    operacion.clear()
    operacion_texto.set("")
    resultado_polar_decimal.config(text="", foreground="black")
    resultado_polar_fraccion.config(text="", foreground="black")
    resultado_rectangular.config(text="", foreground="black")
    for entry in z_entries:
        entry.delete(0, 'end')
root = tk.Tk()
root.title("Calculadora de Forma Polar")
operacion_texto = tk.StringVar()
labels_z = []
z_entries = []
for i in range(1, 6):
    label_z = ttk.Label(root, text=f"Número complejo Z{i}:", font=("Times New Roman", 12, "bold"), foreground="brown")
    label_z.grid(row=(i-1)*2, column=0, pady=5, sticky="e")
    labels_z.append(label_z)
    label_z_real = ttk.Label(root, text="Parte real:", font=("Times New Roman", 12, "bold"), foreground="brown")
    label_z_real.grid(row=(i-1)*2, column=1, pady=5, sticky="w")
    entry_z_real = ttk.Entry(root)
    entry_z_real.grid(row=(i-1)*2, column=2, pady=5)
    z_entries.append(entry_z_real)
    label_z_imag = ttk.Label(root, text="Parte imaginaria:", font=("Times New Roman", 12, "bold"), foreground="brown")
    label_z_imag.grid(row=(i-1)*2 + 1, column=1, pady=5, sticky="w")
    entry_z_imag = ttk.Entry(root)
    entry_z_imag.grid(row=(i-1)*2 + 1, column=2, pady=5)
    z_entries.append(entry_z_imag)
etiqueta_operacion = ttk.Label(root, text="Operaciónes:", font=("Times New Roman", 12, "bold"), foreground="brown")
etiqueta_operacion.grid(row=1, column=14, pady=5, padx=10, sticky="e")
pantalla_operacion = ttk.Label(root, textvariable=operacion_texto, font=("Arial", 12), foreground="black")
pantalla_operacion.grid(row=1, column=15, rowspan=2, pady=5, padx=10, sticky="w")
botones_z = [
    ("z1", lambda: agregar_texto("z1")),
    ("z2", lambda: agregar_texto("z2")),
    ("z3", lambda: agregar_texto("z3")),
    ("z4", lambda: agregar_texto("z4")),
    ("z5", lambda: agregar_texto("z5")),
    ("+", lambda: agregar_texto("+")),
    ("-", lambda: agregar_texto("-")),
    ("*", lambda: agregar_texto("*")),
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
row = 1
col = 5
style = ttk.Style()
style.configure("Custom.TButton", font=("Arial", 12), foreground="blue", background="green")
style.configure("Red.TButton", font=("Arial", 12, "bold"), foreground="brown", background="red")
for texto, comando in botones_z:
    ttk.Button(root, text=texto, command=comando, style="Custom.TButton").grid(row=row, column=col, padx=5, pady=5)
    row += 1
    if row > 7:
        row = 2
        col += 2
boton_guardar = ttk.Button(root, text="Guardar Números", command=guardar_numeros, style="Red.TButton")
boton_guardar.grid(row=1, column=7, columnspan=3, pady=5, sticky="ew")
boton_refrescar = ttk.Button(root, text="Refrescar", command=refrescar, style="Custom.TButton")
boton_refrescar.grid(row=1, column=11, columnspan=3, pady=5, sticky="ew")
resultado_polar_decimal = ttk.Label(root, text="", font=("Times New Roman", 12, "bold"), foreground="black")
resultado_polar_decimal.grid(row=13, column=0, columnspan=6, pady=5, padx=10, sticky="w")
resultado_polar_fraccion = ttk.Label(root, text="", font=("Times New Roman", 12, "bold"), foreground="black")
resultado_polar_fraccion.grid(row=14, column=0, columnspan=6, pady=5, padx=10, sticky="w")
resultado_radianes_pi = ttk.Label(root, text="", font=("Times New Roman", 12, "bold"), foreground="black")
resultado_radianes_pi.grid(row=15, column=0, columnspan=6, pady=5, padx=10, sticky="w")
resultado_rectangular = ttk.Label(root, text="", font=("Times New Roman", 12, "bold"), foreground="black")
resultado_rectangular.grid(row=16, column=0, columnspan=6, pady=5, padx=10, sticky="w")

root.mainloop()