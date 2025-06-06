#1. Crear una función llamada imprimir_hola_mundo que imprima por pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el programa principal.

# Definimos la funcion la cual nos devolvera un saludo
def saludo():
    print("Hola Mundo!")
# Llamamos a la funcion
saludo()    


#2. Crear una función llamada saludar_usuario(nombre) que reciba como parámetro un nombre y devuelva un saludo personalizado.

#Definimos nuestra funcion que realizara el saludo
def saludar_usuario(nombre):
    return (f"Hola, {nombre}")
# Solicitamos al usuario que ingrese su numbre
nombre_usuario = input("Ingrese su Nombre: ")
# Se llama a la funcion y se imprime el saludo con el nombre ingresado
print(saludar_usuario(nombre_usuario))


#3. Crear una función llamada informacion_personal(nombre, apellido, edad, residencia) que reciba cuatro parámetros e imprima: “Soy
#[nombre] [apellido], tengo [edad] años y vivo en [residencia]”.

# Definimos la funcion que mostrara un mensaje con datos del usuario
def informacion_personal(nombres, apellidos, edads, residencias):
    return (f"Soy {nombres} {apellidos}, tengo {edads} años y vivo en {residencias}")
# Solicitamos al usuario que ingrese sus datos
nombre = input("Ingrese su Nombre:")
apellido = input("Ingrese su Apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su lugar de Residencia: ")
# Lamamos a la funcino que muestre el mensaje con los datos del usuario
informacion_personal(nombre, apellido, edad, residencia)

#4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo. 
# calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo. 
# Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados.

# Imporamos la de la libreria de matematicas para poder usar "PI".
import math
# Definimos las funciones para poder calcular el area y el perimetro.
def calcular_area_circulo(radio):
    return math.pi * radio**2

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio
# Solicitamos al usuario que ingrese el radio del circulo y lo guardamos en una variable.
radio = float(input("Ingrese el Radio del circulo: "))
# Solicitamos que se muestren los resultado llamando a las funciones. 
print("El area del circulo es:", calcular_area_circulo(radio))
print("El Perimetro del circulo es: ", calcular_perimetro_circulo(radio))


#5. Crear una función llamada segundos_a_horas(segundos) que reciba una cantidad de segundos como parámetro y devuelva la cantidad
# de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función.

# Definimos la fncion que convertira los segundos a horas.
def segundos_a_horas(segundos):
    return segundos/3600
# Solicitamos al usuario que ingrese la cantidad de segundos.
segundos= int(input("Ingrese la cantidad de segundo"))
# Se llama a la funcion y se imprime el resultado convertido en horas.
print("Los segundos ingresados hacen un total de: ", segundos_a_horas(segundos), "horas.")


# 6. Crear una función llamada tabla_multiplicar(numero) que reciba un número como parámetro y imprima la tabla de multiplicar de ese
# número del 1 al 10. Pedir al usuario el número y llamar a la función.

# Definimos la funcion que nos devolvera la tabla de multiplicar del numero ingresado.
def tabla_multiplicar(numero):
        for i in range(1, 11):
            print(f"{numero} x {i} = {numero * i}")
# Pedimos al usuario un número
num = int(input("Ingrese un número: "))
# Llamamos a la función con el número ingresado y se genera la tabla de multiplicar
tabla_multiplicar(num)


# 7. Crear una función llamada operaciones_basicas(a, b) que reciba dos números como parámetros y devuelva una tupla con el resultado de sumarlos, 
# restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara.

# Definimos la funcion que realizar alas operaciones basicas
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else "No se puede dividir por cero"
    return (suma, resta, multiplicacion, division)
# Solicitamos al usuario que ingrese dos números.
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
# Llamamos a la función y obtenemos los resultados
resultados = operaciones_basicas(num1, num2)
# Mostramos los resultados de las operaciones que se realizoaron en la funcion
print(f"\nResultados de operaciones básicas con {num1} y {num2}:")
print(f"Suma: {resultados[0]}")
print(f"Resta: {resultados[1]}")
print(f"Multiplicación: {resultados[2]}")
print(f"División: {resultados[3]}")


# 8. Crear una función llamada calcular_imc(peso, altura) que reciba el peso en kilogramos y la altura en metros, y devuelva el índice de
# masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.

# Definimos la funcion que calculara el IMC
def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return round(imc, 2)
# Solicitamos al usuario que ingrese sus datos
peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros: "))
# Llamamos a la funcion y se muestra el IMC
imc = calcular_imc(peso, altura)
print(f"Su índice de masa corporal (IMC) es: {imc}")

# 9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba una temperatura en grados Celsius y devuelva su equivalente en Fahrenheit. 
# Pedir al usuario la temperatura en Celsius y mostrar el resultado usando la función.

#Definimos la funcion que realizara la conversion
def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return round(fahrenheit, 2)
# Pedimos la temperatura al usuario
celsius = float(input("Ingrese la temperatura en grados Celsius: "))
# Se llama a la funcion y se muestra la temperatura en Fahrenheit
fahrenheit = celsius_a_fahrenheit(celsius)
print(f"La temperatura equivalente en Fahrenheit es: {fahrenheit}°F")


# 10.Crear una función llamada calcular_promedio(a, b, c) que reciba tres números como parámetros y devuelva el promedio de ellos.
# Solicitar los números al usuario y mostrar el resultado usando esta función.

# Definimos la funcion que ralizara el calculo del promedio
def calcular_promedio(a, b, c):
    promedio = (a + b + c) / 3
    return round(promedio, 2)
# Solicitar al usuario que ingrese 3 numeros
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))
# Llamamos a la funcin que calculara y mostrar el resultado
promedio = calcular_promedio(num1, num2, num3)
print(f"El promedio de los números ingresados es: {promedio}")