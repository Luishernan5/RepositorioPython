import numpy as np

def imprimir_valores(matriz_resultados):
    try:
        # Imprimir los valores de X e Y
        print(f"El valor de X es: {matriz_resultados[0][0]}")
        print(f"El valor de Y es: {matriz_resultados[1][0]}")

    except IndexError:
        print("La matriz de resultados no tiene el formato adecuado.")

# Ejercicio 1
matriz_resultados_1 = np.array([[-4], [22]])

print("Para el primer ejercicio:")
imprimir_valores(matriz_resultados_1)

# Ejercicio 2
matriz_resultados_2 = np.array([[13], [12]])

print("\nPara el segundo ejercicio:")
imprimir_valores(matriz_resultados_2)
