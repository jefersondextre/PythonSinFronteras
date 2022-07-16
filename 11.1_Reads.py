# open('path_file','r') 
# Le pasamos permisos del archivo:
# r read  .Para permitir leer el archivo
# a append  . Modificar el archivo agregando al final de lo ya contenido
# w write .    En caso de no existir el archivo se creará . se abrirá
# x     Si el archivo no se crea se creara, si ya existe nos mandara un error
c= open('chanchito.txt','r')
# read() Leemos todo el contenido del archivo
# print(c.read())
# readline() Permite leer el archivo linea a linea
print(c.readline())
print(c.readline())

# Control mas especifico para todas las lineas

for x in c:
  print(x)

# Una ves leido el archivo lo cerraremos con close()
c.close()