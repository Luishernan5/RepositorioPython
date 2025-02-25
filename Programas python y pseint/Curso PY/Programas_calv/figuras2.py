import numpy as np
import matplotlib.pyplot as plt

# Definición de las funciones paramétricas
def parametric_curve_a(t):
    x = np.exp(t)
    y = np.cos(t)
    return x, y

def parametric_curve_b(t):
    x = 3 * t**2
    y = t**3
    return x, y

def parametric_curve_c(t):
    x = t * np.sin(t)
    y = 4 * t
    return x, y

def parametric_curve_d(t):
    x = t**2
    y = np.exp(2) * np.ones_like(t)  # Asegurarse de que y sea un arreglo
    return x, y

# Funciones para calcular la pendiente de la recta tangente
def tangent_line_a(t):
    dx_dt = np.exp(t)
    dy_dt = -np.sin(t)
    m = dy_dt / dx_dt
    x0 = np.exp(t)
    y0 = np.cos(t)
    return m, x0, y0

def tangent_line_b(t):
    dx_dt = 6 * t
    dy_dt = 3 * t**2
    m = dy_dt / dx_dt
    x0 = 3 * t**2
    y0 = t**3
    return m, x0, y0

def tangent_line_c(t):
    dx_dt = np.sin(t) + t * np.cos(t)
    dy_dt = 4
    m = dy_dt / dx_dt
    x0 = t * np.sin(t)
    y0 = 4 * t
    return m, x0, y0

def tangent_line_d(t):
    dx_dt = 2 * t
    dy_dt = 0
    m = dy_dt / dx_dt
    x0 = t**2
    y0 = np.exp(2)  # Este valor es constante
    return m, x0, y0

# Función para graficar curvas y rectas tangentes
def plot_all_curves():
    plt.figure(figsize=(12, 8))

    # Caso A
    plt.subplot(2, 2, 1)
    t_values = np.linspace(0, 3, 100)
    x, y = parametric_curve_a(t_values)
    m, x0, y0 = tangent_line_a(np.pi / 4)
    tangent_x = np.linspace(x0 - 1, x0 + 1, 100)
    tangent_y = m * (tangent_x - x0) + y0
    plt.plot(x, y, label='Curva A: $X(t) = e^t, Y(t) = \cos(t)$', color='blue')
    plt.plot(tangent_x, tangent_y, label='Tangente', color='red', linestyle='--')
    plt.scatter([x0], [y0], color='green')  # Punto de tangencia
    plt.title('Curva y Tangente (Caso A)')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.axhline(0, color='black', lw=0.5, ls='--')
    plt.axvline(0, color='black', lw=0.5, ls='--')
    plt.grid()
    plt.legend()

    # Caso B
    plt.subplot(2, 2, 2)
    x, y = parametric_curve_b(t_values)
    m, x0, y0 = tangent_line_b(2)
    tangent_x = np.linspace(x0 - 1, x0 + 1, 100)
    tangent_y = m * (tangent_x - x0) + y0
    plt.plot(x, y, label='Curva B: $X(t) = 3t^2, Y(t) = t^3$', color='blue')
    plt.plot(tangent_x, tangent_y, label='Tangente', color='red', linestyle='--')
    plt.scatter([x0], [y0], color='green')  # Punto de tangencia
    plt.title('Curva y Tangente (Caso B)')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.axhline(0, color='black', lw=0.5, ls='--')
    plt.axvline(0, color='black', lw=0.5, ls='--')
    plt.grid()
    plt.legend()

    # Caso C
    plt.subplot(2, 2, 3)
    x, y = parametric_curve_c(t_values)
    m, x0, y0 = tangent_line_c(np.pi / 2)
    tangent_x = np.linspace(x0 - 1, x0 + 1, 100)
    tangent_y = m * (tangent_x - x0) + y0
    plt.plot(x, y, label='Curva C: $X(t) = t \sin(t), Y(t) = 4t$', color='blue')
    plt.plot(tangent_x, tangent_y, label='Tangente', color='red', linestyle='--')
    plt.scatter([x0], [y0], color='green')  # Punto de tangencia
    plt.title('Curva y Tangente (Caso C)')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.axhline(0, color='black', lw=0.5, ls='--')
    plt.axvline(0, color='black', lw=0.5, ls='--')
    plt.grid()
    plt.legend()

    # Caso D
    plt.subplot(2, 2, 4)
    x, y = parametric_curve_d(t_values)
    m, x0, y0 = tangent_line_d(1)
    tangent_x = np.linspace(x0 - 1, x0 + 1, 100)
    tangent_y = m * (tangent_x - x0) + y0
    plt.plot(x, y, label='Curva D: $X(t) = t^2, Y(t) = e^2$', color='blue')
    plt.plot(tangent_x, tangent_y, label='Tangente', color='red', linestyle='--')
    plt.scatter([x0], [y0], color='green')  # Punto de tangencia
    plt.title('Curva y Tangente (Caso D)')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.axhline(0, color='black', lw=0.5, ls='--')
    plt.axvline(0, color='black', lw=0.5, ls='--')
    plt.grid()
    plt.legend()

    plt.tight_layout()
    plt.show()

# Ejecutar la función para mostrar todas las gráficas
plot_all_curves()
