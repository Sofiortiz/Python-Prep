#1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir 
# por pantalla si es mayor o menor a cero

var1 = 0
if (var1 > 0):
    print("el numero " + str(var1)+ " es mayor que 0")

elif (var1 < 0):
    print("el numero " + str(var1)+ " es menor que 0")

else:
    print("El numero es igual a 0")

#2) Crear dos variables y un condicional que informe si son del mismo tipo de dato

var2 = 56
var3 = 87

if (type(var2) == type(var3)):
    print("son el mismo tipo de datos")

else:
    print("no son el mismo tipo de datos")

#3) Para los valores enteros del 1 al 20, imprimir por pantalla si es par o impar

n =1
while(n < 21):
    if (n % 2 == 0):
        print("el numero " + str(n) + " es par")

    else:
        print("el numero " + str(n) + " es impar")

    n += 1

#4) En un ciclo for mostrar para los valores entre 0 y 5 el resultado de elevarlo a la potencia igual a 3

for s in range(0,6):
    print(s**3)

#5) Crear una variable que contenga un número entero y realizar un ciclo for la misma cantidad de ciclos

var4 = 7
for l in range(0,var4):
    print(var4)

#6) Utilizar un ciclo while para realizar el factorial de un número guardado en una variable, 
# sólo si la variable contiene un número entero mayor a 0

c = 5
factorial = 1
if(type(c) == int):
    if(c > 0):
        while(c > 1):
            factorial = factorial * c
            c -=1 

        print("El factorial es" , factorial)

#7) Crear un ciclo for dentro de un ciclo while

a = 5
while (a < 10):
    for b in range (1,10):
        print(b)
        a += 1

#8) Crear un ciclo while dentro de un ciclo for

#9) Imprimir los números primos existentes entre 0 y 30

#10) ¿Se puede mejorar el proceso del punto 9? Utilizar las sentencias break y/ó continue para tal fin

#11) En los puntos 9 y 10, se diseño un código que encuentra números primos y además se lo optimizó. 
# ¿Es posible saber en qué medida se optimizó?

#12) Si la cantidad de números que se evalúa es mayor a treinta, esa optimización crece?

#13) Aplicando continue, armar un ciclo while que solo imprima los valores divisibles por 12, 
# dentro del rango de números de 100 a 300

#14) Utilizar la función **input()** que permite hacer ingresos por teclado, para encontrar números 
# primos y dar la opción al usario de buscar el siguiente

#15) Crear un ciclo while que encuentre dentro del rango de 100 a 300 el primer número divisible 
# por 3 y además múltiplo de 6
