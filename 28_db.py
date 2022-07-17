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


cursor.execute('select * from Usuario')


# ----- fetchall vs fetchone --------
resultado = cursor.fetchall()
# fetchall devuelve todos los registros encontrados
# resultado = cursor.fetchone()
# fetchone devuelve solo el primer registro encontrado

print(resultado)