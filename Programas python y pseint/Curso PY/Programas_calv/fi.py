import numpy as np
import matplotlib.pyplot as plt

# Definir el rango de valores de theta
theta = np.linspace(0, 2 * np.pi, 1000)

# Calcular la función R(theta) = 1 / (1 - cos(theta))
R = 1 / (1 - np.cos(theta))

# Evitar valores muy grandes (cerca de 0) para mejorar la visualización
R[np.abs(R) > 10] = np.nan  # Asignar NaN para valores muy grandes

# Graficar la función
plt.plot(theta, R, label=r'$R(\theta) = \frac{1}{1 - \cos(\theta)}$')
plt.title("Gráfico de la función rectangular R(θ)")
plt.xlabel(r'$\theta$')
plt.ylabel(r'$R(\theta)$')
plt.grid(True)
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.legend()
plt.show()