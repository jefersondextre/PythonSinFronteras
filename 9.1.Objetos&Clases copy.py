class Animal:
    def __init__(self, nombre, onomatopeya):
        self.nombre = nombre
        self.onomatopeya = onomatopeya
    
    def saludo(self):
        print(f'Hola, soy un {self.tipo} y mi sonido es el {self.onomatopeya}')
    

class Gato(Animal):
    tipo = 'gato'
    
    def __init__(self,nombre, onomatopeya):
        Animal.__init__(self,nombre,onomatopeya)
        print('Hola soy un gato extendido')

class Perro(Animal):
    tipo = 'perro'
    def __init__(self,nombre,onomatopeya):
        # super siempre hace referencia a la clase padre
        super().__init__(nombre,onomatopeya)
        print('Instanciando un perro')

class Canario(Animal):
    tipo='canario'
    

gato = Gato('Cucho','maullido')
perro= Perro('Hachikon','ladrido')
canario=Canario('Piolin','silvido')
gato.saludo()
perro.saludo()
canario.saludo()
