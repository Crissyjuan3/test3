





















































Matriz = [[2,4,6],
          [1,3,5],
          [9,7,8]]

Matriz2 = [5,10,15]

Matriz3= [[10,20,30],
          [25,50,75],
          [28,92,54]]

#imprimame la diagonal secundario de la Matriz
for i in range(len(Matriz)):
    print(Matriz[i][len(Matriz)-1-i], end=" ")
print("\n")

##imprimame la diagonal Principal de la Matriz
for i in range(len(Matriz)):
    print(Matriz[i][i], end=" ")
print("\n")

#sumar la primera columna con la segunda columna
for i in range(len(Matriz)):
    print(Matriz[i][0]+Matriz[i][1], end=" ")
print("\n")

#suma la primera columna con la segunda fila
for i in range(len(Matriz)):
    print(Matriz[i][0]+Matriz[1][i], end=" ")
print("\n")

#la inversa de la diagonal secundaria de la Matriz
for i in range(len(Matriz) - 1, -1, -1):
    print(Matriz[i][i], end=" ")
print("\n")

#la inversa de la diagonal principal de la Matriz
for i in range(len(Matriz)-1,-1,-1):
    print(Matriz[i][len(Matriz)-1-i], end=" ")
print("\n")

#La columa 1 de la Matriz
for i in range(len(Matriz)):
    print(Matriz[i][1], end=" ")
print("\n")

#la columna 1 inversa de la Matriz
for i in range(len(Matriz)-1, -1, -1):
    print(Matriz[i][1], end=" ")
print("\n")

#Todos los elementos de la matriz elevados al cuadrado
for i in range(len(Matriz)):
    for j in range(len(Matriz)):
        print(Matriz[i][j]**2, end=" ")
print("\n")
#Intercambio de columnas: Dada la matriz, intercambia la primera y la última columna.
A = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
for i in range(len(A)):
    A[i][0], A[i][-1] = A[i][-1], A[i][0]
print(A)
print("\n")

#Intercambio de filas: Dada la matriz, intercambia la primera y la última fila.
Matriz4 = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]
for i in range(len(Matriz4)):
    Matriz4[0][i], Matriz4[-1][i] = Matriz4[-1][i], Matriz4[0][i]
print(Matriz4, end=" ")
print("\n")

#Ejercicio 1: Crear una matriz de 3x3 y llenarla con números del 1 al 9

matrix1 = [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]]
num = 1
for i in range(3):
    for j in range(3):
        matrix1[i][j] = num
        num += 1
for row in matrix1:
    print(row)

#Ejercicio 2: Sumar todos los elementos de la matriz creada en el ejercicio anterior.
sumaaa = 0
for i in range(3):
    for j in range(3):
        sumaaa += matrix1[i][j]
print(f"La suma de todos los elementos de la matriz es {sumaaa}")

#Ejercicio 3: Transponer la matriz creada en el ejercicio 1.
matrix_transpose = [[0, 0, 0],
                    [0, 0, 0],
                    [0, 0, 0]]
for i in range(3):
    for j in range(3):
        matrix_transpose[j][i] = matrix1[i][j]
for row in matrix_transpose:
    print(row)

#Ejercicio 4: Crea una matriz de identidad de 4x4. Una matriz de identidad es una matriz cuadrada en la que todos los elementos de la diagonal principal son unos y todos los demás elementos son ceros.
matrix_identity = [[0, 0, 0, 0],
                     [0, 0, 0, 0],
                     [0, 0, 0, 0],
                     [0, 0 ,0, 0]]
for i in range(4):
    for j in range(4):
        if i == j:
            matrix_identity[i][j] = 1
for row in matrix_identity:
    print(row)

#sumar todos los elementos de las matriz 4 x 4
Matriz5= [[1,2,3,4],
          [5,6,7,8],
          [9,10,11,12],
          [13,14,15,16]]
sumaaaa=0
for i in range(len(Matriz5)):
    for j in range(len(Matriz5)):
        sumaaaa += Matriz5[i][j]
print(f"La suma de todos los elementos de la matriz es {sumaaaa}")

for i in range(len(Matriz5)):
    print(Matriz5[i][0]+Matriz5[i][1], end=" ")
print()

#Ejercicio 1: Suma de filas Crea una matriz de 3x3 y llénala con números del 1 al 9. Luego, calcula la suma de cada fila.

Matriz6= [[1,2,3,4],
          [5,6,7,8],
          [13,14,15,16]]

