#EJERCICIO 23: Generadores
##Estructuras que extraen valores de una función y se almacenan en objetos iterables, (que se pueden recorrer)
#Los valores se almacenan de uno en uno
#Son más eficientes que las funciones tradicionales
#Utiles con listas de valores infinitos
#Ejemplo:
#def genera_Numeros():
#yield numeros

#Ejemplo sin generador:
#def genera_pares(limite):
#    num=1
#    listilla=[]
#    while num<limite:
#        listilla.append(num*2)
#        num=num+1
#    return listilla
#print(genera_pares(10))

#Ejemplo 1 con generador:
#def genera_pares(limite):
#    num=1
#    while num<limite:
#        yield num*2
#        num=num+1
#devuelve_pares=genera_pares(10)
#for i in devuelve_pares:
#    print(i)

#Ejemplo 2 con generador:
#def genera_pares(limite):
#    num=1
#    while num<limite:
#        yield num*2
#        num=num+1
#devuelve_pares=genera_pares(10)
#print(next(devuelve_pares))
#print("Aquí puede ir más código...")
#print(next(devuelve_pares))
#print("Aquí puede ir más código...")
#print(next(devuelve_pares))



#EJERCICIO 24: Generador yiel from
#simplificar el código de los generadores en el caso de utilizar bucles anidados
#Ejemplo 1:
#def devuelve_ciudades(*ciudades): #puedes recibir varios parámetros (número indefinido)
#    for elemento in ciudades:
#        yield elemento#
#ciudades_devueltas=devuelve_ciudades("Guanajuato", "Guadalajara", "México", "Hidalgo", "Puebla")
#print(next(ciudades_devueltas)); print(next(ciudades_devueltas))

#Ejemplo 2: sub-elemento
#def devuelve_ciudades(*ciudades): #puedes recibir varios parámetros (número indefinido)
#    for elemento in ciudades:
#        for subelemento in elemento:
#            yield subelemento
#ciudades_devueltas=devuelve_ciudades("Guanajuato", "Guadalajara", "México", "Hidalgo", "Puebla")
#print(next(ciudades_devueltas)); print(next(ciudades_devueltas))

#Ejemplo 3: usando yiel from
#def devuelve_ciudades(*ciudades): #poniendo "#" puedes recibir varios parámetros (número indefinido)
#    for elemento in ciudades:
#        yield from elemento #para evitar poner el sub-de algo
#ciudades_devueltas=devuelve_ciudades("Guanajuato", "Guadalajara", "México", "Hidalgo", "Puebla")
#print(next(ciudades_devueltas)); print(next(ciudades_devueltas)); print(next(ciudades_devueltas)); print(next(ciudades_devueltas))



#EJERCICIO 25: Excepciones
#Son errores que ocurren durante la ejecución del programa. 
#La sintaxis del código es correcta pero durante la ejecución ha ocurrido "algo inesperado"
#Ejemplo 1: try - except
#def suma(num1, num2):
#    return num1+num2
#def resta(num1, num2):
#    return num1-num2
#def multiplica(num1, num2):
#    return num1*num2
#def divide(num1, num2):
#    try: #se agrega "try" le estas diciendo que intente la operación
#        return num1/num2
#    except ZeroDivisionError: #pero le agregas la excepción cuando el usuario divida entre cero, y pones el nombre del error que apareció
#        print("¡¡¡No dividas entre cero, por favor!!!")
#        return "Operación errónea"
#while True:
#    try: #un try siempre debe tener o un except o un finally
#        op1=(int(input("Introduce el primer número: ")))
#        op2=(int(input("Introduce el segundo número: ")))
#        break
#    except ValueError:
#        print("Los valores introducidos no son correctos. Intenta de nuevo.")
#operacion=input("Selecciona la operación a realizar (suma, resta, multiplica, divide): ")
#if operacion=="suma":
#    print(suma(op1,op2))
#elif operacion=="resta":
#    print(resta(op1, op2))
#elif operacion=="multiplica":
#    print(multiplica(op1, op2))
#elif operacion=="divide":
#    print(divide(op1, op2))
#else:
#    print("Operación no finalizada")
#el punto del ejemplo es de que si alguna vez se divide entre cero te mostrará un error,
#pero no es de sintaxis si no que es matemático.
#entonces se debe controlar las excepciones
#el error que aparece en la terminal "ZeroDivisionError: dividion by zero"

#Ejemplo 2:
#def divide():
#    try: #un try siempre debe tener o un except o un finally
#        op1=(float(input("Introduce el primer número: ")))
#        op2=(float(input("Introduce el segundo número:")))
#        print("La división es: " + str(op1/op2))
#    except ValueError:
#        print("El valor introducido es erróneo")
#    except ZeroDivisionError:
#        print("No dividas entre cero")
#    print("Cálculo finalizado")
#divide()

#Ejemplo 3:
#def divide():
#    try: #un try siempre debe tener o un except o un finally
#        op1=(float(input("Introduce el primer número: ")))
#        op2=(float(input("Introduce el segundo número:")))
#        print("La división es: " + str(op1/op2))
#    except:
#        print("Ha ocurrido un error")
#    print("Cálculo finalizado")
#divide()

