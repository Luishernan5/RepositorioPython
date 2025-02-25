import scipy.integrate as integrate
import numpy as np

# Definición de las funciones de integración
def innermost_integral(z, y):
    return z

def middle_integral(y, x):
    result, _ = integrate.quad(innermost_integral, y+1, y**2)
    return result

def outer_integral(x):
    result, _ = integrate.quad(lambda y: middle_integral(y, x), np.sqrt(x), x+2)
    return result

# Integral más externa
result, _ = integrate.quad(outer_integral, -1, 4)

print("El valor numérico de la integral triple es:", result)