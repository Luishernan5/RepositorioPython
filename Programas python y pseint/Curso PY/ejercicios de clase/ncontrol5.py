'primer diccionario'
periodos = {
    'otra_escuela' : 1,
    'pase_directo' : 2
}

'segundo diccionario'
carreras = {
    '1': 'Ingenieria Industrial',
    '2': "Ingenieria en Tic's ",
    '3': 'Ingenieria en Sistemas Computacionales',
    '4': 'Química',
    '5': 'Civil',
    '6': 'Mecatrónica',
    '7': 'Ingenieria Eléctrica',
    '8': 'Logística',
    '9': 'Administración'
}

'valida si es o no alumno de otra escuela'
otraescuela = input("¿Es el alumno de otra escuela?  (sí o no) si= otra escuela no=pase directo: ").lower() =="si" if periodos else "no" 
periodos = 1 if otraescuela else 2 
Numerocarrera = input("Ingresa el número de la carrera:\n" + '\n'.join(f"{num}. {carrera}" for num, carrera in carreras.items()) + "\n")
carrera = carreras.get(Numerocarrera)
if not carrera:
    print("Caracter inválido")
    quit()
    'para validar si es numero menor a 999 o no'
Numeroalumno = input("Ingresa el número de alumno:\n")
if  not Numeroalumno.isdigit() or len(Numeroalumno)>3:
    print("Numero invalido")
    quit()
Numeroalumno = Numeroalumno.zfill(3)
    
'imprimir datos'
matricula = f"2024{periodos}{Numerocarrera}{Numeroalumno}"
print("Matrícula:", matricula)
print("Carrera:", carrera)
print("Número de alumno:", Numeroalumno)
