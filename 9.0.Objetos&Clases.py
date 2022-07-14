# Clase Padre
class Usuario:

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def saludo(self):
        print(f'Hola, mi nombre es {self.nombre} {self.apellido}')
# ===========Clase Hijo============================
class Admin(Usuario):

    def superSaludo(self):
        print(f'Hola, me llamo {self.nombre} y soy Administrador')



# Instanciando clase Usuario
usuario = Usuario('Carlos', 'Fernandez')

# print(usuario.nombre)
# print(usuario.apellido)
# print(usuario2.nombre)
# print(usuario2.apellido)

usuario.saludo()
# Cambiando propiedades de las instancias 
usuario.nombre='chanchito'
usuario.saludo()
# Quitandole propiedades a la clase y la instancia
# del usuario.nombre
# del usuario
usuario.saludo()

admin = Admin('Jeferson','Dextre')

admin.saludo()
admin.superSaludo()

# usuario.superSaludo()   de la clase padre no se puede llamar a metodos de la clase hija

