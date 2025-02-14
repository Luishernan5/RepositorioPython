#PART 1
#lista modificable
lista = ["Luis Hernan","Soy el 8",True,1.75]
print(lista[0]) #Agrupar datos a traves de arreglos "Arrays"

#lista no modificable
tupla = ("Futbol","Soy el numero 11","Mido 1.76", "Soy titular") #Se usan parentesis en la tupla
print(tupla[2])

#PART 2
lista = ["Luis Hernan","Soy el 8",True,1.75]
tupla = ("Futbol","Soy el numero 11","Mido 1.76", "Soy titular") #la variable no se modifica en tupla

#esto es valido:
lista[3] = "Maquinola" #Imprime el texto "Maquinola", a exepcion de tupla no lo hace 
print(lista[3])

#ESTO NO:
#tupla[3] = "Maquinola"

#crear un conjunto (set)
conjunto = {"Futbol","Soy el numero 8","Mido 1.76", "Soy titular"} #no se pueden modificar al igual que la tupla, pueden estar desordenados
print(conjunto)

conjunto = {"Futbol","Soy el numero 8","Mido 1.76", "Soy titular","Mido 1.76"} #los datos repetidosno los muestra
print(conjunto)
#print(conjunto[3]) -> no accede al elemento

#creando un diccionario de datos
diccionario = {
    'nombre' : "Luis Hernan", 
    'numero' : "8",
    'esta feliz' : True,
    'altura' : 1.76,
    'dato duplicado' : "Luis Hernan"  
}

#en una lista se puede describir asi:
#    o : "Luis Hernan", 
#    1 : "8",
#    2 : True,
#    3 : 1.76,
#    4 : "Luis Hernan"  

print(diccionario['altura'])
print(diccionario['nombre'])
