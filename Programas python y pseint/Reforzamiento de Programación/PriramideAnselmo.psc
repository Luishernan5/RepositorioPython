Algoritmo sin_titulo
	Definir nf, k, j, ne, ne2, fila Como Entero
	Imprimir "Ingresa un numero "
	Leer nf
	ne = 100
	ne2 = 1
	Para k = 1 Hasta ne + 1 Con Paso 1 Hacer
		Escribir Sin Saltar " "
	FinPara
	Escribir "*"
	Para fila = 1 Hasta nf - 2 Con Paso 1 Hacer
		Escribir Sin Saltar ""
		Para k = 1 Hasta ne Con Paso 1 Hacer
			Escribir Sin Saltar" "
		FinPara
		Escribir Sin Saltar "*"
		ne = ne - 1
		Si fila >= 1 Entonces
			Para k = 1 Hasta ne2 Con Paso 1 Hacer
				Escribir Sin Saltar " "
			FinPara
			ne2 = ne2 + 2
			Escribir "*"
		FinSi
	FinPara
	Para k = 1 Hasta ne Con Paso 1 Hacer
		Escribir Sin Saltar " "
	FinPara
	Escribir Sin Saltar "* "
	Para k = 1 Hasta nf - 2 Con Paso 1 Hacer
		Escribir Sin Saltar "* "
	FinPara
	Escribir "*"
FinAlgoritmo
