# Funciones

from re import I


def miFuncion():
    x = 0
    while x < 5:
        x += 1
        print(f' Mi función número {x}')


miFuncion()
miFuncion()


def imprimeDato(argumento1):
    print('Mi argumento es', argumento1)


imprimeDato('Parametro')
# =========================================
# Valor por default


def saludar(nombre, apellido='value_default'):
    print(f'Mi nombre completo es {nombre} {apellido}')


saludar('Jeferson', 'Dextre')
saludar('Jeferson')

# ====================================


def ListaConvocados(*convocado):
    print(f'Los comvocados son: {convocado}')


ListaConvocados('Galesse', 'Lapadula', 'Flores', 'Ruiz Diaz', 'Trauco')
# imprimiendo como tupla
# convirtio de tupla a lista o


# ========================================
def ListaConvocados2(*convocado):
    print(f'El arquero sera : {convocado[0]}')


ListaConvocados2('Galesse', 'Lapadula', 'Flores', 'Ruiz Diaz', 'Trauco')
# =====================================
# usando el nombre de los argumentos para identificarlos y no la posicion


def nombrecompleto(apellido, nombre):
    print(nombre, apellido)


nombrecompleto(nombre='chanchito', apellido='feliz')


# ===================
def nombrecompleto2(**kwargs):
    print(kwargs['nombre'], kwargs['apellido'])


nombrecompleto2(nombre='Chanchito', apellido='FFeliz')

# En lugar de agrupar los argumentos en una lista o un diccionario nosotros le pasemos una lista como argumento


def miFuncionLista(lista):
    for elemento in lista:
        print(elemento)


miFuncionLista(['chanchito', 'feliz'])

# retornando valores
def concatenaNombres(lista):
    i = ''
    for el in lista:
        i = i+el+' '
    return i


nombres = concatenaNombres(['chanchito', 'feliz'])
print(nombres)
