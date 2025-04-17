#1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
#(incluyendo ambos extremos), en orden creciente, mostrando un número por línea.


#Definimos una variable y le asignamos el valor 0
i = 0
# Usando la condicion for determinamos el trango de 100
for i in range(101):
# imprimimos el resultado del o al 100
    print(i)


#2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de dígitos que contiene.


#Definimos la variable num que almacenara el nuero ingresado por el usuario.
num = int(input("Ingrese un numero entero: "))
# Ingresamos la condicion para que el usuario ingrese un numero entero.
if num > 0:
# al ingresar un numero entero se utiliza lafuncion del contador al numero ingresado por el usuario y se muestra en pantalla.
    print("El numero ingresado contien " , len (str(num)),  "digitos")
# Si el usuario ingresa un numero que no es entero se arrojara un cartel de advertencia.
else:
    print("El numero ingresado no es entero")


#3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
#dados por el usuario, excluyendo esos dos valores.

#Definimos dos variables las cuales almacenaran los numeros ingresados por el usuario
valor1 = int(input("Ingrese el primer numero entero: "))
valor2 = int(input("Ingrese el segundo numero entero: "))

# Definimos la condicion para que si el primer valor es mayor que el segundo, el programa los invierta y pueda realizar la suma comprendida entre los numeros.
if valor1 > valor2:
    valor1, valor2 = valor2, valor1
# definimos la variable suma que excluyendo los valores ingresados realizara la suma    
suma = sum(range(valor1 + 1, valor2))
#Se muestra por consola la suma entre los numeros ingresados
print(f"La sumas comprendida entre los numeros {valor1} y {valor2} es: {suma}")    


#4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
#secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0.

#Definimos la variable num solicitandole al usuario que ingrese un numero y la variable total asignandole un valor 0.
num = int(input("Ingrese el primer numero: "))
total = 0
#Mientras el numero ingresado por el usuario sea distinto de cero el programa seguira solicitando al usuario que ingrese un nuevo nuemero.
while num != 0:
    total += num 
    num = int(input("Ingrese el siguinete numero: "))
#Cuando el usuario ingresa cero el programa reliza la suma de todos los numero ingresado que se fueron almacenando en la variable total
print("La suma de los numeros Ingresados es:", (total))


#5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
#programa debe mostrar cuántos intentos fueron necesarios para acertar el número.


#Importamos de biblioteca la funcion random.
import random

#Definimos la variable donde se almacenara el nuro al azar que saldra de la funcion random. y definimos la variable intentos que nos servira de acumulador.
numero_adivinar= random.randint(0,9)
intentos = 1

#solicitamos al usuario que ingrese un numero antes de empezar las condiciones.
numero= int(input("Adivina en que numero estoy pensando entre el 0 al 9: "))
#si el numero ingresado por el usuario es distinto al numero a adivinar se da inicio a la funcion while.
while numero != numero_adivinar:
    print("ese no era el numero, intentalo nuevamente")
#mientras el usuario no adivine se mostrara un cartel que debe volver a intentarlo y ese intento se guardara en nuestro contador ya definido anteriormente.   
    intentos += 1
    numero = int(input("Adivina nuevamente: "))
# al adivinar el numero se muestra un mensaje de felicitacion y cuantos intentos le llevo adivinar.    
print("Felicidad Adivinaste, solo te llevo", (intentos), "intentos")



#6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
#entre 0 y 100, en orden decreciente.

#Definimos una variable y le asignamos el valor 0
i = 0
# Usando la condicion for determinamos el trango de 100
for i in range(100, -1, -2):
# imprimimos el resultado del 0 al 100 mostrando solo los numeros pares
    print(i)


#7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
#número entero positivo indicado por el usuario.


#definimos las variables y le solicitamos al usuario que ingrese un numero, el cual sera el rango maximo para realizar la suma.
i = 0
num = int(input("Ingrese un numero positivo: "))

# si el numero ingresado por el usuario es mayo a cero o positivo se da inicio al ciclo.
if num > 0:
# con el nuero ingresado por el usuario definimos la variable suma y y usamos la funcion sum en el rango de 0 y el numero ingresado.    
    suma = sum(range(i, num + 1))
#se muestra en pantalla el resultado de la suma.    
    print("La suma de todos los números comprendidos entre 0 y el número entero positivo indicado es: ", (suma))    
else:
# si el usuario ingresa un numero negativo se muestra en pantalla que deb ingresar un numero positivo.    
    print("Ingrese un numero positivo")


#8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
#programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
#negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
#menor, pero debe estar preparado para procesar 100 números con un solo cambio).

# definimos las funciones de los datos solicitado y las inicializamos en cero.
pares = 0
impares = 0
negativo = 0
positivo = 0

#definimos las condiciones de los ciclos para que segun corresponda se vallan almacenando.
for num in range(100):

    num = int(input("Ingrese un Numero: "))

    if num % 2 == 0:
        pares += 1
    else:
        impares += 1 
    if num > 0:
        positivo += 1
    else:
        negativo += 1   
# mostramos el resultado de los numeros ingresados por el usuario.

print("Cantidad de numeros positivos: ", positivo)
print("Cantidad de numeros negativos: ", negativo)
print("Cantidad de numeros pares: ", pares)
print("Cantidad de numeros impares: ", impares)    


#9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
#media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
#poder procesar 100 números cambiando solo un valor).

from statistics import median
numeros = []
i=0
for i in range(100):
    num = int(input("Ingrese un numero: "))
    numeros.append(num)
media = median(numeros)
print("La media de los numeros ingresados es: ", media)


#10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
#usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.



num = int(input("Ingrese un número: "))  
if num > 0:
    num_invertido = int(str(num)[::-1])  
    print(f"El número invertido es: {num_invertido}")
else:
    num_invertido = int(str(abs(num))[::-1]) 
    print(f"El número invertido es:- {num_invertido}")