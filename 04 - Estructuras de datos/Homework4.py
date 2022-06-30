## Estructuras de Datos

##1) Crear una lista que contenga nombres de ciudades del mundo que contenga más de 5 elementos e 
# imprimir por pantalla

list3 = ["Roma", "Paris", "Bruselas", "Madrid", "Frankfurt", "Ankara"]
print(list3)

##2) Imprimir por pantalla el segundo elemento de la lista

print(list3[1])

##3) Imprimir por pantalla del segundo al cuarto elemento

print(list3[1:4])

##4) Visualizar el tipo de dato de la lista

print(type(list3))

##5) Visualizar todos los elementos de la lista a partir del tercero de manera genérica, es decir, 
# sin explicitar la posición del último elemento

print(list3[2:])

##6) Visualizar los primeros 4 elementos de la lista

print(list3[:4])

##7) Agregar una ciudad más a la lista que ya exista y otra que no ¿Arroja algún tipo de error?

list3.append("Paris")
list3.append("Lisboa")
print(list3)

##8) Agregar otra ciudad, pero en la cuarta posición

list3.insert(3,"Moscu")
print(list3)

##9) Concatenar otra lista a la ya creada

list1 = ["Buenos Aires", "Brasilia"]
list3.extend(list1)
print(list3)

##10) Encontrar el índice de la ciudad que en el punto 7 agregamos duplicada. ¿Se nota alguna 
# particularidad?

print(list3.index("Paris"))

##11) ¿Qué pasa si se busca un elemento que no existe?

#print(list.index("Odense")) #Sale un error

##12) Eliminar un elemento de la lista

list3.remove("Buenos Aires")
print(list3)

##13) ¿Qué pasa si el elemento a eliminar no existe?

# Arroja un error

##14) Extraer el úlimo elemento de la lista, guardarlo en una variable e imprimirlo

ultimo = list3.pop()
print(ultimo)
print(list3)

##15) Mostrar la lista multiplicada por 4

print(list3 * 4)

##16) Crear una tupla que contenga los números enteros del 1 al 20

list2 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
mi_tupla = tuple(list2)


##17) Imprimir desde el índice 10 al 15 de la tupla

print(mi_tupla[9:15])

##18) Evaluar si los números 20 y 30 están dentro de la tupla

print(20 in mi_tupla)
print(30 in mi_tupla)

##19) Con la lista creada en el punto 1, validar la existencia del elemento 'París' y si no existe, 
# agregarlo. Utilizar una variable e informar lo sucedido.

elemento = "París"
if(not(elemento in list3)):
    list3.append(elemento)
    print("El elemento", elemento, "ha sido agregado")
else:
    print("El elemento", elemento,"ya existia")

##20) Mostrar la cantidad de veces que se encuentra un elemento específico dentro de la tupla y 
# de la lista

print(mi_tupla.count(3))
print(list3.count("Paris"))

##21) Convertir la tupla en una lista

mi_lista = list(mi_tupla)
print(mi_lista)

##22) Desempaquetar solo los primeros 3 elementos de la tupla en 3 variables

print("Primero:", mi_tupla[0] ,"segundo:",mi_tupla[1],"tercero:",mi_tupla[2])

##23) Crear un diccionario utilizando la lista crada en el punto 1, asignandole la clave "ciudad".
#  Agregar tambien otras claves, como puede ser "Pais" y "Continente".

dic = {"ciudad":list3 , "Pais": ["Argentina", "Francia", "Italia"], "Continente":["America","Europa"]}
print(dic)

##24) Imprimir las claves del diccionario

print(dic.keys())

##25) Imprimir las ciudades a través de su clave

print(dic["ciudad"])