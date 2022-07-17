import mysql.connector
# importamos el paquete mysql.connector

# Creamos una instancia del paquete con el metodo connect con sus parametros requeridos
midb=mysql.connector.connect(
  host='localhost',
  user='root',
  password='123456',
  database='prueba'
)


# Un cursor es un objeto que nos permite interactuar con la base de datos mediante sql
cursor=midb.cursor()

sql='insert into Usuario (email,username,edad) values(%s,%s,%s)'
values=('miCorreo@outlook.com','nombreUsuario',35)

cursor.execute(sql,values)
# cursor.execute('select * from Usuario')
# cursor.execute('show create table Usuario')

# Comprometiendo los cambios
# Tomara los datos en execute y ejecutar la consulta sql directamente con la base de datos
midb.commit()
# Llamamos ahora a rowcount
print(cursor.rowcount)

# ----- fetchall vs fetchone --------
# resultado = cursor.fetchall()
# fetchall devuelve todos los registros encontrados
# resultado = cursor.fetchone()
# fetchone devuelve solo el primer registro encontrado

# print(resultado)