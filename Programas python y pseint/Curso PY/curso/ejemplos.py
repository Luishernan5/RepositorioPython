diccionario = {
    'luis' : "nombre",
    'ramirez' : "apellido",
    'es titular' : True,
}

print(diccionario['luis'])
print(diccionario['ramirez'])

DatosPersonales = ["luis","hernan","edad 19","altura 1.75"]
print(DatosPersonales[2])

profesion = 'estudiante'
jefe = "hola bienvenido " + profesion + " numero 190"
print(jefe)

taxi = 35
conductor = f"su total a pagar es: {taxi} pesos"
print(conductor)

RealMadrid  = "equipo y numero 1 en champions"
fifa = f"este es el mejor {RealMadrid} league"
print("equipo" in fifa)
print("luis" in fifa)
print("mejor" not in fifa)
print("apoco" not in fifa)
