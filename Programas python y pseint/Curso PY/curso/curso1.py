'importaciones'
import os
import time

'programa 1'
def entrada():
    while True: 
        edad = int(input("ingresa tu edad: "))
        break
    if edad >=18:
        print("puedes pasar")
    else: 
        print("no puedes pasar")
        
'programa 2'
def salario():
    while True:
        salario=int(input("ingresa tu salario: "))
        break
    if salario<=1000:
        print("Faltaste mucho al trabajo")
    elif salario>=1001 and salario<=1500:
        print("trabajaste por lo menos 3 dias")
    elif salario>1500 and salario<=2000:
        print("trabaste por lo menos 4 dias")
    elif salario>=2001 and salario<=2500:
        print("trabaste horas extra")    

'Programa 3'
def tabla():
    while True:
        num=int(input("que tabla necesitas: "))
        cont=1
        if num>10:
            break
        while cont<=10:
            print(f"{num} * {cont} = {num*cont}")
            cont+=1
        break
    
'Programa 4'
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
        
'Programa 5'
def trabajador():
    turno = {
        '1': "Tarde",
        '2': "Mañana"
    }
    empresa = {
        '1': "Trupper",
        '2': "Liverpool",
        '3': "Super Donico",
        '4': "Bodega Aurrera"
    }
    opciones = ""
    completo = False
    while not completo:
        while opciones not in ['1', '2']:
            print("Elige una opción: \n1: Tarde \n2: Mañana")
            opciones = input("Ingresa una opción: ")
            if opciones in ['1', '2']:
                print("Has seleccionado", turno[opciones])
            else:
                print("Número invalido")

        while True:
            print("Elige tu empresa: ")
            for key, value in empresa.items():
                print(key, "-", value)
            eleccion = input("De qué empresa eres: ")
            if eleccion in empresa:
                print("Has seleccionado:", empresa[eleccion])
                break
            else:
                print("Empresa inválida")

        control = ""
        while not control.isdigit() or len(control) > 5:
            control = input("Ingresa tu número de trabajador: ")
            if control.isdigit() and len(control) <= 5:
                break
            else:
                print("Número de trabajador inválido.")
        control = control.rjust(5, '0')
        print(f"Numero de Control: 12024{opciones}{eleccion}{control}")

        completo = True
        
'programa 6'
def notas():
    n=int(input("ingresa tu nota de 1 a 100: "))
    if n<=20 and n>=1:
        print("Tu nota fue desaprobatoria, tienes una segunda oportunidad")
        n3=int(input("Dame tu nota de la segunda vuelta: "))
        if n3>=70 and n3<=100:
            print("Estas aprobado")
        else:
            print("No aprobaste")
    elif n>=21 and n<=50:
        print("Tienes otra oportunida")
        n2=int(input("Dame tu nota de la segunda oportunidad: "))
        if n2>=70 and n2<=100:
            print("Aprobaste")
        else:
            print("Estas reprobado")
    elif n>=51 and n<=75:
        print("Te falta estudiar mas")
        n4=(input("Quieres una segunda oportunidad? "))
        if n4=="si":
            n5=int(input("Que nota obtuviste en tu segunda oportunidad? "))
            if n5>=75 and n5<=100:
                print("Felicidades estas aprobado")
        elif n4=="no":
            print("Tu nota sera desaprobatoria")
    elif n>=76 and n<=90:
        print("Estas aprobado")
        if n<80:
            print("Si estudias mas puedes mejorar")
        elif n>80:
            print("Lo hiciste bien")
    elif n>=91 and n<=100:
        print("Tu nota fue exelente")
        if n>95:
            print("Eres inreible")
            
