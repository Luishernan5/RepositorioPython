Algoritmo sin_titulo
	Imprimir "Dime la cantidad de columnas y filas para las 3 matrices"
	Leer colfi
	Limpiar Pantalla
	//Llenar matriz A
	Imprimir "Matriz A"
	n = 1
	Dimension matriz[colfi,colfi]
	Mientras n <= colfi Hacer
		m = 1
		Mientras m <= colfi
			Imprimir "Ingresa el valor de la casilla..." n "," m
			Leer matriz[n , m]
			m = m + 1
		FinMientras
		n = n + 1
	FinMientras
	//Llenar matriz B
	Imprimir "Llenar matriz B"
	colfi2 = colfi
	Dimension matriz2[colfi2,colfi2]
	n= 1
	Mientras n <= colfi2 Hacer
		m = 1
		Mientras m <= colfi2 Hacer
			Imprimir "Ingresa el valor de la casilla..." n "," m
			Leer matriz2[n,m]
			m = m + 1
		FinMientras
		n = n + 1
	FinMientras
	//Imprimir matriz A
	Imprimir "Matriz A"
	s = 1
	Mientras s <= colfi
		r = 1
		Mientras r <= colfi
			Imprimir sin saltar matriz[s , r],""
			r = r + 1
		FinMientras
		s = s + 1
		Imprimir con salto 
	FinMientras
	//Imprimir matriz B
	Imprimir "Matriz B"
	s = 1
	Mientras s <= colfi2
		r = 1
		Mientras r <= colfi2
			Imprimir sin saltar matriz2[s r],""
			r = r + 1
		FinMientras
		s = s + 1
		Imprimir con salto 
	FinMientras
	//Imprimir matriz C
	colfi3 = colfi
	Imprimir "Matriz C"
	s = 1
	Mientras s <= colfi3
		r = 1
		Mientras r <= colfi3
			multi= matriz[s,r] * matriz2[s,r]
			Imprimir sin saltar multi,""
			r = r + 1
		FinMientras
		s = s + 1
		Imprimir con salto 
	FinMientras
FinAlgoritmo
