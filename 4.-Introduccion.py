# Comentario de una linea
# ? Esto es un comentario en Python
'''
Esto tambien es un comentario
de varias lineas
para colocarlo
en bloque
'''
from ast import operator


if 5 > 3:
    print('5 es mayor que 3')

if 3 < 5:
    print('3 no es mayor que 5')

# VAriables:
x = 5
y = '2daVariable'
print(x, y)
# Los Nombres de las variables deben ser mas expresivos, para saber que hacen
email = 'jadexb04@gmail.com'
print(email)

_mi_var = 'chanchito'
miVar = 'Camelcase'
MIVAR = 'variable'
mivar34 = 'Variable con numero'


# VARIABLES MULTIPLES
a, b, c = 'Lala', 'Lele', 'Lili'
print(a, b, c)

variable = A = B = C = 'otro'
print(variable, A, C)

# Concatenacion
inicio = 'Hola '
final = 'mundo'
print(inicio + final)
