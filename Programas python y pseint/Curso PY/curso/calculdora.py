import tkinter as tk

def suma():
    n1=int(num1.get())
    n2=int(num2.get())
    resultado=n1+n2
    label_resultado.config(text = "Resultado: "+ str(resultado))
    
def resta():
    n1=int(num1.get())
    n2=int(num2.get())
    resultado=n1-n2
    label_resultado.config(text = "Resultado: "+ str(resultado))
    
def multiplicacion():     
    n1=int(num1.get())
    n2=int(num2.get())
    resultado=n1*n2
    label_resultado.config(text = "Resultado: "+ str(resultado))
        
def division():
    n1=int(num1.get())
    n2=int(num2.get())
    resultado=n1/n2
    label_resultado.config(text = "Resultado: "+ str(resultado))

def insertar(numeros):
    obtener = ventana.focus_get()
    if isinstance(obtener, tk.Entry):
        obtener.insert(tk.END,numeros)

def borrar():
    num1.delete(0, tk.END)
    num2.delete(0, tk.END)
    label_resultado.config(text="Resultado :")

#crear ventana
ventana = tk.Tk()
ventana.title("Calculadora Hernan")
ventana.configure(bg = "lightcyan")
    
#campos de numeros y etiquetas
num1 = tk.Entry(ventana, bg="springgreen", fg="black", width=13, justify="center")
lnum1 = tk.Label(ventana, bg="pink", fg="black", text="Valor 1", width=11,)
num2 = tk.Entry(ventana, bg="springgreen", fg="black", width=13, justify="center")
lnum2 = tk.Label(ventana, bg="pink", fg="black", text="Valor 2", width=11)
label_resultado = tk.Label(ventana,text = "Resultado : ", width=30, bg="lightsteelblue", fg="black", justify="center")

#botones
boton1 = tk.Button(ventana, bg = "yellow", fg = "black", text = "1", width = 10, height = 2, command=lambda: insertar("1"))
boton2 = tk.Button(ventana, bg = "yellow", fg = "black", text = "2", width = 10, height = 2, command=lambda: insertar("2"))
boton3 = tk.Button(ventana, bg = "yellow", fg = "black", text = "3", width = 10, height = 2, command=lambda: insertar("3"))
boton4 = tk.Button(ventana, bg = "yellow", fg = "black", text = "4", width = 10, height = 2, command=lambda: insertar("4"))
boton5 = tk.Button(ventana, bg = "yellow", fg = "black", text = "5", width = 10, height = 2, command=lambda: insertar("5"))
boton6 = tk.Button(ventana, bg = "yellow", fg = "black", text = "6", width = 10, height = 2, command=lambda: insertar("6"))
boton7 = tk.Button(ventana, bg = "yellow", fg = "black", text = "7", width = 10, height = 2, command=lambda: insertar("7"))
boton8 = tk.Button(ventana, bg = "yellow", fg = "black", text = "8", width = 10, height = 2, command=lambda: insertar("8"))
boton9 = tk.Button(ventana, bg = "yellow", fg = "black", text = "9", width = 10, height = 2, command=lambda: insertar("9"))
boton10 = tk.Button(ventana, bg = "yellow", fg = "black", text = "0", width = 10, height = 2, command=lambda: insertar("0"))

boton_borrar = tk.Button(ventana, bg = "red", fg = "black", text = "AC", width = 10, height = 2, command=borrar)

boton_division = tk.Button(ventana, bg = "cyan", fg = "black", text = "/", width = 10, height = 2, command=division)
boton_multiplicacion = tk.Button(ventana, bg = "cyan", fg = "black", text = "*", width = 10, height = 2, command=multiplicacion)
boton_suma = tk.Button(ventana, bg = "cyan", fg = "black", text = "+", width = 10, height = 2, command= suma)
boton_resta = tk.Button(ventana, bg = "cyan", fg = "black", text = "-", width = 10, height = 2, command=resta)

#agregar botones
num1.grid(row = 1, column = 0, columnspan=2, padx=3, pady= 3, ipadx=3, ipady=3)
lnum1.grid(row=0, column=0, columnspan=2, padx=3, pady=3, ipadx=3, ipady=3)
num2.grid(row = 1, column = 1, columnspan=2, padx=3, pady= 3, ipadx=3, ipady=3)
lnum2.grid(row=0, column=1, columnspan=2, padx=3, pady=3, ipadx=3, ipady=3)

label_resultado.grid(row=2, column=0, columnspan=4, padx=5, pady=5)

boton_division.grid(row = 3, column = 0, padx = 5, pady = 5)
boton_suma.grid(row = 3, column = 1, padx = 3, pady = 5)
boton_multiplicacion.grid(row = 3, column = 2, padx = 5, pady =5)

boton_resta.grid(row = 4, column = 2, padx = 5, pady = 5)
boton8.grid(row = 4, column = 0, padx = 5, pady = 5)
boton9.grid(row = 4, column = 1, padx = 5, pady = 5)

boton7.grid(row = 5, column = 0, padx = 5, pady = 5)
boton5.grid(row = 5, column = 2, padx = 5, pady = 5)
boton6.grid(row = 5, column = 1, padx = 3, pady = 5)

boton4.grid(row = 6, column = 2, padx = 5, pady = 5)
boton2.grid(row = 6, column = 0, padx = 5, pady = 5)
boton3.grid(row = 6, column = 1, padx = 5, pady = 5)

boton1.grid(row = 7, column = 0, padx = 5, pady = 5)
boton10.grid(row = 7, column = 1, padx = 5, pady = 5)
boton_borrar.grid(row = 7, column = 2, padx = 5, pady = 5)

ventana.mainloop()