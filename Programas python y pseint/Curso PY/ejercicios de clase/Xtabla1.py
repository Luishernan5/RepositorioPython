import os
import time
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
tablaTiempo()
        