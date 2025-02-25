import os
import time

a=0
while a <= 9:
    a = a + 1
    m = 1
    time.sleep(1)
    os.system("cls")
    while m <= 10:
        print(f"{m} * {a} - {m * a}")
        m = m + 1