# Recursividad - por ejemplo sonutiles para hacer intentos de coneccion a un servidor 
def recursion(i):
  if(i<1):
    return i
  print(i)
  recursion(i-1)
  
recursion(6)