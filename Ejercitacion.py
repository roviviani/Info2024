#Ejercicio1
anio_actual = 2024
anio_nac= 1998
calculo = anio_actual - anio_nac
if calculo >= 18:
 print('Usted es mayor de edad')
else: 
 print('Usted es menor de edad')

 #Ejercicio2
def es_multiplo_de_5(numero):
    return numero % 5 == 0

numero = int(input("Ingrese un número para verificar si es múltiplo de 5: "))

if es_multiplo_de_5(numero):
    print(f"{numero} es múltiplo de 5.")
else:
    print(f"{numero} no es múltiplo de 5.")

#Ejercicio3
def numero_mayor(numero):
   return numero > 100
numero1 = int(input("Ingrese el primer numero"))
numero2 = int(input("Ingrese el segundo numero"))
if numero_mayor(numero1) and numero_mayor(numero2):
 print(f"Ambos números ({numero1} y {numero2}) son mayores a 100.")
elif numero_mayor(numero1):
    print(f"El número {numero1} es mayor a 100, pero el número {numero2} no lo es.")
elif numero_mayor(numero2):
    print(f"El número {numero2} es mayor a 100, pero el número {numero1} no lo es.")
else:
    print(f"Ambos números ({numero1} y {numero2}) no son mayores a 100.")

#Ejercicio4
def anio_bisiesto(anio):
    return (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)

anio_actual = int(input('Ingrese un año para verificar si es bisiesto: '))

if anio_bisiesto(anio_actual):
    print(f'El año {anio_actual} es bisiesto.')
else:
    print(f'El año {anio_actual} no es bisiesto.')




