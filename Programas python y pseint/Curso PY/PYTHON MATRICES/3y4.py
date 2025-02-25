import numpy as np

def imprimir_valores(matriz_resultados):
    try:
        # Imprimir los valores de X e Y
        for i, valor in enumerate(matriz_resultados):
            if i % 2 == 0:
                print(f"El valor de X{i//2+1} es: {valor[0]}")
            else:
                print(f"El valor de Y{i//2+1} es: {valor[0]}")

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

# Ejercicio 3
matriz_resultados_3 = np.array([[2], [3], [2]])

print("\nPara el tercer ejercicio:")
imprimir_valores(matriz_resultados_3)

# Ejercicio 4
matriz_resultados_4 = np.array([[2], [9], [2], [9]])

print("\nPara el cuarto ejercicio:")
imprimir_valores(matriz_resultados_4)
