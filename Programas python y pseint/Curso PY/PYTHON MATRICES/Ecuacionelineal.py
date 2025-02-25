import tkinter as tk  # Importar la biblioteca tkinter para la interfaz gráfica
from tkinter import ttk  # Importar ttk para estilos de widgets
import numpy as np  # Importar numpy para cálculos numéricos
from numpy.linalg import solve  # Importar la función solve de numpy.linalg para resolver sistemas de ecuaciones lineales
from fractions import Fraction  # Importar Fraction de fractions para manejar números fraccionarios
import matplotlib.pyplot as plt  # Importar pyplot de matplotlib para graficar

# Función para preguntar al usuario las dimensiones del vector w
def preguntar_dimensiones_w():
    global w_entry, w_dimension  # Variables globales para almacenar la entrada del usuario
    # Etiqueta para preguntar al usuario sobre la dimensión del vector w
    etiqueta_dimension_w = tk.Label(w_frame, text="¿Cuántas coordenadas tendrá el vector w?", font=('Courier New', 12), foreground="black", background="lightgreen")
    etiqueta_dimension_w.grid(row=0, column=0, sticky="w")  # Colocar la etiqueta en la interfaz gráfica
    # Entrada para que el usuario ingrese la dimensión del vector w
    entrada_dimension_w = tk.Entry(w_frame, font=('Courier New', 12), background="cyan")
    entrada_dimension_w.grid(row=0, column=1)  # Colocar la entrada en la interfaz gráfica
    
    # Función interna para preguntar las coordenadas del vector w
    def preguntar_coordenadas_w():
        global w_entry  # Variable global para almacenar las coordenadas del vector w
        # Entrada para que el usuario ingrese las coordenadas del vector w
        w_entry = tk.Entry(w_frame, font=('Courier New', 12), background="cyan")  
        w_entry.grid(row=1, column=1)  # Colocar la entrada en la interfaz gráfica
        # Etiqueta para preguntar al usuario sobre las coordenadas del vector w
        etiqueta_coordenadas_w = tk.Label(w_frame, text=f"Ingrese las coordenadas del vector w (separadas por comas):", font=('Courier New', 12), foreground="black", background="lightgreen")
        etiqueta_coordenadas_w.grid(row=1, column=0, sticky="w")  # Colocar la etiqueta en la interfaz gráfica
        w_dimension = int(entrada_dimension_w.get())  # Obtener la dimensión del vector w
    
    # Botón para confirmar la dimensión del vector w y proceder a ingresar las coordenadas
    boton_dimension_w = tk.Button(w_frame, text="Aceptar w", command=preguntar_coordenadas_w, background="pink")
    boton_dimension_w.grid(row=0, column=2)  # Colocar el botón en la interfaz gráfica

# Función para preguntar al usuario la cantidad de vectores s que desea calcular
def preguntar_vectores_s():
    global s_entry, s_entries  # Variables globales para almacenar la entrada del usuario
    # Etiqueta para preguntar al usuario sobre la cantidad de vectores s
    etiqueta_dimension_s = tk.Label(s_frame, text="¿Cuántos vectores desea calcular?", font=('Courier New', 12), foreground="black", background="lightgreen")
    etiqueta_dimension_s.grid(row=0, column=0, sticky="w")  # Colocar la etiqueta en la interfaz gráfica
    # Entrada para que el usuario ingrese la cantidad de vectores s
    entrada_dimension_s = tk.Entry(s_frame, font=('Courier New', 12), background="cyan")
    entrada_dimension_s.grid(row=0, column=1)  # Colocar la entrada en la interfaz gráfica
    
    # Función interna para crear campos de entrada para los vectores s
    def crear_campos_entrada_s():
        global s_entries  # Variable global para almacenar las entradas de los vectores s
        s_entries = []  # Lista para almacenar las entradas de los vectores s
        # Iterar sobre la cantidad de vectores ingresados por el usuario
        for i in range(int(entrada_dimension_s.get())):
            # Etiqueta para preguntar al usuario sobre las coordenadas del vector s
            etiqueta_vector_s = tk.Label(s_frame, text=f"Ingrese las coordenadas del vector s{i+1} (separadas por comas):", font=('Courier New', 12), foreground="black", background="lightgreen")
            etiqueta_vector_s.grid(row=i+1, column=0, sticky="w")  # Colocar la etiqueta en la interfaz gráfica
            # Entrada para que el usuario ingrese las coordenadas del vector s
            entrada_vector_s = tk.Entry(s_frame, font=('Courier New', 12), background="cyan")  
            entrada_vector_s.grid(row=i+1, column=1)  # Colocar la entrada en la interfaz gráfica
            s_entries.append(entrada_vector_s)  # Agregar la entrada a la lista de entradas de los vectores s
    
    # Botón para confirmar la cantidad de vectores s y proceder a ingresar las coordenadas
    boton_dimension_s = tk.Button(s_frame, text="Aceptar s", command=crear_campos_entrada_s, background="pink")
    boton_dimension_s.grid(row=0, column=2)  # Colocar el botón en la interfaz gráfica

