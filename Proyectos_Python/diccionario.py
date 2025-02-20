diccionario = {
    'nombre' : "Luis Hernan", 
    'amigo1' : "Ek Alondra",
    'amigo2' : "Emilio",
    'altura' : 1.74,
    'edad'   : 19,
    'nombre1' : "Ortiz",
    'escuela' : "true"
    
}
print(diccionario["nombre"])
print(diccionario["altura"])
print(diccionario["edad"])
print(diccionario["amigo2"])
print(diccionario["nombre1"])
print("nombre" in diccionario)
print("numero" in diccionario)
print("mucho" not in diccionario)
print(diccionario["escuela"])

#se crean 3 diccionarios
op1 = {"nombre" : "luis", "direccion" : "soyaniquilpan", "edad" : 27, "trabajo" : "maestro"}
op2 = {"nombre" : "diego", "direccion" : "huertas", "edad" : 19, "trabajo" : "maestro"}
op3 = {"nombre" : "victor", "direccion" : "dongu", "edad" : 19, "trabajo" : "estudiante"}
print(op1["nombre"])
print(op1.get("edad"))
#puedes modificar un dato para mostrar lo que quieres
op2['nombre'] = "llavero"
print(op2)
print(op3)
#puedes anañdir otro dato al final
op3["carrera"] = "sistemas"
print(op3)
# elimina el ultimo dato "popitem"
print(list(op3.values()))
op1.popitem()
print(op1)
# elimina solo un dato "pop"
salida=op2.pop('edad')
print(op2)

t1 = {'a' : 100, 'b' : 200}
t2 = {'e' : 50, 'd' : 400}
t1.update(t2)
print(t1)
