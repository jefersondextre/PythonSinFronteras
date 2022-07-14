for x in range(6):
  print(x)

print('=============')
  
for x in range(3,6):
  print(x)

print('=============')

for x in range(3,60,3):
  print(x)
else:
  print('hemos terminado')

print('=============')

usuarios = ['chanchito feliz', 'felipe', 'roberto', 'nicolas']
edades = [24,25,26,35]
for usuario in usuarios:
  for edad in edades:
    print(usuario, edad)
    # Por cada usuario  se recorre todas las edades.