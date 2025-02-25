def operaciones2():
    def suma():
        x=int(input("dame un numero: "))
        r=int(input("dame otro numero : "))
        z=x+r
        print("El resultado de la suma es: ", z)
        
    def resta():
        x=int(input("dame un numero: "))
        r=int(input("dame otro numero: "))
        z=x-r
        print("el resultado de la resta es: ", z)
            
    def multiplicacion():
        x=int(input("dame un numero: "))
        r=int(input("dame otro numero: "))
        z=x*r
        print("el resultado de la multiplicacion es: ", z)
        
    def division():
        x=int(input("dame un numero: "))
        r=int(input("dame otro numero: "))
        z=x/r
        print("el resultado de la division es: ", z)
    suma()    
    resta()
    multiplicacion()
    division()
operaciones2()

            