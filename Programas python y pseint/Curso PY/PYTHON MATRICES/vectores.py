import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def main():
    'Preguntar al usuario si desea graficar en 2D o 3D´'
    dimension = input("¿En qué dimensión deseas graficar (2D o 3D)? ").lower()

    'Pedir al usuario las coordenadas del primer punto (A)'
    if dimension == "2d":
        x1, y1 = map(float, input("Introduce las coordenadas del primer punto (x, y) A: ").split())
    elif dimension == "3d":
        x1, y1 = map(float, input("Introduce las coordenadas del primer punto (x, y) A: ").split())
    else:
        print("Dimensión no válida.")
        return

    'Pedir al usuario las coordenadas del segundo punto (B)'
    if dimension == "2d":
        x2, y2 = map(float, input("Introduce las coordenadas del segundo punto (x, y) B: ").split())
    elif dimension == "3d":
        x2, y2 = map(float, input("Introduce las coordenadas del segundo punto (x, y) B: ").split())
    else:
        return

    'Preguntar al usuario qué operación desea realizar'
    operacion = input("Introduce la operación a realizar para obtener el vector (suma, resta o promedio): ").lower()

    'Calcular el vector resultante según la operación seleccionada'
    if operacion == "suma":
        if dimension == "2d":
            x_resultante = x1 + x2
            y_resultante = y1 + y2
        elif dimension == "3d":
            x_resultante = x1 + x2
            y_resultante = y1 + y2
            z_resultante = np.random.randint(10)
    elif operacion == "resta":
        if dimension == "2d":
            x_resultante = x2 - x1
            y_resultante = y2 - y1
        elif dimension == "3d":
            x_resultante = x2 - x1
            y_resultante = y2 - y1
            z_resultante = np.random.randint(10)
    elif operacion == "promedio":
        if dimension == "2d":
            x_resultante = (x1 + x2) / 2
            y_resultante = (y1 + y2) / 2
        elif dimension == "3d":
            x_resultante = (x1 + x2) / 2
            y_resultante = (y1 + y2) / 2
            z_resultante = np.random.randint(10)
    else:
        print("Operación no válida. Se utilizará la operación de promedio por defecto.")
        if dimension == "2d":
            x_resultante = (x1 + x2) / 2
            y_resultante = (y1 + y2) / 2
        elif dimension == "3d":
            x_resultante = (x1 + x2) / 2
            y_resultante = (y1 + y2) / 2
            z_resultante = np.random.randint(10)

    'Graficar el vector resultante en un plano 2D o 3D según la dimensión seleccionada'
    if dimension == "2d":
        plt.figure()

        'Dibujar el punto A'
        plt.plot(x1, y1, 'ro', label='Punto A')
        plt.text(x1, y1, f'({x1}, {y1})', verticalalignment='bottom')

        'Dibujar el punto B'
        plt.plot(x2, y2, 'bo', label='Punto B')
        plt.text(x2, y2, f'({x2}, {y2})', verticalalignment='bottom')

        'Dibujar el punto Z'
        plt.plot(x_resultante, y_resultante, 'go', label='Punto Z')
        plt.text(x_resultante, y_resultante, f'({x_resultante}, {y_resultante})', verticalalignment='bottom')

        'Dibujar los triángulos'
        plt.plot([x1, x2], [y1, y2], 'r-', label='Línea A-B')
        plt.plot([x1, x_resultante], [y1, y_resultante], 'b-', label='Línea A-Z')
        plt.plot([x2, x_resultante], [y2, y_resultante], 'y-', label='Línea B-Z')

        'Configuraciones de la gráfica'
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title('Vector resultante en 2D')
        plt.grid(True)
        plt.legend()

        'Mostrar la gráfica'
        plt.show()

        'Mostrar el vector resultante'
        print(f"El vector resultante es: ({x_resultante, y_resultante})")

    elif dimension == "3d":
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        'Dibujar el punto A'
        ax.scatter(x1, y1, 0, c='r', marker='o', label='Punto A')
        ax.text(x1, y1, 0, f'({x1}, {y1}, 0)', color='r')

        'Dibujar el punto B'
        ax.scatter(x2, y2, 0, c='b', marker='o', label='Punto B')
        ax.text(x2, y2, 0, f'({x2}, {y2}, 0)', color='b')

        'Calcular z_resultante si no se ha calculado aún'
        if operacion == "suma" or operacion == "resta" or operacion == "promedio":
            z_resultante = np.random.randint(10)

        'Dibujar el punto Z'
        ax.scatter(x_resultante, y_resultante, z_resultante, c='g', marker='o', label='Punto Z')
        ax.text(x_resultante, y_resultante, z_resultante, f'({x_resultante}, {y_resultante}, {z_resultante})', color='g')

        'Dibujar los triángulos'
        ax.plot([x1, x2], [y1, y2], [0, 0], c='r', label='Línea A-B')
        ax.plot([x1, x_resultante], [y1, y_resultante], [0, z_resultante], c='b', label='Línea A-Z')
        ax.plot([x2, x_resultante], [y2, y_resultante], [0, z_resultante], c='y', label='Línea B-Z')

        'Configuraciones de la gráfica'
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        ax.set_title('Vector resultante en 3D')
        ax.grid(True)
        ax.legend()

        'Mostrar la gráfica'
        plt.show()

        'Mostrar el vector resultante'
        print(f"El vector resultante es: ({x_resultante, y_resultante})")

if __name__ == "__main__":
    main()
