def matricula():
    periodo = {
        '1': "por promedio",
        '2': "de otra escuela"
    }
    carrera = {
        '1': "Industrial",
        '2': "Civil",
        '3': "Sistemas",
        '4': "Tic's",
        '5': "Administracion",
        '6': "Quimica",
        '7': "Contabilidad",
        '8': "Mecatronica",
        '9': "Electrica"
    }

    opciones = ""
    while opciones not in ['1', '2']:
        print("Elige una opción: \n1: por promedio \n2: de otra escuela")
        opciones = input("Elige una opción: ")

    print("Has seleccionado:", periodo[opciones])

    while True:
        print("Elige una carrera:")
        for key, value in carrera.items():
            print(key, "-", value) #'key: toma el valor de 1-9' #'value: toma el valor de Industriañ-Electrica'
        eleccion = input("De qué carrera eres: ")

        if eleccion in carrera:
            print("Has seleccionado:", carrera[eleccion])
            break
        else:
            print("Carrera inválida")

    alumno = ""
    while not alumno.isdigit() or len(alumno) > 3: #isdigit: verifica si todo lo ingresado son dijitos, retorna True si son puros digitos, de lo contrario sera False y no retorna
        alumno = input("Ingresa tu número de alumno: ")
        if alumno.isdigit() and len(alumno) <= 3:#len: longitud de una secuencia para que lo maximo sea el valor 3
            break
        else:
            print("Número de alumno inválido.")

    alumno = alumno.rjust(3, '0') #rjust: rellena los carateres a la izquierda si es que hacen falta en este caso son los 0

    print(f"Matrícula: 2024{opciones}{eleccion}{alumno}")
matricula()

