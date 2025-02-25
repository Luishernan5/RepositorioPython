def tabla():
    while True:
        x=int(input("ingresa la tabla que deseas: "))
        c=1
        if x>10:
            break
        while c<=10:
            print(f"{x} * {c} = {x*c}")
            c+=1
tabla()