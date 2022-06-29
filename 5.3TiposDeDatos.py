# Diccionarios anidados
gatitos1 = {
  "fluffy":{
      "nombre":"Fluffy",
      "edad": 4,
  },
  "Mamba":{
    "nombre":"Black Mamba",
    "edad":12
  }
}
print(gatitos1)

# =================================== #
Fluffy = {
    "nombre":"Fluffy",
    "edad": 4,
}
Mamba = {
    "nombre":"Black Mamba",
    "edad":12
  }

gatitos2 ={
  "Fluffy": Fluffy,
  "Mamba": Mamba
}
print(gatitos2)

# ==============================
perritos = dict(nombre="Chanchito Feliz",edad=6)
print(perritos)


# Booleanos: True o False
verdadero = True
falso= False
print(verdadero,falso)