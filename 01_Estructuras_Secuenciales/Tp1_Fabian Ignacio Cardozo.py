# 1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.

print ("Hola Mundo");

# 2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando el nombre ingresado.

nombre = input("Ingresa tu Nombre: ");
print(f"Hola {nombre}!");

# 3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e imprima por pantalla una oración con los datos ingresados.

nombre= input("Hola, Ingresa tu Nombre: ");
apellido = input("Ahora ingresa tu Apellido: ");
edad = input("Ahora ingresa tu Edad: ");
edad = int(edad);
recidencia = input("Por ultimo ingresa el lugar de tu residencia: ");
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {recidencia}");

# 4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y su perímetro.

pi = 3.141592;
radio = float(input("Ingresa el radio del circulo: "));    
area = pi + radio ** 2;
perimetro = 2 * pi * radio;
print(f"El Area del Circulo es de: {area} y el perimetro es de: {perimetro}");

# 5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a cuántas horas equivale.

tiempo_ingresado = int(input("Ingresse la cantidad de segundos: "));
horas = tiempo_ingresado + 3600
print(f"{tiempo_ingresado} segundos equivalen a {horas} horas.");

#6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de multiplicar de dicho número.

numero = int(input("Ingrese Un numero: "));
for i in range(1, 11):
    resultado = i * numero;
    print(f"{numero} X {i} = {resultado}");


#7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.

numero1 = int(input("Ingese el Primer numero distino de 0: "));
numero2 = int(input("Ingese el Segundo numero distino de 0: "));

if numero1 == 0 or numero2 == 0:
    print("Ingrese un Numero distunto  de 0")
else: 
    suma = numero1 + numero2;
    resta = numero1 - numero2;
    multiplicacion = numero1 * numero2;
    division = numero1 / numero2;

print(f"La Suma de {numero1} + {numero2} es: {suma}");
print(f"La Resta de {numero1} - {numero2} es: {resta}");
print(f"La Multiplicacion de {numero1} * {numero2} es: {multiplicacion}");
print(f"La Division de {numero1} / {numero2} es: {division}");

# 8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice de masa corporal.

altura = float(input("Ingrese su altura: "));
peso = float(input("Ingrese su peso: "));

imc = peso / altura ** 2;

print(f"Su Indice de Masa Corporal es de: {imc}");

# 9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por pantalla su equivalente en grados Fahrenheit.

temp_celcius = float(input("Ingrese la Temperatura en Grados Celcius: "));

temp_fahrenheit = 1.8*temp_celcius + 32;

print(f"La Temperatura en Grados Fahrenheit es de: {temp_fahrenheit}°")

#10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de dichos números.

num1 = int(input("Ingresa el primer numero: "));
num2 = int(input("Ingresa el segundo numero: "));
num3 = int(input("ingresa el tercer numero: "));

promedio = (num1 + num2 + num3) / 3;

print(f"El promedio de los numeros ingresados es: {promedio}");