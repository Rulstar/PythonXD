#Programación orientada a objetos 
#EJERCICIO 3: encapsulando funciones con dos "__" (guión bajo)
#class Coche(): #los nombres de las clases van con mayúscula
#    def __init__(self): #Constructor (estado inicial)
#        self.__largo_chasis=250 #estado inicial
#        self.__ancho_chasis=120 #estado inicial
#        self.__ruedas=4 #estado inicial y lo estas encapsulando con dos "_" dentro de la clase
#        self.__en_marcha=False #estado inicial
#    def arrancar(self, arrancamos): #el "self" es el objeto/instancia/ejemplar perteneciente a la clase
#        self.__en_marcha=arrancamos
#        if(self.__en_marcha):
#            revisado=self.__revision_interna()
#        if(self.__en_marcha and revisado):
#            return "El coche está en marcha"
#        elif(self.__en_marcha and revisado==False):
#            return "Algo salió mal durante la revisión interna. No puede arrancar el coche."
#        else:
#            return "El coche está parado"
#    def estado(self):
#        print("El coche tiene", self.__ruedas, "ruedas. Un ancho de", self.__ancho_chasis, "y un largo de", self.__largo_chasis, "centímetros")
#    def __revision_interna(self): #aquí encapsulamos esta función para que,
#        #sólamente la uses dentro de la clase y no la puedas llamar fuera de la clase
#        print("Realizando revisión interna")
#        self.gasolina="ok" #aquí puedes cambiar el "ok"
#        self.aceite="ok" #aquí puedes cambiar el "ok"
#        self.puertas="cerradas" #aquí puedes cambiar el "cerradas"
#        if(self.gasolina=="ok" and self.aceite=="ok" and self.puertas=="cerradas"):
#            return True
#        else:
#            return False
#mi_carrito=Coche()
#print(mi_carrito.arrancar(True))
#mi_carrito.estado(); print(" ")
#print("---------------------------- A continuación creamos el segundo objeto -----------------------------"); print(" ")
#mi_carrazo=Coche()
#print(mi_carrazo.arrancar(False)) 
#mi_carrazo.estado()



#HERENCIA.- (entre clases)
#Sirven para reutilizar código en caso de crear objetos similares
#Ejercicio 1:
class Transporte(): #esta es la super clase
    def __init__(self, marca, modelo):
        self.marca=marca
        self.modelo=modelo
        self.en_marcha=False
        self.acelera=False
        self.frena=False
    def arrancar(self):
        self.en_marcha=True
    def acelerar(self):
        self.acelera=True
    def frenar(self):
        self.frena=True
    def edo(self):
        print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn marcha: ", self.en_marcha, "\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena)
class Moto(Transporte): #aquí le pones la super clase para que le heredes a la moto, en este caso, si no le pones a qué superclase pertenece te marca error en la consola.
    pass
mi_moto=Moto("BMW", "D1800")
mi_moto.edo()

#Ejercicio 2:
#class Transporte(): #comportamientos universales
#    def __init__(self, marca, modelo):
#        self.marca=marca
#        self.modelo=modelo
#        self.en_marcha=False
#        self.acelera=False
#        self.frena=False
#    def arrancar(self):
#        self.en_marcha=True
#    def acelerar(self):
#        self.acelera=True
#    def frenar(self):
#        self.frena=True
#    def edo(self):
#        print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn marcha: ", self.en_marcha, "\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena)

#class Moto(Transporte): #aquí le pones la super clase para que le heredes a la moto, en este caso, si no le pones a qué superclase pertenece te marca error en la consola. Es un comportamiento propio
#    hcaballito="" #aquí declaras una variable "hcaballito"
#    def caballito(self):
#        hcaballito="Estás haciendo el caballito"



#mi_moto=Moto("BMW", "D1800")
#mi_moto.caballito()
#mi_moto.edo()