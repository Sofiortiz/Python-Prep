##1) Crear una función que reciba un número como parámetro y devuelva si True si es primo y False si 
# no lo es

def primo(num):
    if((num/2) % 2 == 0):
        return False
    else:
        return True

##2) Utilizando la función del punto 1, realizar otra función que reciba de parámetro una lista de 
# números y devuelva sólo aquellos que son primos en otra lista

lista1=[]

def lista(lis):
    for i in lis:
        if(primo(i)):
            lista1.append(i)
    return(lista1)

##3) Crear una función que al recibir una lista de números, devuelva el que más se repite y cuántas 
# veces lo hace. Si hay más de un "más repetido", que devuelva cualquiera




##4) A la función del punto 3, agregar un parámetro más, que permita elegir si se requiere el menor 
# o el mayor de los mas repetidos.

##5) Crear una función que convierta entre grados Celsius, Farenheit y Kelvin<br>
##Fórmula 1	: (°C × 9/5) + 32 = °F<br>
##Fórmula 2	: °C + 273.15 = °K<br>
##Debe recibir 3 parámetros: el valor, la medida de orígen y la medida de destino

def temperatura(valor, origen, destino):
    if(origen == "C"):
        if(destino == "F"):
            grados = (valor * 9/5) + 32
            print("El valor en grados Farenheit es",grados)
        elif(destino == "K"):
            grados = valor + 273.15
            print("El valor en grados Kelvin es",grados)
        else:
            print("El valor ya esta en grados Celsius, el valor es", valor )

##6) Iterando una lista con los tres valores posibles de temperatura que recibe la función del punto 5, 
# hacer un print para cada combinación de los mismos:

##7) Armar una función que devuelva el factorial de un número. Tener en cuenta que el usuario puede 
# equivocarse y enviar de parámetro un número no entero o negativo

def factorial(n):
    if(type(n) != int):
        print("El numero debe ser entero")
    if(n<1):
        print("el numero debe ser positivo")
    if(n>1):
        n = n * (factorial(n-1))
    return n
