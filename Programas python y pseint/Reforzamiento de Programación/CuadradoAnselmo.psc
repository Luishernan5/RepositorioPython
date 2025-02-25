Algoritmo sin_titulo
	Definir numeroLados, contador Como Entero
	
	Escribir "Escribe un numero:"
	Leer numeroLados
	
	Para a<-1 Hasta numeroLados Con Paso 1 Hacer
		Para b<-1 Hasta numeroLados Con Paso 1 Hacer
			Si a == 1 O a == numeroLados O b == 1 O b == numeroLados Entonces
				Escribir Sin Saltar "* "
			SiNo
				Escribir Sin Saltar "  "
			FinSi
		Fin Para
		
		Escribir " "
	Fin Para
FinAlgoritmo
