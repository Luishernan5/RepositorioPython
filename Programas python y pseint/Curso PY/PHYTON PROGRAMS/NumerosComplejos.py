from fractions import Fraction

# Funciones para operaciones con números complejos
def suma_complejos(zetas):
    resultado = sum(zetas)
    print("La suma es:", resultado)

def resta_complejos(zetas):
    resultado = zetas[0]
    for z in zetas[1:]:
        resultado -= z
    print("La resta es:", resultado)

def multiplicacion_complejos(zetas):
    resultado = zetas[0]
    for z in zetas[1:]:
        resultado *= z
    print("La multiplicación es:", resultado)

def division_complejos(zetas):
    numerador = zetas[0]
    for z in zetas[1:]:
        numerador *= z.conjugate()
    denominador = zetas[1] * zetas[1].conjugate()
    
    # Convertir los valores a fracciones
    numerador_real = Fraction(numerador.real)
    numerador_imag = Fraction(numerador.imag)
    denominador_real = Fraction(denominador.real)
    denominador_imag = Fraction(denominador.imag)
    
    # Calcular la parte real e imaginaria del resultado
    parte_real = Fraction((numerador_real * denominador_real + numerador_imag * denominador_imag), (denominador_real ** 2 + denominador_imag ** 2))
    parte_imaginaria = Fraction((numerador_imag * denominador_real - numerador_real * denominador_imag), (denominador_real ** 2 + denominador_imag ** 2))
    
    print("La división es:", parte_real, "+", parte_imaginaria, "i")

# Bucle principal para solicitar operaciones al usuario
while True:
    print("\nSelecciona una operación:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("0. Salir")
    
    opcion = int(input("Ingrese el número de la operación que desea realizar: "))
    
    if opcion == 0:
        print("Saliendo...")
        break
    
    cantidad_zetas = int(input("Ingrese cuántos números complejos desea utilizar (0 para salir): "))
    if cantidad_zetas == 0:
        print("Saliendo...")
        break
        
    zetas = []
    for i in range(cantidad_zetas):
        print(f"Ingrese el número complejo Z{i + 1}:")
        while True:
            entrada_real = input(f"Ingrese la parte real del número {i + 1} (o '0' para omitir): ")
            if entrada_real == '0':
                parte_real = 0
                break
            try:
                parte_real = Fraction(entrada_real)
                break
            except ValueError:
                print("Entrada inválida. Intente de nuevo.")
        while True:
            entrada_imag = input(f"Ingrese la parte imaginaria del número {i + 1} (o '0' para omitir): ")
            if entrada_imag == '0':
                parte_imag = 0
                break
            try:
                parte_imag = Fraction(entrada_imag)
                break
            except ValueError:
                print("Entrada inválida. Intente de nuevo.")
        
        z = complex(parte_real, parte_imag)
        zetas.append(z)
    
    if opcion == 1:
        suma_complejos(zetas)
    elif opcion == 2:
        resta_complejos(zetas)
    elif opcion == 3:
        multiplicacion_complejos(zetas)
    elif opcion == 4:
        division_complejos(zetas)
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")