'Programa 7'
def superheroes():
    superhero={
        '1':"Batman",
        '2':"Superman",
        '3':"Spiderman",
        '4':"Iron-Man",
        '5':"Flash"
    }
    
    power={
        '1':"Superfueza",
        '2':"Super velocidad",
        '3':"Agilidad",
        '4':"Resistente",
        '5':"Inteligente"
    }
    while True:
        print("")
        print("Los superheroes son: ")
        for key, value in superhero.items():
            print(key, "-", value)
        escoger=input("Que superheroe escoges: ")
        if escoger in superhero:
            print("Has seleccionado: ", superhero[escoger])
            print("")
            selected_powers = []
            print("Los poderes disponibles son:")
            for key, value in power.items():
                print(f"{key}. {value}")
            while True:
                escoger_poder = input("¿Qué poder quieres (ingresa el número, separado por comas si quieres más de uno)?: ")
                poderes_seleccionados = escoger_poder.split(',')
                for poder in poderes_seleccionados:
                    if poder.strip() in power:
                        selected_powers.append(power[poder.strip()])
                    else:
                        print(f"El poder {poder.strip()} no es válido.")
                else:
                    break
            print("")
            print("Poderes seleccionados:")
            for poder in selected_powers:
                print("- ", poder)
            if escoger_poder=="1" or escoger_poder=="2":
                print("Es un buen heroe")
            elif escoger_poder=="3" or escoger_poder=="4":
                print("Es un heroe fantastico")
            elif escoger_poder=="5":
                print("Es un heroe brillante")
            break
        else:
            print("Opción inválida. Por favor, selecciona un número válido.")

'Programa 8'
def sumatoria():
    acu = 0
    while True: #al menos unavez se ejecutara
        n1 =(input("teclea un numero: o presiona x para salir "))
        if(n1=="x"):
            break #rompe el ciclo
        
        else:
            acu=acu+int(n1) #toma n1 como entero
            #esta fuera del ciclo lo siguiente
            if(acu>0):
                print("El resultado final del acumulador es ---> ", acu)
            else:
                print("se pulso x para salir del bucle")

'Programa 9'
def tablaTiempo():
    n = 1
    while n <=10:
        m = 1
        time.sleep(0.5)
        os.system("cls")
        print(f"la tabla del {n} es:")
        while m <=10:
            r = n*m
            print(f"{n} x {m} = {r}")
            m +=1
        n +=1
        print()
        
'Programa 10'
def numeros():
    n1=int(input("Dame un numero: "))
    if n1%2==0:
        print("El numero es par")
    else:
        print("El numero es impar")

'Programa 11'
def operaciones():
    a = int(input("ingresa el primer numero: "))
    b = int(input("ingresa el segundo numero: "))
    print("{+} suma a+b")
    print("{-} resta a-b")
    print("{*} multiplica a*b")
    print("{/} divide a/b")
    simbolo = input("ingresa la operacion insertando el simbolo: ")
    match simbolo:
        case "+":
            print("el resultado", (a+b))
        case "-":
            print("el resultadon", (a-b))
        case "*":
            print("el resultado", (a*b))
        case "/":
            if b !=0:
                print("el resultado", (a/b))
            else:
                print("no se puede dividir entre cero")
        case _:
            print("operacion no valida")
            
'Programa 12'
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

'Programa 13'
def formula():
    n = int(input("Ingrese un número: "))
    s = ''
    for i in range(1, n+1):
        s += f"{i}^{i}"
        if i != n:
            s += "+"
    r = sum(i**(i+1) for i in range(1, n+1)) / n
    print("El resultado de la formula es: ", r)

'salir'
def salir():
    print("Saliendo.....")
                         
'menu'
var=True
while var:
    print("Tus opciones son: ", "\n1.- Entrada", "\n2.- Salario", "\n3.- Tabla", "\n4.- Matricula", "\n5.- Trabajador", "\n6.- Notas", "\n7.- Superheroes", "\n8.- Sumatoria", "\n9.- Tabla Determinada", "\n10.- Numeros", "\n11.- Operaciones", "\n12.- Calificaciones", "\n13.- Formula", "\n14.- Salir")
    opciones=int(input("Que programa eliges: "))
    print("")
    if opciones ==1:
        entrada()
    elif opciones ==2:
        salario()
    elif opciones ==3:
        tabla()
    elif opciones ==4:
        matricula()  
    elif opciones ==5:
        trabajador()
    elif opciones ==6:
        notas()
    elif opciones ==7:
        superheroes()
    elif opciones ==8:
        sumatoria()
    elif opciones ==9:
        tablaTiempo()
    elif opciones ==10:
        numeros()
    elif opciones ==11:
        operaciones()
    elif opciones ==12:
        calificaciones()
    elif opciones ==13:
        formula()
    elif opciones ==14:
        salir()
        break
    print("")
print("no esta en el rango")
