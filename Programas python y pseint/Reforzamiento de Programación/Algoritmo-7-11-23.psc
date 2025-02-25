Algoritmo sin_titulo
	Mostrar "Ingresa tu nombre, dirección, puesto"
	Leer nom, dic, pues
	Mostrar "Ingresa tu sueldo semanal, días trabajados, horas extra trabajadas"
	Leer suel, dstr, hrs
	//Pago por hora
	ope = suel/6
	div = ope/8
	suelsem = ope * dstr
	//Pago de horas extra
	Si hrs <= 8 entonces 
		mul1 = (div * 2)
		paghext = mul1 * hrs
		Mostrar "EL sueldo total a pagar por hrs extra es de: $" paghext
	Sino
		Si hrs > 8
			mul1 = (div * 3)
			ope2 = hrs - 8
			ope3 = ope2 * mul1
			ope4 = 16 * div
			paghext = ope3 + ope4
			Mostrar "Las horas dobles a pagar son $" ope4
			Mostrar "Las horas triples a pagar son $" ope3
			Mostrar "EL sueldo total a pagar por hrs extra es de: $" paghext
		FinSi
	FinSi
	total1 = suelsem + paghext
	Mostrar "El total del sueldo más las horas extra es de: $" total1
	//Pago de ley de impuesto sobre renta
	Si total1 >= 0 y total1 <= 2500 entonces
		lisr = (total1 * 0.04)
		Mostrar "El total a pagar de la ley de impuesto sobre renta es de: $", lisr
	SiNo
		Si total1 > 2501 Entonces
			lisr = (total1 * 0.07)
			Mostrar "El total a pagar de la ley de impuesto sobre renta es de: $", lisr
		FinSi
	FinSi
	//Pago Seguro
	Si total1 >= 0 y total1 <= 3000
		imss = (total1 * 0.03)
		Mostrar "El total a pagar por seguro IMSS: $", imss 
	SiNo
		Si total1 > 3001 Entonces
			imss = (total1 * 0.05)
			Mostrar "El total a pagar por seguro IMSS: $", imss 
		FinSi
	FinSi
	cuosin = (total1 * 0.02)
	Mostrar "El total a pagar de la cuota sindical es de: $", cuosin
	sumimp = lisr + imss + cuosin
	Mostrar "El total de las deducciones es de: $", sumimp 
	totalnet = (total1 - sumimp)
	Mostrar "El total neto que se pagara es de: $", totalnet
FinAlgoritmo
