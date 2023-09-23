
"""

#Pyhton trabaje con sangria en lugar de llaves

---------------------------
#imprimir una cadena

-> print("Hello, World!") 
-> exit()

---------------------------
#imprimir una cadena con "," | concatenacion

x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

#rpta:  Python is awesome

---------------------------
#imprimir una cadena con "+" | concatenacion

x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

#rpta:  Python is awesome

NOTA: Para utilizar el "+" ambos deben ser del mismo tipo

---------------------------
#VARIABLES

-> x = 5                   | este es un tipo int
-> y = "John" O 'John'     | este es un tipo string

-> print(x)
-> print(y)

---------------------------

#ESPECIFICACION DE VARIABLES
    
-> x = str(3)    # x STRING
-> y = int(3)    # y ENTERO
-> z = float(3)  # z FLOAT

---------------------------

#OBTENER EL TIPO DE DATO DE UNA VARIABLE

-> print(type(y))

#rpta: <class 'int'>

---------------------------

#MULTIPLES VALORES EN UNA LINEA

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

#rpta:

Orange
Banana
Cherry

---------------------------

#UN VALOR PARA MULTIPLES VARIABLES

x = y = z = "Orange"
print(x)
print(y)
print(z)

#rpta:

Orange
Orange
Orange

---------------------------

#DESEMPAQUETAR UN ARRAY

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

#rpta:

apple
banana
cherry

---------------------------
#VARIABLE GLOBAL

x = "awesome" #declaramos una variable global

def myfunc(): #esto es una funcion
  print("Python is " + x)

myfunc()

#rpta: 

Python is awesome

---------------------------
# VARIABLE LOCAL

x = "awesome"

def myfunc():
  x = "fantastic" #redefiniendo el valor
  print("Python is " + x)

myfunc()

print("Python is " + x) #se utiliza el valor global

#rpta:

Python is fantastic
Python is awesome

---------------------------
#VARIABLE GLOBAL DENTRO DE UNA FUNCION LOCAL

#Para crear una variable global dentro de una función, puede usar l globalpalabra clave.

def myfunc():
  global x  
  x = "fantastic"

myfunc()

print("Python is " + x)

#rpta: 

Python is fantastic

---------------------------
#OTRO EJEMPLO

x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

#rpta: 

Python is fantastic

"""




