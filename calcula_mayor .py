print("Esto es una calculadora que devuelve el numero mas grande")

primer_numero=int(input("Introduce el primer numero: "))
segundo_numero=int(input("introduce el segundo numero: "))


def devuelvemax(num1, num2):

	if primer_numero<segundo_numero:
		print(segundo_numero)
	elif primer_numero>segundo_numero:
		print(primer_numero)
	else:
		print("Los numeros son iguales.")

print("El numero mas alto es: ")

devuelvemax(primer_numero, segundo_numero)


