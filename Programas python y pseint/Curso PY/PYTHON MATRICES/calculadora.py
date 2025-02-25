import numpy as np

# Función para encontrar la matriz A' que cumple con la operación A' * A = A_prima_resultado
def encontrar_A_prima(A, A_prima_resultado):
    A_prima = np.dot(A_prima_resultado, np.linalg.inv(A))
    return A_prima

# Función principal
def main():
    # Ingresa el tamaño de la matriz A
    filas_A = int(input("Ingrese el número de filas de la matriz A: "))
    columnas_A = int(input("Ingrese el número de columnas de la matriz A: "))
    
    # Ingresa la matriz A
    print("Ingrese los elementos de la matriz A:")
    A = np.zeros((filas_A, columnas_A))
    for i in range(filas_A):
        for j in range(columnas_A):
            A[i, j] = float(input(f"Elemento A({i+1}, {j+1}): "))

    # Ingresa el tamaño de la matriz objetivo A'
    filas_A_prima = int(input("Ingrese el número de filas de la matriz objetivo A': "))
    columnas_A_prima = int(input("Ingrese el número de columnas de la matriz objetivo A': "))
    
    # Ingresa la matriz objetivo A'
    print("Ingrese los elementos de la matriz objetivo A':")
    A_prima_resultado = np.zeros((filas_A_prima, columnas_A_prima))
    for i in range(filas_A_prima):
        for j in range(columnas_A_prima):
            A_prima_resultado[i, j] = float(input(f"Elemento A'({i+1}, {j+1}): "))

    # Encuentra la matriz A' que cumple con A' * A = A_prima_resultado
    A_prima = encontrar_A_prima(A, A_prima_resultado)

    # Imprime la matriz A'
    print("La matriz A' que cumple con la operación es:")
    print(A_prima)

if __name__ == "__main__":
    main()
