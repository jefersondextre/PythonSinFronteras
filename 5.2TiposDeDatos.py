# Rangos
'''
Permite tener muchos elementos desde uno inicial hasta otro final que vamos a determinar
Se puede modificar de un elemento inicial a otro final
usado en las iteraciones
'''
from cgi import print_arguments


rango = range(6)
print(rango)

# Diccionarios
'''
Son como los objetos javascript
'''
diccionario = {
  "nombre":"Silvestre",
  "raza":"siames",
  "edad":5
}

print(diccionario)
print(diccionario["nombre"])
print(diccionario["raza"])
# Accediendo por metodo
print(diccionario.get('nombre'))
# Cambiando valores del diccionario
diccionario["nombre"]="Tom"
print(diccionario)
# longitud de elementos del diccionario
print(len(diccionario))
# Añadiendo una propiedad 
diccionario["ronronea"]='SI'
print(diccionario)
# Eliminar elemento del diccionario
diccionario.pop("ronronea")
print(diccionario)
# Eliminando el ultimo elemento o el ultimo agregado del diccionario
diccionario.popitem()
print(diccionario)

del diccionario["nombre"]
print(diccionario)

print("=========")
copiaGatito = diccionario.copy()
copiaGatito2 = dict(diccionario)
print(copiaGatito,copiaGatito2)
# Eliminando elementos del diccionario
diccionario.clear() 
print(diccionario)