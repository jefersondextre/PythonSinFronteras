import modulos as xs
from camelcase import CamelCase 

c = CamelCase()

s = 'Esta oracion necesita CamelCase'
camelcased = c.hump(s)
print(camelcased)


# from modulos import saludo,otroMetodo, otracosa
# from modulos import saludo

# print(xs.mascotas)

# xs.saludo('Nicolas')

# saludo('Jeferson')

# PIP es un administrador de paquetes instalados en Python, permitiendonos instalar modulos, listar , agregar, eliminar modulos

# pypi.org