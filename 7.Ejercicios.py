# dato = input('Ingrese dato: ')
# lista = ['hola','chanchito','feliz','mundo']

# if lista.count(dato) >0:
#   print('El dato existe:',dato)
# else:
#   print('El dato no existe :( ',dato)
  
  
  
# ==== CALCULADORA ====

primero=input('Ingrese primer número: ')
try:
  primero= int(primero)
except:
  primero = 'chanchito feliz'

if primero == 'chanchito feliz':
  print('el valor ingresado no es un entero')
  exit()

segundo=input('Ingrese segundo número: ')
try:
  segundo = int(segundo)
except:
  segundo = 'chanchito feliz'
  
if segundo == 'chanchito feliz':
  print('el valor ingresado no es un entero')
  exit()

simbolo = input('Ingrese la operación: ')

if simbolo == '+':
    print('Suma:',primero + segundo)
elif simbolo == '-':
    print('Resta: ',primero - segundo)
elif simbolo == '*':
    print('Multiplicación:', primero * segundo)
elif simbolo == '/':
  if segundo == 0 :
    print('La División por cero no es válida')
    exit()
  print('División: ', primero / segundo)
else:
  print('No ingreso un operador válido')    






# if primero == 'chanchito feliz' or segundo == 'chanchito feliz':
#   print('Ingresaste mal un dato, prueba nuevamente solo con numeros')
# else:


# print(int(primero) + int(segundo))