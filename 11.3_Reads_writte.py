# open('path_file','r') 
# Le pasamos permisos del archivo:
# r read  .Para permitir leer el archivo
# a append. Modificar el archivo agregando al final de lo ya contenido
# w write .    En caso de no existir el archivo se creará . Si ya existe se abrirá sobreescribiendo lo ya contiene borrando lo anterior
# x     Si el archivo no se crea se creara, si ya existe nos mandara un error
c= open('chanchito.txt','w')
# read() Leemos todo el contenido del archivo
# print(c.read())
# readline() Permite leer el archivo linea a linea
c.write('\nAgregaremos una nueva linea a nuestro archivo ')
# print(c.readline())

# Una ves leido el archivo lo cerraremos con close()
c.close()

x=open('chanchito.txt',)
print(x.read())