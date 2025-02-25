Algoritmo sin_titulo
	//Llenar matriz
	Imprimir "Dime la cantidad de columnas de la matriz"
	Leer c
	Imprimir "Dime la cantidad de renglones de la matriz"
	Leer r
	e = 1
	Dimension matriz[r,c]
	Mientras e <= r Hacer
		m = 1
		Mientras m <= c
			Imprimir "Ingresa el valor de la casilla..." e "," m
			Leer matriz[e,m]
			m = m + 1
		FinMientras
		e = e + 1
	FinMientras
	//Imprimir matriz
	s = 1
	Mientras s <= r
		n = 1
		Mientras n <= c
			Imprimir sin saltar matriz[s,n],""
			n = n + 1
		FinMientras
		s = s + 1
		Imprimir con salto 
	FinMientras
    FinAlgoritmo
