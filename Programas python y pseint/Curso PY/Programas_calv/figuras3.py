import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Configuración de la figura 3D
fig = plt.figure(figsize=(12, 10))
ax = fig.add_subplot(111, projection='3d')

# a) (2cos(t), 2sen(t), t) 0<=t<=2π
t_a = np.linspace(0, 2*np.pi, 100)
x_a = 2 * np.cos(t_a)
y_a = 2 * np.sin(t_a)
z_a = t_a
ax.plot(x_a, y_a, z_a, label='(2cos(t), 2sin(t), t)', color='b')

# b) (1, 3t^2, t^3) 0<=t<=1
t_b = np.linspace(0, 1, 100)
x_b = np.ones_like(t_b)
y_b = 3 * t_b**2
z_b = t_b**3
ax.plot(x_b, y_b, z_b, label='(1, 3t^2, t^3)', color='g')

# c) (sen(3t), cos(3t), 2t^(3/2)) 0<=t<=1
t_c = np.linspace(0, 1, 100)
x_c = np.sin(3*t_c)
y_c = np.cos(3*t_c)
z_c = 2 * t_c**(3/2)
ax.plot(x_c, y_c, z_c, label='(sin(3t), cos(3t), 2t^(3/2))', color='r')

# d) (t, t, t^2) 1<=t<=2
t_d = np.linspace(1, 2, 100)
x_d = t_d
y_d = t_d
z_d = t_d**2
ax.plot(x_d, y_d, z_d, label='(t, t, t^2)', color='c')

# e) (t, tsen(t), tcos(t)) 0<=t<=π
t_e = np.linspace(0, np.pi, 100)
x_e = t_e
y_e = t_e * np.sin(t_e)
z_e = t_e * np.cos(t_e)
ax.plot(x_e, y_e, z_e, label='(t, tsin(t), tcos(t))', color='m')

# Configuración de la gráfica
ax.set_title('Curvas 3D')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend()

plt.show()