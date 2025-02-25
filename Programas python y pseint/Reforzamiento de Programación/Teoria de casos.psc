Algoritmo sin_titulo
	
		Imprimir "Dime un número"
		leer num1
		Imprimir "1.- Factorial x Numero"
		Imprimir "2.- Serie Fibonacci"
		Imprimir "3.- z^2=x^2+m^2"
		Imprimir "4.- x tabla de multiplicar"
		Imprimir "5.- Pirámide de figura"
		Imprimir "Selecciona una opción"
		leer opcion1
		según opcion1 Hacer
	1:
		A = 1
		AC = 1
		mientras (A <= num1 ) hacer 
			AC = AC * A
			A = A + 1
		FinMientras
		Imprimir "El resultado es: " AC
	2:
		A <- 0;
		B <- 1;
		C <- 0;
		Para Cont <-1 Hasta num1 Con Paso 1 Hacer
			Escribir C, " ";
			A <- B;
			B <- C;
			C <- A + B;
		FinPara
	3:
		Imprimir "Los resultados posibles son: "
		Para num1 desde 1 hasta num1
			Para x desde 1 Hasta num1 Hacer
				para m desde 1 Hasta num1 Hacer
					si num1^2 = x^2 + m^2 Entonces
						Imprimir num1^2 " = " x^2 " + " m^2
					finsi
				finpara
			FinPara
		FinPara
	4:
		A = 1
		Mientras (A <= 10)
			r = num1 * A
			Imprimir num1 "*" A "=" r
			A = A + 1
		FinMientras
	5:
		ne = 20
		ne2 = 1
		Para k = 1 Hasta ne + 1 Con Paso 1 Hacer
			Escribir Sin Saltar " "
		FinPara
		Escribir "*"
		Para fila = 1 Hasta num1 - 2 Con Paso 1 Hacer
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
		Para k = 1 Hasta num1 - 2 Con Paso 1 Hacer
			Escribir Sin Saltar "* "
		FinPara
		Escribir "*"
FinSegun
FinAlgoritmo

