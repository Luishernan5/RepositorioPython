Algoritmo sin_titulo
	Imprimir " Dime cuantos trabajadores son son "
	Leer a
	b = 1
	Dimensión Vector[a]
	Mientras b <= a Hacer
		Imprimir " Ingresa el sueldo del trabajador " b
		Leer Vector[b]
		b = b + 1
	FinMientras
	c = 1
	totsuel = 0
	Mientras c <= a Hacer
		totsuel = totsuel + Vector[c] 
		c = c + 1
	FinMientras
	Imprimir "El total a liquidar el fin de semana por todos los trabajadores es de $" totsuel
FinAlgoritmo
