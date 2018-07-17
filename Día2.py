#EJERCICIO 13: Diccionarios [clave:valor]
#mi_diccionario={"Alemania":"Berlín", "México":"DF", "Brasil":"Brasilia", "Francia":"París"}
#print(mi_diccionario["Brasil"]) #imprime la clave que fue guardada

#mi_diccionario["Italia"]="Lisboa" #agregar elemento
#print(mi_diccionario) #imprime el diccionario

#mi_diccionario["Italia"]="Roma" #corregir elemento
#print(mi_diccionario)

#del mi_diccionario["Brasil"] #eliminar clave:valor
#print(mi_diccionario)

#mi_diccionario1={"Alemania":"Berlín", 23:"Jodan", "Refrescante":5}
#print(mi_diccionario1)

#tuplar=("España", "Francia", "México", "Alemania")
#diccionario2={tuplar[0]:"Madrid", tuplar[1]:"París", tuplar[2]:"DF", tuplar[3]:"Berlín"}
#print(diccionario2)
#print(diccionario2["México"]) #imprime el valor de "México"

#tupla dentro de un diccionario / lista dentro de un diccionario
#enciclopedia={23:"Jordan", "Nombre":"Michael", "Equipo":"Chicago", "anillos":(1991, 1992, 1993, 1996, 1997, 1998)}
#print(enciclopedia)
#print(enciclopedia["anillos"])

#diccionario dentro de un diccionario
#enciclopedia1={23:"Jordan", "Nombre":"Michael", "Equipo":"Chicago", "anillos":{"temporadas":(1991, 1992, 1993, 1996, 1997, 1998)}}
#print(enciclopedia1)
#print(enciclopedia1.keys()) #imprime las claves del diccionario
#print(enciclopedia1.values()) #imprime los valores del diccionario
#print(len(enciclopedia1)) #imprime la longitud del diccionario



#ESTRUCTURAS DE CONTROL DE FLUJO
#en Python no existe el switch
#EJERCICIO 14: Condicionales IF
#print("Evaluación de los alumnos")
#calif=input("Introduce la calificación del alumno: ")
#def evaluacion(calificacion): #defines una función4
#    valoracion="Felicidades, aprobado"
#    if calificacion<5:
#        valoracion="Reprobado"
#    return valoracion
#print(evaluacion(int(calif)))



#EJERCICIO 15: Condicionales ELSE
#print("Verificación de acceso")
#edad=int(input("Introduce tu edad: "))
#if edad<18:
#    print("No puedes pasar")
#elif edad>100: #con "elif" ya no importa si hay un else a continuación, debido a que ya no le pondrá atención.
#    print("Edad incorrecta")
#else:
#    print("Puedes pasar")
#print("El programa ha finalizado")

#print("Verificación de calificación")
#calif=int(input("Introduce la calificación: "))
#if calif<5:
#    print("Reprobado")
#elif calif<6:
#    print("Panzazo")
#elif calif<7:
#    print("Bien")
#elif calif<9:
#    print("Excelente")
#else:
#    print("Genial")



#Ejercicio 16:concatenación de operadores
#edad=7 #varía el numerito
#if 0<edad<100: #el código se lee de izquierda a derecha
#    print("Edad correcta")
#else:
#    print("Edad incorrecta")



#EJERCICIO 17:
#salario_presi=int(input("Introduce el salario del presidente: "))
#print("Salario presidente: " + str(salario_presi))
#salario_direc=int(input("Introduce el salario del director: "))
#print("Salario del Director: " + str(salario_direc))
#salario_jefe_area=int(input("Introduce el salario del jefe de área: "))
#print("Salario del Jefe de área: " + str(salario_jefe_area))
#salario_admin=int(input("Introduce el salario del administrativo: "))
#print("Salario del administrativo: " + str(salario_admin))
#if salario_admin<salario_jefe_area<salario_direc<salario_presi:
#    print("Todo muy bien")
#else:
#    print("Algo no esta bien")



#EJERCICIO 18: Operadores lógicos "and" , "or"
#print("Becas 2018")
#distancia=int(input("Introduce la distancia a la escuela en km: "))
#print(distancia)
#hermanos=int(input("Introduce el # de hermanos: "))
#print(hermanos)
#salario_familia=int(input("Introduce el salario anual: "))
#print(salario_familia)
#if distancia>40 and hermanos>2 or salario_familia<=20000:
#    print("Tienes derecho a beca")
#else:
#    print("No tienes derecho a beca")



