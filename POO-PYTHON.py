
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

---------------------------
#Valores Nulos

import pandas as pd

data = pd.DataFrame([[20, 1000], [None, 2000], [30, 3000]], columns=['edad', 'ingresos'])

# Detección de valores nulos
valores_nulos = data.isnull()

# Suma de valores nulos por columna
cantidad_nulos_por_columna = valores_nulos.sum()

print("Cantidad de valores nulos por columna:")
print(cantidad_nulos_por_columna)

# Posiciones de los valores nulos
posiciones_nulos = {}
for columna in data.columns:
    posiciones_nulos[columna] = list(data.index[data[columna].isnull()])

print("\nPosiciones de los valores nulos por columna:")
print(posiciones_nulos)

-----------------------

#Tratamiento de valores nulos

base = pd.read_csv("https://raw.githubusercontent.com/PacktWorkshops/The-Pandas-Workshop/master/Chapter07/Data/deletion.csv")
base
base.isnull().sum()

import seaborn as sns #forma visual de ver los valores nulos
sns.heatmap(base.isnull())

#Imputacion

base["population"].fillna(base["population"].mean(), inplace = True)
base

"""