for i in range(len(Matriz6)):
    print(Matriz6[0][i] + Matriz6[1][i] + Matriz6[2][i], end=" ")
print()

#Ejercicio 2: Suma de columnas Utilizando la misma matriz del Ejercicio 1, calcula la suma de cada columna.

for i in range(len(Matriz6)):
    print(Matriz6[i][0] + Matriz6[i][1] + Matriz6[i][2] + Matriz6[i][3], end=" ")
print()

#Ejercicio 3: Multiplicación de filas Crea una matriz de 2x2 y llénala con números del 1 al 4. Luego, multiplica todos los elementos de cada fila.
Matriz7 = [[1,2],
           [3,4]]

for i in range(len(Matriz7)):
    print(Matriz7[i][0] * Matriz7[i][1], end=" ")
print()

#Multiplica las columnas
for i in range(len(Matriz7)):
    print(Matriz7[0][i] * Matriz7[1][i], end=" ")
print()

#Ejercicio 5: Invertir filas Crea una matriz de 3x3 y llénala con números del 1 al 9. Luego, invierte el orden de las filas (la primera fila se convierte en la última, la segunda fila se convierte en la penúltima, etc.).

Matriz8 = [[1,2,3],
           [4,5,6],
           [7,8,9]]
for i in range(len(Matriz8)-1, -1, -1):
    print(Matriz8[i], end=" ")
print()

#Ejercicio 6: Invertir columnas Utilizando la misma matriz del Ejercicio 5, invierte el orden de las columnas (la primera columna se convierte en la última, la segunda columna se convierte en la penúltima, etc.).
# [[3,2,1],
#  [6,5,4],
#  [9,8,7]]
for i in range(len(Matriz8)):
    for j in range(len(Matriz8)-1, -1, -1):
        print(Matriz8[i][j], end=" ")
    print()

#Ejercicio 1: Crear una matriz vacia de 2x2 y llenarla con números del 1 al 4
Matriz9 = [[0,0],
           [0,0]]
num = 1
for i in range(2):
    for j in range(2):
        Matriz9[i][j] = num
        num += 1
for row in Matriz9:
    print(row)

matrizx = [[1,2,3],
          [4,5,6],
          [7,8,9]]
print(f"el total de filas es de: {len(matrizx)}")

#sacar elementos de la matriz
print(matrizx[0][1])
print(matrizx[1][1])
print("\n") #salto de linea: dame el slash inventido: \n
listaa = [1,2,3]
for elementos in list:
    print(elementos)
print()
print()
print()
# for fila in matriz:
#     for elemento in fila:
#         print(elemento, end=" ")
#
# for i in range(len(matriz)):
#     for j in matriz[i]:
#         print(j)
#
for i in range(len(matrizx)):
    print(matrizx[i][2], end=" ")
print()
print()
print()
#recorrer diagonal principal
for i in range(len(matrizx)):
    print(matrizx[i][i], end=" ")
print()
print()
print()
#toda la matriz multplicada por 2
for i in range(len(matrizx)):
    for j in range(len(matrizx)):
        print(matrizx[i][j]*2, end=" ")
print()
print()
print()

#Imprime cada columna de la matriz individualmente
for i in range(len(matrizx)): #inicializa el recorrido de la filas
    for j in range(len(matrizx)): #inicializa el recorrido de las columnas
        print(matrizx[j][i], end=' ')
print()
print()
print()

print(f"el total de filas es de: {len(matrizx)}")
print(f"el total de columnas es de: {len(matrizx[0])}")
print(f"el total de elementos es de: {len(matrizx)*len(matrizx[0])}")



"""
-------------------------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------------------------------------------------------------
"""


#utiliza lambda para ordenar la tupla por ornden de precio
tup_list = [('eggs', 5.25), ('honey', 9.70), ('carrots', 1.10), ('peaches', 2.45)]
print(sorted(tup_list, key=lambda x: x[1]))
print("\n")

#Función para sumar: Escribe una función lambda que tome dos números y devuelva su suma.
suma = lambda x, y: x + y
print(suma(2, 3))
print("\n")

#Función para duplicar: Escribe una función lambda que tome un número y devuelva el doble.
doble = lambda x: x * 2
print(doble(2))
print("\n")

#25. Utiliza list comprehension para crear una lista de los cuadrados de los números del 1 al 5.
mi_lista9 = [i**2 for i in range(1,6)]
print(f"Los cuadrados del numero 1 al 5 son:", mi_lista9)

