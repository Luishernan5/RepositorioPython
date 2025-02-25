import tkinter as Tk
def suma():
    num1=int(entry_num1.get())
    num2=int(entry_num2.get())
    resultado=num1+num2
    label_resultado.config(text = "Resultado: "+ str(resultado))
def resta():
    num1=int(entry_num1.get())
    num2=int(entry_num2.get())
    resultado=num1-num2
    label_resultado.config(text = "Resultado: "+ str(resultado))
def multiplicacion():
    num1=int(entry_num1.get())
    num2=int(entry_num2.get())
    resultado=num1*num2
    label_resultado.config(text = "Resultado: "+ str(resultado))
def division():
    num1=int(entry_num1.get())
    num2=int(entry_num2.get())
    resultado=num1/num2
    label_resultado.config(text = "Resultado: "+ str(resultado))
app=Tk.Tk()
app.title("TECNOLOGICO DE ESTUDIOS SUPERIORES DE JILOTEPEC")
    
label_num1 = Tk.Label(text= "Ingrese el primer numero: ")
entry_num1 = Tk.Entry()
    
label_num2 = Tk.Label(text = "Ingresa el segundo numero: ")
entry_num2 = Tk.Entry()
    
label_resultado = Tk.Label(text = "*****")
label_espacio = Tk.Label(text = "")
button_suma = Tk.Button(text = "Suma", command = suma)
label_espacio1 = Tk.Label(text = "")
button_resta = Tk.Button(text = "Resta", command = resta)
label_espacio2 = Tk.Label(text = "")
button_multiplicacion = Tk.Button(text = "Multiplicacion", command = multiplicacion)
label_espacio3 = Tk.Label(text = "")
button_division = Tk.Button(text = "Division", command= division)

label_num1.pack()
entry_num1.pack()
    
label_num2.pack()
entry_num2.pack()

label_resultado.pack()
label_espacio.pack()
button_suma.pack()
label_espacio1.pack()
button_resta.pack()
label_espacio2.pack()
button_multiplicacion.pack()
label_espacio3.pack()
button_division.pack()
 
app.geometry("500x600")
app.mainloop()
