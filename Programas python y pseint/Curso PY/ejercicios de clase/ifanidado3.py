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
calificaciones()