#26. Utiliza list comprehension para crear una lista de las vocales en una cadena dada.
cadena = "hola a todos, que tal, mi nombre es Juan y esta es mi tarea de la semana 10"
mi_lista10 = [i for i in cadena if i in "aeiou"]
print(f"Las vocales de la cadena son:", mi_lista10)

#27. Utiliza list comprehension para crear una lista de las palabras de una frase.
cadena = "hola a todos, que tal, mi nombre es Juan, y soy de Ecuador y esta es mi tarea de la semana 10"
mi_lista11 = [i for i in cadena.split()]
print(f"Las palabras de la cadena son:", mi_lista11)

#28. Crea una lista de números y utiliza la función map para duplicar cada elemento de la lista.
mi_lista12 = [2,10,25,14,8,7,3,1,9,36]
mi_lista13 = list(map(lambda x: x*2, mi_lista12))
print(f"Los numeros duplicados son:", mi_lista13)

#29. Crea una lista de números y utiliza la función filter para obtener solo los números pares.
mi_lista14 = [4,20,51,28,16,14,3,2,19,72]
mi_lista15 = list(filter(lambda x: x%2==0, mi_lista14))
print(f"Los numeros pares son:", mi_lista15)

#30. Crea una lista de tuplas, donde cada tupla contiene un nombre y una edad.
mi_lista16 = [("Juan",19),("Fernando",20),("Maria",21)]
print(f"La lista de tuplas es:", mi_lista16)

#realiza una lista que tenga la funcion lambda para sacar el numero par
mi_lista4 = [1,2,3,4,5,6,7,8,9,10,20,30,40,50,66,73,80,90,100]
mi_lista10 = list(filter(lambda x: x%2==0, mi_lista4)) #que hace la x en este caso?:
print(f"Los numeros pares son:", mi_lista10)

def cuadrado(x):
    return x**2
mi_lista11 = list(map(cuadrado, mi_lista4))
print(f"Los cuadrados de la lista son:", mi_lista11)

def cuadrado2():
    milist2 = [2,3,6,8,10]
    cuadrado = [n**2 for n in milist2]
    return cuadrado
print(cuadrado2())


#cual es la estructura de una list comprehension?
#mi_lista = [i for i in (name_lista)]

#utilizar la funcion lambda en mi_lista4 y haz cuanquier calculo que quieras
mi_lista5 = list(map(lambda x: x**2, mi_lista4))
print(f"Los cuadrados de la lista son:", mi_lista5)

#ahora utiliza la funcion filter para solo mostrar los numeros en orden los numeros con mayor cantidad de 0
mi_lista6 = list(filter(lambda x: x%10==0, mi_lista5)) #que hace la x%10==0 en este caso?:
print(f"Los numeros con mayor cantidad de 0 son:", mi_lista6)


# lista1_5 = [1,2,3,4,5]
#
# lista1_5.append(6) #agrega un elemento al final de la lista
# lista1_5.insert(0,0) #agrega un elemento en la posicion que le indiques
# lista1_5.extend([7,8,9,10]) #agrega varios elementos al final de la lista
# lista1_5.remove(10) #elimina el elemento que le indiques
# lista1_5.pop() #elimina el ultimo elemento de la lista
# lista1_5.pop(0) #elimina el elemento de la posicion que le indiques
# lista1_5.clear() #elimina todos los elementos de la lista
# lista1_5.index(5) #devuelve el indice del elemento que le indiques (en este caso el 5)
# lista1_5.count(5) #devuelve cuantas veces se repite el elemento que le indiques
# lista1_5.sort() #ordena la lista de menor a mayor
# lista1_5.reverse() #ordena la lista de mayor a menor
# lista1_5.copy() #copia la lista
# lista1_5 = lista1_5 + lista1_5 #concatena dos listas
# lista1_5 = lista1_5 * 2 #multiplica los elementos de la lista por el numero que le indiques
# lista1_5 = [i for i in lista1_5] #crea una lista de los elementos de la lista
# lista1_5 = [i for i in lista1_5 if i%2==0] #crea una lista de los elementos pares de la lista
# lista1_5 = [i**2 for i in lista1_5] #crea una lista de los elementos al cuadrado de la lista
# lista1_5 = [i for i in lista1_5 if i%10==0] #crea una lista de los elementos con mayor cantidad de 0 de la lista
# lista1_5 = list(filter(lambda x: x%10==0, lista1_5)) #crea una lista de los elementos con mayor cantidad de 0 de la lista
# lista1_5 = list(map(lambda x: x**2, lista1_5)) #crea una lista de los elementos al cuadrado de la lista

