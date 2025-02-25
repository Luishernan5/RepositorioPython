from fractions import Fraction

def main():
    S = {'v1', 'v2'}  # Define tus vectores aquí

    S_dict = {}
    for i, vector in enumerate(S, start=1):
        S_dict[vector] = tuple(map(float, input(f"Ingrese el vector S{i}: ").split(',')))

    input_vectors = {}
    results = []  # Para almacenar si cada vector puede o no expresarse como combinación lineal de S
    
    # Ingresar los vectores u, v, w, z en ese orden
    for vector_name in ['u', 'v', 'w', 'z']:
        try:
            input_vectors[vector_name] = tuple(map(lambda x: float(Fraction(x.strip())), input(f"Ingrese el vector {vector_name}: ").split(',')))
        except ValueError:
            print("Error: Por favor ingrese los números en el formato correcto (por ejemplo, '8' o '17/4').")
            return

    for vector, components in input_vectors.items():
        print(f"\nPara el vector {vector}:")
        for i, component in enumerate(components, start=1):
            expressions = []
            for s_vector, s_components in S_dict.items():
                expressions.append(f"{s_components[i-1]}a{i}")
            equation = " + ".join(expressions)
            print(f"{equation} = {component}")
        
        # Verificar si el vector puede expresarse como combinación lineal de los vectores en S
        can_express = is_linear_combination(S_dict.values(), components)
        results.append(can_express)

    # Verificar si todos los vectores cumplen
    all_can_express = all(results)

    # Imprimir resultados
    if all_can_express:
        print("\nTodos los vectores pueden expresarse como combinación lineal de los vectores en S.")
    else:
        print("\nAl menos uno de los vectores no puede expresarse como combinación lineal de los vectores en S.")

def is_linear_combination(S, vector):
    # Aquí puedes implementar la lógica para verificar si el vector puede expresarse como combinación lineal de los vectores en S
    return True  # Por ahora, siempre retornamos True como ejemplo

if __name__ == "__main__":
    main()
