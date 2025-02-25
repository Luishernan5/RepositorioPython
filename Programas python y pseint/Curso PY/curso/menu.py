def Tabla():
    x =int(input("dime que tabla de multiplicar deseas-->"))
    c=1
    while c <= 10:
        print(f"{x} * {c} = {x*c}")
        c+=1
    print("")
        
def numeros():
    n1=int(input("Dame un numero: "))
    if n1%2==0:
        print("El numero es par")
    else:
        print("El numero es impar")
    print("")

def formula():
    n = int(input("Ingrese un número: "))
    s = ''
    for i in range(1, n+1):
        s += f"{i}^{i}"
        if i != n:
            s += "+"
    r = sum(i**(i+1) for i in range(1, n+1)) / n
    print(r)
    print("")

def calificaciones():
    n1=int(input("ingresa tu calificacion --->"))
    if n1 == 100:
        print("execlente felicidades")
    elif n1 <= 99 and n1 >= 90:
        print("muy bien")
    elif n1 <= 89 and n1 >= 80:
        print("bien")
    elif n1 <= 79 and n1 >= 70:
        print("alumno regular")
    else:
        print("alumno no aprobado")
    print("")

def matricula():
    periodo = {
        '1': "Por promedio",
        '2': "De otra escuela"
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
    matricula_completa = False
    while not matricula_completa:
        while opciones not in ['1', '2']:
            print("")
            print("Elige una opción: \n1: por promedio \n2: de otra escuela")
            opciones = input("Elige una opción: ")
            if opciones in ['1', '2']:
                print("Has seleccionado:", periodo[opciones])
                print("")
            else:
                print("Número invalido")

        while True:
            print("Elige una carrera:")
            for key, value in carrera.items():
                print(key, "-", value)
            eleccion = input("De qué carrera eres: ")
            if eleccion in carrera:
                print("Has seleccionado:", carrera[eleccion])
                print("")
                break
            else:
                print("Carrera inválida")

        alumno = ""
        while not alumno.isdigit() or len(alumno) > 3:
            alumno = input("Ingresa tu número de alumno: ")
            if alumno.isdigit() and len(alumno) <= 3:
                break
            else:
                print("Número de alumno inválido.")
        alumno = alumno.rjust(3, '0')
        print(f"Tu Matrícula es: 2024{opciones}{eleccion}{alumno}")
        print("")
        print("Tu primera opcion fue: ", periodo[opciones])
        print("Tu carrera es: ", carrera[eleccion])
        print("tu numero de alumno es: ", alumno)

        matricula_completa = True
        print("")

'salir'
def salir():
    print("Saliendo.....")
    
var=True
while var:
    print("Tus opciones son: ", "\n1.- Tabla", "\n2.- Par o Impar", "\n3.- Formula", "\n4.- Calificaciones", "\n5.- Matricula", "\n6.- Salir")
    opciones=int(input("Que programa eliges: "))
    print("")
    if opciones ==1:
        Tabla()
    elif opciones ==2:
        numeros()
    elif opciones ==3:
        formula()
    elif opciones ==4:
        calificaciones()  
    elif opciones ==5:
        matricula()
    elif opciones == 6:
        salir()
        break
    else:
        print("Ingresa algo valido")