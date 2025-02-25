from sympy import symbols, Eq, solve, Rational

def obtener_matrices():
    # Solicitar al usuario las dimensiones de las matrices
    filas_A = int(input("Ingrese el número de filas de la matriz A: "))
    cols_A = int(input("Ingrese el número de columnas de la matriz A: "))
    filas_B = int(input("Ingrese el número de filas de la matriz B: "))
    cols_B = int(input("Ingrese el número de columnas de la matriz B: "))
    filas_C = int(input("Ingrese el número de filas de la matriz C: "))
    cols_C = int(input("Ingrese el número de columnas de la matriz C: "))

    # Verificar que las dimensiones de las matrices sean compatibles
    if cols_A != filas_B or cols_B != cols_C or filas_A != filas_C:
        print("Las dimensiones de las matrices no son compatibles.")
        return None, None, None

    # Solicitar al usuario ingresar los elementos de las matrices
    A = []
    B = []
    C = []

    print("Ingrese los elementos de la matriz A:")
    for i in range(filas_A):
        fila = []
        for j in range(cols_A):
            elemento = Rational(input(f"Ingrese el elemento A[{i+1},{j+1}]: "))
            fila.append(elemento)
        A.append(fila)

    print("Ingrese los elementos de la matriz B:")
    for i in range(filas_B):
        fila = []
        for j in range(cols_B):
            elemento = Rational(input(f"Ingrese el elemento B[{i+1},{j+1}]: "))
            fila.append(elemento)
        B.append(fila)

    print("Ingrese los elementos de la matriz C:")
    for i in range(filas_C):
        fila = []
        for j in range(cols_C):
            elemento = Rational(input(f"Ingrese el elemento C[{i+1},{j+1}]: "))
            fila.append(elemento)
        C.append(fila)

    return A, B, C

def calcular_valores_a_b(A, B, C):
    # Definir las variables a y b
    a, b = symbols('a b')

    # Construir la ecuación a * A + b * B = C
    ecuaciones = []
    for i in range(len(A)):
        for j in range(len(A[0])):
            ecuacion = Eq(a * A[i][j] + b * B[i][j], C[i][j])
            ecuaciones.append(ecuacion)

    # Resolver el sistema de ecuaciones
    solucion = solve(ecuaciones, (a, b))

    return solucion

def imprimir_resultados(solucion):
    if solucion:
        print("Los valores de a y b que satisfacen la ecuación son:")
        for var, val in solucion.items():
            if val.is_integer:
                print(f"{var} = {val}")
            else:
                print(f"{var} = {val.evalf()} (en fracción: {val})")
    else:
        print("No se encontraron valores de a y b que satisfagan la ecuación.")

def main():
    print("Este programa calcula los valores de a y b en la ecuación a*A + b*B = C.")
    A, B, C = obtener_matrices()
    if A and B and C:
        solucion = calcular_valores_a_b(A, B, C)
        imprimir_resultados(solucion)

if __name__ == "__main__":
    main()