#Ejemplo 4:
#def divide():
#    try: #un try siempre debe tener o un except o un finally
#        op1=(float(input("Introduce el primer número: ")))
#        op2=(float(input("Introduce el segundo número:")))
#        print("La división es: " + str(op1/op2))
#    except ValueError:
#        print("El valor introducido es erróneo")
#    except ZeroDivisionError:
#        print("No dividas entre cero")
#    finally: #se ejecuta SIEMPRE
#        print("Cálculo finalizado")
#divide()

#Ejemplo 5: para demostrar lo que hace el finally
#def divide():
#    try: #un try siempre debe tener o un except o un finally
#        op1=(float(input("Introduce el primer número: ")))
#        op2=(float(input("Introduce el segundo número:")))
#        print("La división es: " + str(op1/op2))
#    finally:
#        print("Cálculo finalizado")
#divide()



#EJERCICIO 25: Lanzamiento de excepciones
#Ejemplo 1.-
#def evaluaEdad(edad):
#    if edad<0:
#        raise TypeError("No se permiten edades negativas") #personalizas tu error
#    if edad<20:
#        return "Eres muy joven"
#    elif edad<40:
#        return "Eres joven"
#    elif edad<65:
#        "Eres adulto"
#    elif edad<100:
#        return "Eres un anciano"
#print(evaluaEdad(-15))

#Ejemplo 2.-
#import math
#def calcula_Raiz(num1):
#    if num1<0:
#        raise ValueError("El número no puede ser negativo") #personalizas el error
#    else:
#        return math.sqrt(num1)
#op1=(int(input("Introduce un número: ")))
#try:
#    print(calcula_Raiz(op1))
#except ValueError as Error_de_numero_negativo: #mandas a llamar al error
#    print(Error_de_numero_negativo) #que imprimas lo que dice el error personalizado
#print("Programa terminado")




#Programación orientada a objetos.
#Clase, objeto, (ejemplar de clase, instancia de clase, ejemplarizar una clase, instanciar una clase)
#modularización, encapsulamiento, herencia, polimorfismo

#CLASE:
#Modelo donde se redactan las características comunes de un grupo de objetos

#INSTANCIA/EJEMPLAR/OBJETO DE CLASE:
#Ejemplar perteneciente a una clase (comparten, dos objetos [instancia, ejemplar] distintos, una misma clase)

#MODULARIZACIÓN:
#Permite reutilizar trozos de código en otros objetos

#ENCAPSULACIÓN:
#Una forma de que cada clase no sepa de qué trata alguna otra clase

#MÉTODOS DE ACCESO:
#Características para conectar a las clases diferentes.

#NOMENCLATURA DEL PUNTO:
#[OBJETO].[PROPIEDAD DEL OBJETO]="propiedad"
#[OBJETO].[COMPORTAMIENTO DEL OBJETO]()

#EJERCICIO 1 POO: Clase
#class Coche(): #los nombres de las clases van con mayúscula
#    largo_chasis=250
#    ancho_chasis=120
#    ruedas=4
#    en_marcha=False #un coche detenido
#los comportamientos de una clase se declaran por métodos
#    def arrancar(self): #el "self" es el objeto/instancia/ejemplar perteneciente a la clase
#        self.en_marcha=True
#    def estado(self):
#        if(self.en_marcha):
#            return "El coche está en marcha"
#        else:
#            return "El coche está parado"
#mi_carrito=Coche() #instanciar una clase
#print("El largo del coche es: ", mi_carrito.largo_chasis, "centímetros"); print("El coche tiene ", mi_carrito.ruedas, "ruedas")
#mi_carrito.arrancar() #si le quitamos esta línea de código el estado del coche se cambia debido a la función anterior que hiciste de arrancar
#print(mi_carrito.estado())



#EJERCICIO 2: usando el ejercicio anterior (USAMOS CONSTRUCTOR)
#UN CONSTRUCTOR es un método especial que le da estado inicial a los objetos que pertenecen a una clase
#class Coche(): #los nombres de las clases van con mayúscula
#    def __init__(self): #Constructor (estado inicial)
#        self.__largo_chasis=250 #estado inicial
#        self.__ancho_chasis=120 #estado inicial
#        self.__ruedas=4 #estado inicial y lo estas encapsulando con dos "_" dentro de la clase
#        self.__en_marcha=False #estado inicial
#    def arrancar(self, arrancamos): #el "self" es el objeto/instancia/ejemplar perteneciente a la clase
#        self.__en_marcha=arrancamos
#        if(self.__en_marcha):
#            return "El coche está en marcha"
#        else:
#            return "El coche está parado"
#    def estado(self):
#        print("El coche tiene", self.__ruedas, "ruedas. Un ancho de", self.__ancho_chasis, "y un largo de", self.__largo_chasis, "centímetros")
#mi_carrito=Coche()
#print(mi_carrito.arrancar(True)) #ya le tienes que cambiar el True
#mi_carrito.estado(); print(" ")
#print("---------------------------- A continuación creamos el segundo objeto -----------------------------"); print(" ")
#mi_carrazo=Coche()
#mi_carrazo.ruedas=2 #ya no importa poner los guiones bajos aquí porque está fuera de la clase
#print(mi_carrazo.arrancar(False)) #ya le tienes que cambiar el False
#mi_carrazo.estado()