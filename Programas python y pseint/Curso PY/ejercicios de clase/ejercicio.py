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
sumatoria()