# Función para resolver las ecuaciones lineales y mostrar los resultados
def resolver_ecuaciones():
    w_values = [Fraction(value) for value in w_entry.get().split(",")]  # Obtener las coordenadas del vector w
    w = np.array(w_values, dtype=float)  # Convertir a float
    
    A = []  # Lista para almacenar los coeficientes de los vectores s
    b = []  # Lista para almacenar los resultados de las ecuaciones lineales
    
    # Iterar sobre las entradas de los vectores s
    for entry in s_entries:
        vector_values = [Fraction(value) for value in entry.get().split(",")]  # Obtener las coordenadas del vector s
        A.append(vector_values)  # Agregar las coordenadas del vector s como coeficientes
        b.append(np.dot(w, vector_values))  # Calcular el resultado de la ecuación lineal
    
    A = np.array(A, dtype=float)  # Convertir los coeficientes a float
    b = np.array(b, dtype=float)  # Convertir los resultados a float
    
    x = solve(A, b)  # Resolver el sistema de ecuaciones lineales
    
    texto_resultados.delete('1.0', tk.END)  # Limpiar resultados anteriores
    
    # Mostrar los resultados en la interfaz gráfica
    for i, c in enumerate(x):
        texto_resultados.insert(tk.END, f"c{i+1} = {c}\n")
        
    # Imprimir ecuaciones lineales
    texto_ecuaciones.delete('1.0', tk.END)  # Limpiar resultados anteriores
    
    # Mostrar las ecuaciones lineales en la interfaz gráfica
    for i, entry in enumerate(s_entries):
        vector_values = [Fraction(value) for value in entry.get().split(",")]  # Obtener las coordenadas del vector s
        equation_str = f"{w.dot(vector_values)} = "  # Construir la ecuación lineal
        for j, value in enumerate(vector_values):
            equation_str += f"{value}*c{j+1} + "  # Agregar términos a la ecuación lineal
        equation_str = equation_str[:-3]  # Eliminar el último signo de suma
        texto_ecuaciones.insert(tk.END, f"{equation_str}\n")  # Mostrar la ecuación lineal en la interfaz gráfica

