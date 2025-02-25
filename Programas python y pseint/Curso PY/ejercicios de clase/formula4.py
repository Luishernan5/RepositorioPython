def formula():
    n = int(input("Ingrese un número: "))
    s = ''
    for i in range(1, n+1):
        s += f"{i}^{i}"
        if i != n:
            s += "+"
    r = sum(i**(i+1) for i in range(1, n+1)) / n
    print(r)
formula()

