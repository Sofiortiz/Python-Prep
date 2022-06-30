
##1) A partir de una lista vacía, utilizar un ciclo while para cargar allí números negativos del -15 
# al -1

lista = []
i = -15

while(i<0):
    lista.append(i)
    i +=1

print(lista)

##2) ¿Con un ciclo while sería posible recorrer la lista para imprimir sólo los números pares?

i = 0
while(i < len(lista)):
    if(lista[i]%2 == 0):
        print(lista[i])
        i +=1
    else:
        i +=1

##3) Resolver el punto anterior sin utilizar un ciclo while

for elemento in lista:
    if(elemento % 2 == 0):
        print(elemento)
    else:
        pass

##4) Utilizar el iterable para recorrer sólo los primeros 3 elementos

for i in lista[:3]:
    print(i)

##5) Utilizar la función **enumerate** para obtener dentro del iterable, tambien el índice al que 
# corresponde el elemento

for i,c in enumerate(lista[:3]):
    print(i,c)

##6) Dada la siguiente lista de números enteros entre 1 y 20, crear un ciclo donde se completen los 
# valores faltantes: 

lista2 = [1,2,5,7,8,10,13,14,15,17,20]
n = 1 
while (n < 21):
    if(n == lista2[n-1]):
        print(n)
        n += 1
    else:
        lista2.insert((n-1),n)
        print(n)
        n += 1

##7) La sucesión de Fibonacci es un listado de números que sigue la fórmula: <br>
##n<sub>0</sub> = 0<br>
##n<sub>1</sub> = 1<br>
##n<sub>i</sub> = n<sub>i-1</sub> + n<sub>i-2</sub><br>
##Crear una lista con los primeros treinta números de la sucesión.<br>

# f =[0,1,1,2,3,5,8,13,21,34,55,89]
f = [0,1]
n=2
while(n<30):
    f.append(f[n-2]+f[n-1])
    n += 1
print(f)

##8) Realizar la suma de todos elementos de la lista del punto anterior

suma = 0
for i in f:
    suma = suma + i
print(suma)

##print(sum(f))
    
##9) La proporción aurea se expresa con una proporción matemática que nace el número irracional 
# Phi= 1,618… que los griegos llamaron número áureo. El cuál se puede aproximar con la sucesión de 
# Fibonacci. Con la lista del ejercicio anterior, imprimir el cociente de los últimos 5 pares de dos 
# números contiguos:<br>
##Donde i es la cantidad total de elementos<br>
##n<sub>i-1</sub> / n<sub>i</sub><br>
##############n<sub>i-2</sub> / n<sub>i-1</sub><br>
##n<sub>i-3</sub> / n<sub>i-2</sub><br>
##n<sub>i-4</sub> / n<sub>i-3</sub><br>
##n<sub>i-5</sub> / n<sub>i-4</sub><br>

n=29
while (n > 24):
    print( f[n-1] / f[n])
    n-=1

##10) A partir de la variable cadena ya dada, mostrar en qué posiciones aparece la letra "n"<br>

cadena = 'Hola Mundo. Esto es una practica del lenguaje de programación Python'
for i,c in enumerate(cadena):
    if(c == "n"):
        print(i)

##11) Crear un diccionario e imprimir sus claves utilizando un iterador

dic = {"verduras":["Papa", "Zanahoria"], "frutas": ["Naranja", "frutilla"]}

for i in dic:
    print(i)

##12) Convertir en una lista la variable "cadena" del punto 10 y luego recorrerla con un iterador 

lista_cadena = list(cadena)

for i in lista_cadena:
    print(i)

##13) Crear dos listas y unirlas en una tupla utilizando la función zip

l1 = ["Juan", "Veronica"]
l2 = [30,15]

c = zip(l1,l2)
print(list(c))

##14) A partir de la siguiente lista de números, crear una nueva sólo si el número es divisible 
# por 7<br>

lis = [18,21,29,32,35,42,56,60,63,71,84,90,91,100]
lis7 = []
for i in lis:
    if(i % 7 == 0):
        lis7.append(i)
print(lis7)

##15) A partir de la lista de a continuación, contar la cantidad total de elementos que contiene, 
# teniendo en cuenta que un elemento de la lista podría ser otra lista:<br>
lis = [[1,2,3,4],'rojo','verde',[True,False,False],['uno','dos','tres']]

contador=0
aux=[]
for i in lis:
    if(type(i) == list):
        aux=list(i)
        contador = contador + len(aux)
    else:
        contador += 1
print(contador)

##16) Tomar la lista del punto anterior y convertir cada elemento en una lista si no lo es

for i in lis:
    if(type(i) != list):
        print(list(i))