# Función para graficar los resultados
def graficar_resultados():
    # Coeficientes de la solución
    results = [Fraction(result.split('=')[-1].strip()) for result in texto_resultados.get('1.0', tk.END).split('\n') if result]
    
    # Coordenadas de los vectores w y s
    w_values = [Fraction(value) for value in w_entry.get().split(",")]
    w = np.array(w_values, dtype=float)  # Convertir a float
    
    s_coordinates = []  # Lista para almacenar las coordenadas de los vectores s
    for entry in s_entries:
        vector_values = [Fraction(value) for value in entry.get().split(",")]  # Obtener las coordenadas del vector s
        s_coordinates.append(vector_values)  # Agregar las coordenadas del vector s
    
    # Graficar los triángulos formados por los vectores w y s
    plt.figure()
    colors = ['b', 'g', 'r', 'c', 'm', 'y']  # Lista de colores para diferenciar los triángulos
    for i, s_coords in enumerate(s_coordinates):
        triangle_points = np.array([np.zeros(len(w)), w, w + s_coords, np.zeros(len(w))])  # Coordenadas de los puntos extremos del triángulo
        plt.plot(triangle_points[:,0], triangle_points[:,1], color=colors[i%len(colors)], linestyle='-')
        plt.fill(triangle_points[:,0], triangle_points[:,1], color=colors[i%len(colors)], alpha=0.3)
        # Etiquetas de los vectores
        plt.text(w[0], w[1], f'w ({w[0]}, {w[1]})', fontsize=9, color='red')
        plt.text(w[0] + s_coords[0], w[1] + s_coords[1], f's{i+1} ({w[0] + s_coords[0]}, {w[1] + s_coords[1]})', fontsize=9, color='cyan')
    plt.xlabel('Componente 1')
    plt.ylabel('Componente 2')
    plt.title('Triángulos formados por los vectores w y s')
    plt.grid(True)
    plt.show()

root = tk.Tk()  # Crear la ventana principal
root.title("Resolutor de Espacio Vectorial")  # Establecer el título de la ventana
root.configure(background='yellow')  # Establecer el color de fondo de la ventana

# Parte 1: Botones de acción
action_frame = tk.Frame(root, background='cyan')  # Crear un marco para los botones
action_frame.grid(row=0, column=0, padx=10, pady=10, sticky="w")  # Colocar el marco en la ventana

# Botones para definir w, s, resolver ecuaciones y graficar resultados
boton_dimension_w = tk.Button(action_frame, text="Definir w", command=preguntar_dimensiones_w, background="pink")
boton_dimension_w.grid(row=0, column=0, padx=5, pady=5)

boton_dimension_s = tk.Button(action_frame, text="Definir vectores s", command=preguntar_vectores_s, background="pink")
boton_dimension_s.grid(row=0, column=1, padx=5, pady=5)

boton_resolver = tk.Button(action_frame, text="Resolver", command=resolver_ecuaciones, background="pink")
boton_resolver.grid(row=0, column=2, padx=5, pady=5)

boton_graficar = tk.Button(action_frame, text="Graficar", command=graficar_resultados, background="pink")
boton_graficar.grid(row=0, column=3, padx=5, pady=5)

# Parte 2: Ingresar w
w_frame = tk.Frame(root, background="lightgreen")  # Crear un marco para ingresar w
w_frame.grid(row=1, column=0, padx=10, pady=10, sticky="w")  # Colocar el marco en la ventana

# Parte 3: Ingresar s
s_frame = tk.Frame(root, background="lightgreen")  # Crear un marco para ingresar s
s_frame.grid(row=2, column=0, padx=10, pady=10, sticky="w")  # Colocar el marco en la ventana

# Parte 4: Resultados
results_frame = tk.Frame(root, background="lightgreen")  # Crear un marco para los resultados
results_frame.grid(row=3, column=0, padx=10, pady=10, sticky="w")  # Colocar el marco en la ventana

# Etiquetas para los resultados y ecuaciones lineales
etiqueta_resultados = tk.Label(results_frame, text="Resultados:", font=('Courier New', 12), foreground="red")
etiqueta_resultados.grid(row=0, column=0, sticky="w")

texto_resultados = tk.Text(results_frame, height=3, width=30, background="pink")
texto_resultados.grid(row=1, column=0, padx=5, pady=5, sticky="w")

etiqueta_ecuaciones = tk.Label(results_frame, text="Ecuaciones Lineales:", font=('Courier New', 12), foreground="red")
etiqueta_ecuaciones.grid(row=2, column=0, sticky="w")

texto_ecuaciones = tk.Text(results_frame, height=5, width=50, background="pink")
texto_ecuaciones.grid(row=3, column=0, padx=5, pady=5, sticky="w")

root.mainloop()  # Iniciar el bucle de eventos
