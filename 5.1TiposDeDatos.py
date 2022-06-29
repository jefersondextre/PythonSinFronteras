# Strings y numeros
# ======================
# String
palabra = 'hola mundo'
oracion = "hola mundo comilla doble"
# entero
entero = 25
# float
decimales = 20.5
# complejos
complejo= 1j
# print(palabra, oracion  ,entero,decimales,complejo)

# Listas
lista1 = []
lista = [1,2,3]
print(lista)

lista.append(4)
print(lista)

lista2=lista.copy()
print('lista2 '+str(lista2))

print(lista2.count(4))
print(len(lista))
largoLista=len(lista)
largoLista2=len(lista2)
print(largoLista,largoLista2)

# print(lista2)

# lista.clear()
# print(lista)

# Eliminando elementos a una lista
lista3=['uno','dos','tres']
# Eliminando el ultimo elemento de la lista3
lista3.pop()
print(lista3)
# Elimina un elemento en particular de la lista3
lista3.remove('uno')
print(lista3)
# invertir el orden de la lista4
lista4=['PHP','JAVASCRIPT','PYTHON','HTML',str(7)]
lista4.reverse()
print(lista4)

# Ordenando listas pero que sean del mismo tipo de datos
lista4.sort()
print(lista4)

# TUPLAS --- No se pueden modificar directamente(), 
tupla=('HOLA','MUNDO','SOMOS','TUPLA')
print(tupla)
print(tupla[0])

print(tupla.count('hola'))

# Posicion del elemento buscado
tupla2=tupla.index('SOMOS')
print(tupla2)

# Para modficar las tuplas tenemos que 
# transformarlas a una lista y luego recien modificarlo.
listaDeTupla=list(tupla)
listaDeTupla.append('chanchito feliz')
print(listaDeTupla)