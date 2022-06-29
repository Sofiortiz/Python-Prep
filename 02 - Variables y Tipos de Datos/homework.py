# Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla

var1 = 15
print(var1)   

# Imprimir el tipo de dato de la constante 8.5

var2 = 8.5
print(type(var2))           

# Imprimir el tipo de dato de la variable creada en el punto 1

print(type(var1))           

# Crear una variable que contenga tu nombre

nombre = "Sofia"            

# Crear una variable que contenga un número complejo

numcomplejo = 1 + 2j        

# Mostrar el tipo de dato de la variable crada en el punto 5

print(type(numcomplejo))    

# Crear una variable que contenga el valor del número Pi redondeado a 4 decimales

numpi = 3.1416 

# Crear una variable que contenga el valor 'True' y otra que contenga el valor True. ¿Se trata de lo mismo?

var3 = "True"
var4 = True                 
#No se trata de lo mismo, var3 es un string y var4 es un booleano

# Imprimir el tipo de dato correspondientes a las variables creadas en el punto 8

print(type(var3))
print(type(var4))           

# Asignar a una variable, la suma de un número entero y otro decimal

sum = 30 + 22.5

# Realizar una operación de suma de números complejos

sumcomp = (2 + 3j) + (1 + 7j)

# Realizar una operación de suma de un número real y otro complejo

sum1 = 4 + (2 + 1j)

# Realizar una operación de multiplicación

mult = 2 * 4

# Mostrar el resultado de elevar 2 a la octava potencia

pot = 2 ** 8
print(pot)

# Obtener el cociente de la división de 27 entre 4 en una variable y luego mostrarla

div = 27 / 4
print(div)

# De la división anterior solamente mostrar la parte entera

print(int(div))

# De la división de 27 entre 4 mostrar solamente el resto

mod = 27 % 4
print(mod)

# Utilizando como operandos el número 4 y los resultados obtenidos en los puntos 16 y 17. Obtener 27 como resultado

resultado = 4 * (int(div)) + mod
print(resultado)

# Utilizar el operador "+" en una operación donde intervengan solo variables alfanuméricas

alf1 = "Hola11"
alf2 = "Hola22"
sumalf = alf1 + alf2

# Evaluar si "2" es igual a 2. ¿Por qué ocurre eso?

dos1 = "2"
dos2 = 2
print(type(dos1))
print(type(dos2))

print(dos1 == dos2)

# No es igual, ya que dos1 es un string, esta entre comillas, es una PALABRA. dos2 es un numero

# Utilizar las funciones de cambio de tipo de dato, para que la validación del punto 20 resulte verdadera

print(int(dos1) == dos2)

# ¿Por qué arroja error el siguiente cambio de tipo de datos? a = float('3,8')
a = float('3.8')
print(a)

# Arroja un error por la coma, los decimales se marcan con punto

# Crear una variable con el valor 3, y utilizar el operador '-=' para modificar su contenido

val1 = 3
val1 -= 1
print(val1)

# Realizar la operacion 1 << 2 ¿Por qué da ese resultado? ¿Qué es el sistema de numeración binario?

bina = 1 << 2
print(bina)

# Sistema de numeracion binario es un sistema que utiliza dos simbolos 1 y 0 (Es de base 2)

# Realizar la operación 2 + '2' ¿Por qué no está permitido? ¿Si los dos operandos serían del mismo tipo, siempre arrojaría el mismo resultado?

suma1 = 2 
suma2 = "2"
print(int(suma1) + int(suma2))
print(str(suma1) + str(suma2))

# No esta permitido pq no se puede sumar numeros y palabras, son diferente tipo. Arroja resultados diferentes, ya que la suma de enteros hace 2 + 2 dando como resultado 4, y la suma de string hace la suma de "2" + "2" dando como resultado 22

# Realizar una operación válida entre valores de tipo entero y string

val4 = "Este texto se repite "
val5 = 2
print(val4 * val5 + str(val5) + " veces")


