from Mimodulo import *

##1) Crear la clase vehículo que contenga los atributos:<br>
##Color<br>
##Si es moto, auto, camioneta ó camión<br>
##Cilindrada del motor

class Vehiculo:
    def __init__(self, color, tipo, cilindrada):
        self.color = color
        self.tipo = tipo
        self.cilindrada = cilindrada

##2) A la clase Vehiculo creada en el punto 1, agregar los siguientes métodos:<br>
##Acelerar<br>
##Frenar<br>
##Doblar<br>

class Vehiculo:
    def __init__(self, color, tipo, cilindrada):
        self.color = color
        self.tipo = tipo
        self.cilindrada = cilindrada
        self.velocidad =0
        self.direccion= ""

    def acelerar(self,vel):
        self.velocidad += vel
        print(self.velocidad)

    def frenar(self,vel):
        self.velocidad -= vel
        print(self.velocidad)

    def doblar(self,dir):   
        self.direccion += dir
        print(self.direccion)

##3) Instanciar 3 objetos de la clase vehículo y ejecutar sus métodos, probar luego el resultado

v1 = Vehiculo("Rojo","Moto",150)
v2 = Vehiculo("Negro","Auto",1.5)
v3 = Vehiculo("Amarillo","Camion",1.8)

(v1.acelerar(25))
(v2.acelerar(15))
(v3.acelerar(30))

(v1.frenar(5))
(v2.frenar(10))
(v3.frenar(8))

(v1.doblar("Derecha"))
(v2.doblar("Izquierda"))
(v3.doblar("Derecha"))

##4) Agregar a la clase Vehiculo, un método que muestre su estado, es decir, a que velocidad se encuentra
#  y su dirección. Y otro método que muestre color, tipo y cilindrada

class Vehiculo:
    def __init__(self, color, tipo, cilindrada):
        self.color = color
        self.tipo = tipo
        self.cilindrada = cilindrada
        self.velocidad =0
        self.direccion= "Sin giro"

    def acelerar(self,vel):
        self.velocidad += vel
        print(self.velocidad)

    def frenar(self,vel):
        self.velocidad -= vel
        print(self.velocidad)

    def doblar(self,dir):   
        self.direccion = dir
        print(self.direccion)

    def estado(self):
        print("Se encuentra a una velocidad de ", self.velocidad, "k/h, circulando hacia la", self.direccion)

    def apariencia(self):
        print("Es un vehiculo de color", self.color,"del tipo",self.tipo,"con cilindrado",self.cilindrada,"cc")

##5) Crear una clase que permita utilizar las funciones creadas en la práctica del módulo 6<br>
##Verificar Primo<br>
##Valor modal<br>
##Conversión grados<br>
##Factorial<br>

##6) Probar las funciones incorporadas en la clase del punto 5

##7) Es necesario que la clase creada en el punto 5 contenga una lista, sobre la cual se aplquen las 
# funciones incorporadas

##8) Crear un archivo .py aparte y ubicar allí la clase generada en el punto anterior. Luego realizar 
# la importación del módulo y probar alguna de sus funciones

temperatura(58,"C","K")