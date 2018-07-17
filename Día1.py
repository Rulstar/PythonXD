#EJERCICIO 1
#print("Hola mundo")
#print("jojojo")
#un comentario[Agregas comentarios con "#"]



#EJERCICIO 2
#a=0
#for i in range(5):
#    a+=1
#    print(a)



#EJERCICIO 3
#a=0
#for i in range(6):
#    print(a)
#    a+=1



#EJERCICIO 4
#a=0
#for i in range(5):
#    a+=10
#    print(a)



#EJERCICIO 5: Operadores
#Opción 1.-
#a=5+6 #[suma]
#b=10%3 #modulo
#c=5**3 #exponente
#d=9/2 #división
#e=9//2 #división entera
#print(a); print(b); print(c); print(d)

#Opción 2.-
#a=5+6; b=10%3; c=5**3; d=9/2; e=9//2
#print(a); print(b); print(c); print(d); print(e)



#EJERCICIO 6: Tipos [en la consola]
#variable=5
#type(variable)
#<class `tipo de variable que es la variable`



#EJERCICIO 7:
#mensaje="""Esto es un mensaje
#con tres saltos
#de línea"""
#print(mensaje)



#EJERCICIO 8: if - else
#numero1=5; numero2=7
#if numero1>numero2:
#    print("El número 1 es mayor")
#else:
#    print("El número 2 es mayor")



#EJERCICIO 9: funciones
#[sintaxis]
#def nombre_función(parámetros):
#instrucciones de la función
#return()
#[Existen funciones predefinidas y funciones propias]
#def mensaje():
#    print("Esta lloviendo"); print("Esta nublado"); print("Es divertido")
#mensaje()
#mensaje()
#print("EEEEEEEEESTE MENSAJE ESTA FUERA DE LA FUNCIÓN")
#mensaje()



#EJERCICIO 10: función con parámetros
#def suma(num1, num2):
#    print(num1+num2)
#suma(5,7); suma(2,3); suma(5, 12.5)

#def suma(num1, num2):
#    resultado=num1+num2
#    return resultado
#print(suma(5,7)); print(suma(2,3)); print(suma(5,12.5))

#almacena_resultado=suma(5,100)
#print(almacena_resultado)



#EJERCICIO 11: Listas (arreglos/matrices)
#[sintaxis]
#nombre_lista=[elem1, elem2, elem3,...]
#imprimir todo el arreglo
#jugos=["Durazno", "Manzana", "Naranja", "Fresa"]
#print(jugos[:])

#te marca error cuando el índice que le estas poniendo no existe
#saber el elemento en la posición específica
#print(jugos[1])

#empieza a contar desde el final de mi lista con el menos
#print(jugos[-1])

#porción de mi lista [trozo de mi lista]
#print(jugos[:2])
#print(jugos[1:3]) #el "3" es exclusivo
#print(jugos[1:])

#agregar un elemento a tu arreglo al final
#jugos.append("Limonada")
#print(jugos[:])

#agregar un elemento en una posición específica en medio de mi arreglo
#jugos.insert(2,"Chocolate") #en la posición 1 poner el elemento "Chocolate"
#print(jugos[:])

#agregar varios elementos a mi arreglo al final
#jugos.extend(["José", "Paco", "Pedro"])
#print(jugos[:])

#para que te indique en qué poscición esta el elemento
#print(jugos.index("Paco"))

#me dice si el elemento que estoy poniendo esta en mi arreglo [True/False]
#print("Dario" in jugos)

#En una lista/arreglo 
#puedes combinar ya sea enteros, 
#texto, boleanos, flotantes, etc.
#Ejemplo 
#jugos=["Federico", 55.89, True, 5, False]

#para eliminar elemento de mi lista
#jugos.remove(True)
#print(jugos[:])
#para eliminar el último elemento de mi lista
#jugos.pop()
#print(jugos[:])

#para sumar arreglos diferentes
#jugos2=["José", 6, 4.5]
#jugos3=jugos+jugos2
#print(jugos3[:])

#para repetir el arreglo varias veces
#jugos=["Federico", 55.89, True, 5, False]*3
#print(jugos[:])



#EJERCICIO 12: Tuplas [es una lista que no se puede editar]
#sí permiten extraer porciones, pero es una tupla nueva
#No puedes buscar índices
#Permite comprobar si un elemento se encuentra el la tupla
#se ejecutan más rápido que las listas
#menos espacio de memoria
#[Sintaxis]
#nombre_tupla=(elem1, elem2, elem3, ...)
#tupla=("Juan", 15, 1998, 1)
#print(tupla[2])
#print(tupla[:])

#imprimir una tupla en una lista
#lista=list(tupla)
#print(lista)

#imprimir una lista en tupla
#mi_lista=["Juanito", 24, 4, 6.7, "Juanito"] #esta es una lista
#mi_tupla=tuple(mi_lista) #función para convertir la lista a tupla
#print(mi_tupla) #imprimir la tupla
#print("Juanito" in mi_tupla) # te indica si el elemento está en la tupla
#print(mi_tupla.count("Juanito")) #para saber cuántas veces está el elemento
#print(len(mi_tupla)) #saber el número de elementos
#tupla unitaria tupla=("Federico")

#empaquetado de tupla
#mi_tupla1="Diana", 15, 1, 1998
#print(mi_tupla1)

#desempaquetado de tupla
#mi_tupla1=("Diana", 15, 1, 1998)
#nombre, dia, mes, agno=mi_tupla1
#print(nombre); print(dia); print(mes); print(agno)