# Ejercicio: Dada una lista de números enteros, escribe una función que:
# 1. Encuentre el número más grande en la lista.
# 2. Encuentre el número más pequeño en la lista.
# 3. Calcule la media de los números en la lista.

# Puedes usar la siguiente lista como ejemplo:
numeros = [4, 2, 9, 7, 5, 1, 8, 3, 6]
numeros.sort()
print(numeros[8])
print(numeros[0])
media = sum(numeros) / len(numeros)
print(f"La media es: ",media)

# Ejercicio: Dada una lista de números enteros, escribe una función que:
# 1. Encuentre todos los números pares en la lista.
# 2. Encuentre todos los números impares en la lista.
# 3. Calcule la suma de todos los números en la lista.

# Puedes usar la siguiente lista como ejemplo:
numeros2 = [4, 2, 9, 7, 5, 1, 8, 3, 6]
pares = list(filter(lambda x: x%2 == 0, numeros2))
print(pares)
impares = list(filter(lambda x: x%2 !=0, numeros2))
print(impares)
sumaa = sum(numeros2)
print(sumaa)

#esto hace lo mismo que arriba, pero menos eficiente
# Encuentra los números pares
#numeros2 = [4, 2, 9, 7, 5, 1, 8, 3, 6]
# pares = []
# for num in numeros2:
#     if num % 2 == 0:
#         pares.append(num)
# print(pares)
#
# # Encuentra los números impares
# impares = []
# for num in numeros2:
#     if num % 2 != 0:
#         impares.append(num)
# print(impares)
#
# # Calcula la suma de todos los números
# suma = 0
# for num in numeros2:
#     suma += num
# print(suma)

#Con la funcion lambda, uitilza el filer para saber los impares de la lista
list20 = [1,2,3,4,5,6,7,8,9,10]
impares = list(filter(lambda x: x%2!=0, list20))
print(impares)

# Dada la siguiente lista de números, obtenga los numeros pares:
numeros20 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = [x for x in numeros20 if x%2==0], print(pares)

# Dada la siguiente lista de palabras, ordenalas por el que tengga mas de 6 palabras y por los que empiezan con b:
palabras = ['manzana', 'banana', 'cereza', 'durazno', 'frambuesa', 'granada']

six_letter = [x for x in palabras if len(x) > 6]
print(six_letter)

b_word = list(filter(lambda x: x[0]=='b', palabras))
print(b_word)
# 1. Utiliza list comprehension para crear una nueva lista que contenga solo las palabras que tienen más de 6 letras de la lista original.
# 2. Utiliza una función lambda y la función filter() para crear una nueva lista que contenga solo las palabras que comienzan con la letra 'b' de la lista original.

# Dada la siguiente lista de números:
numeros3 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
multiplo10 = [x for x in numeros3 if x%10==0]
print(multiplo10)
multiplo20 = list(filter(lambda x: x%20==0, numeros3))
print(multiplo20)

# 1. Utiliza list comprehension para crear una nueva lista que contenga solo los números que son múltiplos de 10 de la lista original.
# 2. Utiliza una función lambda y la función filter() para crear una nueva lista que contenga solo los números que son múltiplos de 20 de la lista original.

numeros4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
cuadra = [x**2 for x in numeros4]
print(cuadra)
cubo = list(map(lambda x: x**3, numeros4))
print(cubo)

# 1. Utiliza list comprehension para crear una nueva lista que contenga el cuadrado de cada número de la lista original.
# 2. Utiliza una función lambda y la función map() para crear una nueva lista que contenga el cubo de cada número de la lista original.

palabras3 = ['gato', 'perro', 'elefante', 'jirafa', 'hipopótamo']
lettera = [x for x in palabras3 if x.count("a")]
print(lettera)
fiveletter = list(filter(lambda x: len(x) > 5, palabras3))
print(fiveletter)

# 1. Utiliza list comprehension para crear una nueva lista que contenga solo las palabras que tienen la letra 'a' de la lista original.
# 2. Utiliza una función lambda y la función filter() para crear una nueva lista que contenga solo las palabras que tienen más de 5 letras de la lista original.
from functools import reduce

numeros = [1, 2, 3, 4]
producto = reduce(lambda x, y: x * y, numeros)
print(producto)  # Imprime: 24

