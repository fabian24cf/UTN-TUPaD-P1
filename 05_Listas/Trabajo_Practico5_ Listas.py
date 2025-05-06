# 1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4.

# Defnimos una lista en el rango del 1 al 100 y se impriman los multiplos de 4.
lista = list(range(4, 101, 4))
print(lista)

# 2) Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el penúltimo.


#Se crea una lista con cinco elementos numericos.
lista_penultimo = [8, 6, 7, 3, 9]
# Se solicita que se imprima el penultimo numero de la lista creada usando el "-2".
print(lista_penultimo[-2])


# 3)Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por pantalla.

# Se crea una lista vacia.
lista_vacia=[]
# se agrega un nuevo elemento a la lista vacia.
lista_vacia.append("manzana")
# Se vuelve a agregar un nuevo elemento a la lista.
lista_vacia.append("banana")
# Se agrega un nuevo elemento a la lista.
lista_vacia.append("pera")
# Se imprime la lista que ahora contiene 3 elementos.
print(lista_vacia)

# 4) Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”, respectivamente.
#  Imprimir la lista resultante por pantalla. animales = ["perro", "gato", "conejo", "pez"].

# Creamos una lista de animales segun lo solicitado.
animales = ["perro", "gato", "conejo", "pez"]
# Modificamos la segunda posicion de las lista por "loro".
animales[1] = "loro"
# Modificamos la ultima posicion de la lista con "oso".
animales[-1] = "oso" 
# Se imprime la nueva lista modificada.
print(animales)


# 5) Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza.

# En el siguiente codigo podemos ver que se define una lista llamada "numeros", la cual esta conformada por 5 numeros.
numeros = [8, 15, 3, 22, 7]
# En la siguiente linea, se removera el numero con el maximo valor de las lista.
numeros.remove(max(numeros))
# se imprime el resultado de la lista que ahora contine solo 4 numeros.
print(numeros)


#6) Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por pantalla los dos primeros.

# Definimos una lista con numeros del 10 al 30 hacuieno saltos de 5 en 5.
numeros = list(range(10,31,5))
# Se imprime los dos primeros numeros de la lista.
print(numeros[0:2])


# 7)Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores cualesquiera. 
# autos = ["sedan", "polo", "suran", "gol"]


# Se crea un lista llamada autos.
autos = ["sedan", "polo", "suran", "gol"]
# Se modifican los valores centrales de las listas por "BMW, Ferrari".
autos[1:2]= ["BMW","Ferrari"]
# Se imprime la lista con los nuevos valores modificados.
print(autos)


# 8) Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append directamente. 
# Imprimir la lista resultante por pantalla.

# Creamos una lista vacia
dobles= []
# A la lista vacia se agres el doble de 5, 10 y 15 multiplicandolo por 2
dobles.append(2 * 5)
dobles.append(2 * 10)
dobles.append(2 * 15)
# Se imprime el resultado de la lista
print(dobles)


#9) Dada la lista “compras”, cuyos elementos representan los productos comprados por diferentes clientes:
#compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]


compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]

#a) Se agregar "jugo" a la lista del tercer cliente usando append.
compras[2].append("jugo")

#b) Se reemplazar "fideos" por "tallarines" en la lista del segundo cliente.
compras[1][1]= ("tallarines")

#c) Se elimina "pan" de la lista del primer cliente.
compras[0].remove("pan")

#d) Se imprimir la lista resultante por pantalla.
print(compras)


#10) Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos:
# Posición lista_anidada[0]: 15
# Posición lista_anidada[1]: True
# Posición lista_anidada[2][0]: 25.5
# Posición lista_anidada[2][1]: 57.9
# Posición lista_anidada[2][2]: 30.6
# Posición lista_anidada[3]: False
# Imprimir la lista resultante por pantalla.

lista_anidada= [[15, True, [25.5, 57.9, 30.6], False]]
print(lista_anidada)