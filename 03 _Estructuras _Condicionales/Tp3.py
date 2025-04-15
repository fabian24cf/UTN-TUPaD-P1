#1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
# deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.


# Solicitamos al usuario que ingrese su edad

edad= int(input("Ingresa tu edad: "))
Mayor_edad = 18

#Ingresamos la condicion para determinar si el usurio es Mayor de edad

if edad == Mayor_edad or edad > Mayor_edad: 
    print("Eres Mayor de Edad")


#2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, 
# deberá mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el mensaje “Desaprobado”


#Solicitamo al usuario que ingrese su nota
Nota = int(input("Ingrese su nota: "))
Aprobado = 6

# Ingresamos la condicion para determinar si la nota ingresada arrojara aprobado o desaprobado

if Nota <= 0 >= 10:
    if Nota >= Aprobado:
        print("Felicidades Aprobaste")
    else:
        print("Desaprobaste sigue intentandolo")
else:
    print("Ingrese una Nota Valida entre del 1 al 10")


#3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa unnúmero par, 
# imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso contrario,
# imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
# operador de módulo (%) en Python para evaluar si un número es par o impar.


#Solicitaremos al usuario que ingrese un numero par

numero=int(input("Ingrese un Numero PAR: "))

# Usamos el operador (%) para determinar si el numero ngresado por el usuario es par

if numero % 2 == 0:
    print("El numero ingresado es PAR")
else:
    print("Por favor, ingrese un número par")    


#4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las siguientes categorías pertenece:
# ● Niño/a: menor de 12 años.
# ● Adolescente: mayor o igual que 12 años y menor que 18 años.
# ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
# ● Adulto/a: mayor o igual que 30 años.

#solicitamo al usurio que ingrese su edad
edad = int(input("Ingrese su Edad: "))

#una vez ingresada la edad por el usuario asignamos un rango de edad entre los 1 y 100 años y determinamos las categorias segun los rangos de edad. 
if edad <= 1 or edad >= 100:
    print("Ingrese una edad valida")   
else:       
    if edad < 3:
        print("Usted es un/a bebe")
    elif edad >= 3 and edad < 12:
        print("Usted es un Niño/a")
    elif edad >= 12 and edad < 18:
        print("Usted es un adolecente")
    elif edad >= 18 and edad <= 30:
        print("Usted es un/a Adulto/a Joven")
    elif edad >= 30 :
        print("Usted es un/a Adulto/a")    


#5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
#(incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
#pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
#pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso
#de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal
#como una lista o un string.    

#solicitamo al usurio que ingrese su contraseña
contraseña = input("Ingrese su Contraseña: ")

# Determinamos si la contraseña ingresada esta en el rango de los 8 y 14 caracteres es valida o no
if len(contraseña) >= 8 <=14:
    print("La contraseña ingresada es correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")    


#6) Escribir un programa que tome la listanumeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si
# hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.


#Importamos de la biblioteca Statistics.
from statistics import mode, median, mean
import random
# generaremos 50 numero aleatorios comprendidios entres el 1 al 100.
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

#definimos variables y usamos las funciones importadas para usarlas en los numeros aleatorios generados anteriormente.
moda = mode(numeros_aleatorios)
media = median(numeros_aleatorios)
mediana = mean(numeros_aleatorios)

# Definimos las condiciones para determinar el tipo de sesgo deacuerdo a las variables definidas anteriormente.
if media > mediana and mediana > moda:
    sesgo = ("Sesgo Positivo")
elif media < mediana and mediana < moda:
    sesgo = ("Sesgo Negaitivo")
elif media == mediana == moda:
    sesgo = ("Sin Sesgo")
else:
    sesgo = "No se pudo determinar el sesgo"

# Deacuerdoa las condiciones aplicadas, se imprme en pantalla los nueros aleatorios que se generaron, la moda, la mediana, la media y el tipo de sesgo.

print(f"Números aleatorios: {numeros_aleatorios}")
print(f"Moda: {moda}")
print(f"Mediana: {mediana}")
print(f"Media: {media}")
print(f"Tipo de sesgo: {sesgo}")    

