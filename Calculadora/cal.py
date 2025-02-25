import tkinter as tk
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Funciones para cálculos
def suma_vectores(v1, v2):
    return np.add(v1, v2)

def resta_vectores(v1, v2):
    return np.subtract(v1, v2)

def producto_punto(v1, v2):
    return np.dot(v1, v2)

def producto_cruz(v1, v2):
    return np.cross(v1, v2)

def graficar_vectores(v1, v2, resultado=None, operacion=""):
    try:
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        # Origen
        origen = [0, 0, 0]

        # Graficar vectores
        ax.quiver(*origen, *v1, color='red', label='Vector 1')
        ax.quiver(*origen, *v2, color='green', label='Vector 2')
        if resultado is not None:
            ax.quiver(*origen, *resultado, color='blue', label=f'Resultado ({operacion})')

        # Configuración de la gráfica
        ax.set_xlim([min(0, v1[0], v2[0]), max(v1[0], v2[0])])
        ax.set_ylim([min(0, v1[1], v2[1]), max(v1[1], v2[1])])
        ax.set_zlim([min(0, v1[2], v2[2]), max(v1[2], v2[2])])
        ax.set_title(f"Gráfica de Vectores - {operacion}")
        ax.set_xlabel("X")
        ax.set_ylabel("Y")
        ax.set_zlabel("Z")
        ax.legend()

        plt.show()
    except Exception as e:
        messagebox.showerror("Error", str(e))

def graficar_parametrica(rango):
    t = np.linspace(rango[0], rango[1], 100)
    x = np.sin(t)
    y = np.cos(t)
    z = t

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(x, y, z, label="Curva Paramétrica", color='blue')
    ax.set_title("Curva Paramétrica")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    ax.legend()
    plt.show()

def graficar_polar():
    theta = np.linspace(0, 2 * np.pi, 100)
    r = 1 + np.sin(4 * theta)

    plt.figure()
    plt.polar(theta, r, color='magenta')
    plt.title("Curva Polar")
    plt.show()

# Interfaz gráfica
def crear_interfaz():
    def obtener_vectores():
        try:
            v1 = list(map(float, entry_v1.get().split(',')))
            v2 = list(map(float, entry_v2.get().split(',')))
            return np.array(v1), np.array(v2)
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingresa los vectores en formato correcto (ej. 1,2,3).")
            return None, None

    def realizar_operacion(operacion):
        v1, v2 = obtener_vectores()
        if v1 is None or v2 is None:
            return

        try:
            if operacion == "suma":
                resultado = suma_vectores(v1, v2)
                messagebox.showinfo("Resultado", f"La suma de los vectores es: {resultado}")
                graficar_vectores(v1, v2, resultado, "Suma")
            elif operacion == "resta":
                resultado = resta_vectores(v1, v2)
                messagebox.showinfo("Resultado", f"La resta de los vectores es: {resultado}")
                graficar_vectores(v1, v2, resultado, "Resta")
            elif operacion == "punto":
                resultado = producto_punto(v1, v2)
                messagebox.showinfo("Resultado", f"El producto punto es: {resultado}")
            elif operacion == "cruz":
                resultado = producto_cruz(v1, v2)
                graficar_vectores(v1, v2, resultado, "Producto Cruz")
            elif operacion == "graficar_vectores":
                graficar_vectores(v1, v2)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def graficar_curva_parametrica():
        try:
            rango = list(map(float, entry_rango.get().split(',')))
            if len(rango) != 2:
                raise ValueError("El rango debe tener exactamente dos valores: inicio y fin.")
            graficar_parametrica(rango)
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingresa un rango válido (ej. 0,6.28).")

    root = tk.Tk()
    root.title("Calculadora de Vectores")

    # Estilo
    label_style = {"bg": "#f0f0f0", "fg": "#333333", "font": ("Arial", 14)}
    button_style = {"bg": "#4CAF50", "fg": "#ffffff", "font": ("Arial", 12, "bold"), "width": 20}

    # Entradas
    tk.Label(root, text="Vector 1 (ej. 1,2,3):", **label_style).grid(row=0, column=0, pady=5, padx=5)
    entry_v1 = tk.Entry(root, font=("Arial", 12))
    entry_v1.grid(row=0, column=1, pady=5, padx=5)

    tk.Label(root, text="Vector 2 (ej. 1,2,3):", **label_style).grid(row=1, column=0, pady=5, padx=5)
    entry_v2 = tk.Entry(root, font=("Arial", 12))
    entry_v2.grid(row=1, column=1, pady=5, padx=5)

    tk.Label(root, text="Rango (ej. 0,6.28):", **label_style).grid(row=2, column=0, pady=5, padx=5)
    entry_rango = tk.Entry(root, font=("Arial", 12))
    entry_rango.grid(row=2, column=1, pady=5, padx=5)

    # Botones
    tk.Button(root, text="Suma de vectores", command=lambda: realizar_operacion("suma"), **button_style).grid(row=3, column=0, pady=10)
    tk.Button(root, text="Resta de vectores", command=lambda: realizar_operacion("resta"), **button_style).grid(row=3, column=1, pady=10)
    tk.Button(root, text="Producto punto", command=lambda: realizar_operacion("punto"), **button_style).grid(row=4, column=0, pady=10)
    tk.Button(root, text="Producto cruz", command=lambda: realizar_operacion("cruz"), **button_style).grid(row=4, column=1, pady=10)

    tk.Button(root, text="Graficar curva paramétrica", command=graficar_curva_parametrica, **button_style).grid(row=5, column=0, pady=10)
    tk.Button(root, text="Graficar curva polar", command=graficar_polar, **button_style).grid(row=5, column=1, pady=10)

    root.mainloop()

if __name__ == "__main__":
    crear_interfaz()