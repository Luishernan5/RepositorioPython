Algoritmo sin_titulo
	Imprimir " Dime cuantos trabajadores son "
	Leer a
	m = 1
	Dimensión Vector[a]
	Mientras m <= a Hacer
		Imprimir " Ingresa la edad del trabajador " m
		Leer Vector[m]
		m = m + 1
	FinMientras
	n = 1
	Mientras n <= a Hacer
		Si vector[n] >= 50 entonces
			Imprimir " La edades que reciben reconocimiento son: "
			Imprimir Vector[n]
		FinSi
	n = n + 1
	FinMientras
FinAlgoritmo