#7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresadotermina con vocal, 
# añadir un signo de exclamación al final e imprimir el string resultante por pantalla; en caso contrario, 
# dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla.


#Solicitamos al usuario que ingrese una frase o palabra

palabra = str(input("Ingrse una Frase o Palabra: "))

#Definimos las vocales tanto en mayuscula como en minuscula

vocales=("aeiouAEIOU")

#Definimos las condiciones para saber si la palabra ingresada termina en vocal

if palabra [-1] in vocales:
    print(f"{palabra}!")
else:
    print(palabra)

# 8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 dependiendo de la opción que desee:


#solicitamos al usuario que ingrese su nombre
nombre = str(input("Ingrese su nombre: "))

# solicitamos que ingrese una de las opciones mostradas en pantalla

opcion = int(input("Ingrese una de las siguientes opciones:" \
"1) Si quiere su nombre en mayúsculas." \
"2) Si quiere su nombre en minúsculas." \
"3) Si quiere su nombre con la primera letra mayúscula."))

# Definimos las condiciones para realizar las operacions acorde a la opcion seleccionada por el usuario.
# Se muestra en pantalla el resultado de la opcion seleccionada.

if opcion == 1:
    print(nombre.upper())
elif opcion == 2:    
    print(nombre.lower())
elif opcion == 3:    
    print(nombre.title())
else:
    print("Opcion Incorrecta")    


#9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la magnitud en una de las 
# siguientes categorías según la escala de Richter e imprima el resultadopor pantalla.   

magnitud_terremoto = float(input("Ingrese la magnitud del Terremoto: "))

if magnitud_terremoto < 3:
    print("Según la escala de Richter la Magnitud del Teremoto fue:  Muy Leve")
elif magnitud_terremoto >= 3 and magnitud_terremoto < 4:
    print("Según la escala de Richter la Magnitud del Teremoto fue:  Leve")
elif magnitud_terremoto >= 4 and magnitud_terremoto < 5:
    print("Según la escala de Richter la Magnitud del Teremoto fue:  Moderado")    
elif magnitud_terremoto >= 5 and magnitud_terremoto < 6: 
    print("Según la escala de Richter la Magnitud del Teremoto fue:  Fuerte")
elif magnitud_terremoto >= 6 and magnitud_terremoto < 7:
    print("Según la escala de Richter la Magnitud del Teremoto fue:  Muy Fuerte")   
elif magnitud_terremoto >= 7:
    print("Según la escala de Richter la Magnitud del Teremoto fue:  Extremo")   


#10) Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes del año es y qué día es. 
# El programa deberá utilizar esa información para imprimir por pantalla si el usuario se encuentra en otoño, invierno, primavera o verano.


#Definimos las variables solicitando al usuario que ingrese los datos correspondientes.

Hemisferio = str(input("Ingresa en que Hemisferio te ecuentras, Sur o Norte: "))
mes = int(input("Ingresa el mes actual, del 1 al 12: "))
dia = int(input("Ingresa el dia: "))

#Definimos las condiciones para poder determinar en que hemisferio, mes y dia nos encontramos, y asi poder teerminar la estacion.

if Hemisferio == "norte":
    if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
        estacion = "Invierno"
    elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20):
        estacion = "Primavera"
    elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20):
        estacion = "Verano"
    elif (mes == 9 and dia >= 21) or (mes in [10, 11]) or (mes == 12 and dia <= 20):
        estacion = "Otoño"
elif Hemisferio == "sur":
    if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
        estacion = "Verano"
    elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20):
        estacion = "Otoño"
    elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20):
        estacion = "Invierno"
    elif (mes == 9 and dia >= 21) or (mes in [10, 11]) or (mes == 12 and dia <= 20):
        estacion = "Primavera"
else:
    estacion = "Hemisferio no válido"

# Se imprime el resultado segun los datos ingresados por el usuario.

print(f"Según la fecha ingresada, la estación es: {estacion}")