#EJERCICIO 19: Operadores lógicos "in"
#print("Optativas 2018")
#print("Asignaturas optativas: Informática - Software - Accesibilidad")
#opcion=input("Escribe la asignatura escogida: ")
#asignatura=opcion.lower()
#if asignatura in ("informática", "software", "accesibilidad"):
#    print("Asignatura elegida: " + asignatura)
#else:
#    print("La asignatura escogida no se encuentra en optativas")



#EJERCICIO 20: Bucles [for (determinado)]
#[Sintaxis]
#for [variable] in [elemento a recorrer]:
#    Cuerpo del bucle
#    Cuerpo del bucle
#Ejemplo 1.-
#for i in ["primavera", "verano", "otoño", "invierno"]:
#    print("Hola")
#    print(i)

#Ejemplo 2.-
#for estaciones_año in ["primavera", "verano", "otoño", "invierno"]:
#    print(estaciones_año)

#Ejemplo 3.-
#for i in [1,2,3]:
#    print("Hola")

#Ejemplo 4.- 
#for i in ["Sabio", "Jugar", 3]:
#    print("Hola", end="    ")

#Ejemplo 5.-
#for i in "chistosito80@hotmail.com":
#    print("Holiwi", end=" ")

#Ejemplo 6.-
#email=False
#for i in "chistosito80@hotmail.com": #quitar arroba
#    if(i=="@"):
#        email=True
#if email: #if email==True [se dice implícitamente el True]
#    print("Email correcto")
#else:
#    print("Email no es correcto")

#Ejemplo 7.-
#email=False
#mi_Email=input("Introduce dirección email: ")
#for i in mi_Email:
#    if(i=="@"):
#        email=True
#if email: #if email==True [se dice implícitamente el True]
#    print("Email correcto")
#else:
#    print("Email no es correcto")

#Ejemplo 8.-
#contador=0
#mi_Email=input("Introduce dirección email: ")
#for i in mi_Email:
#    if(i=="@" or i=="."):
#        contador=contador+1
#if contador==2:
#    print("Email correcto")
#else:
#    print("Email no es correcto")

#Ejemplo 9.- [usando range]
#for i in range(5):
#    print("Hola")
#    print(i)

#Ejemplo 10.- [usando range]
#for i in range(5):
#    print(f"Valor de la variable {i}") #función de tipo f; permite jugar con formatos de tipo diferente

#Ejemplo 11.- [usando range]
#for i in range(5, 50, 3):
#    print(f"Valor de la variable {i}")

#Ejemplo 12.-
#valido=False
#email=input("Introduce tu correo: ")
#for i in range(len(email)):
#    if email[i]=="@":
#        valido=True
#if valido:
#    print("Correo correcto")
#else:
#    print("Correo incorrecto")



#EJERCICIO 21: Bucle while
#sintaxis
#while [condición]:
#cuerpo bucle
#Ejemplo 1.-
#i=1
#while i<=10:
#    print("Ejecución " + str(i))
#    i=i+1
#print("Terminó la ejecución")

#Ejemplo 2.-
#edad=int(input("Introduce tu edad: "))
#while edad<5 or edad>100:
#    print("No puede ser válido, ya que, no estás en el rango de edad, vuelve a intentarlo")
#    edad=int(input("Introduce tu edad: "))
#print("Gracias. Puedes entrar"); print("Edad del usuario: " + str(edad))

#Ejemplo 3.-
#import math #importar la librería de matemáticas
#print("Raíz cuadrada")
#num=int(input("Introduce un número: "))
#intentos=0
#while num<0:
#    print("No se calculan raices de números negativos")
#    if intentos==2:
#        print("Has usado muchos intentos. El programa ha finalizado")
#        break;
#    num=int(input("Introduce un número: "))
#    if num<0:
#        intentos=intentos+1
#if intentos<2:
#    resultado=math.sqrt(num)
#    print("La raíz cuadrada de " + str(num) + " es " + str(resultado))



#EJERCICIO 22: Bucles "continue", "pass"
#Ejemplo 3.-
#for letra in "Python":
#    print("Vemos la letra: " + letra)

#Ejemplo 2.-
#for letra in "Python":
#    if letra=="h":
#        continue
#    print("Vemos la letra: " + letra)

#Ejemplo 3.-
#nombre="Raúl Alejandro"
#contador=0
#for i in nombre:
#    if i==" ":
#        continue
#    contador+=1
#print(contador)

#para teminar más tarde
#class Mi_clase:
#    pass #Para implementar más tarde

#Ejemplo 4.-
#email=input("Teclee su email: ")
#for i in email:
#    if i=="@":
#        arroba=True
#        break;
#else:
#    arroba=False
#print(arroba)