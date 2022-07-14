usuarios= ['chanchito feliz','felipe','roberto','nicolas']

for usuario in usuarios:
  print(usuario)

print('===================== ')
usuario2 = 'chanchito felilz'
for c in usuario2:
  print(c)
  

print('========= break ============ ')
usuarios3 = ['chanchito feliz', 'felipe', 'roberto', 'nicolas']

for usuario in usuarios3:
  if usuario == 'roberto':
    break
  print(usuario)

print('========== continue =========== ')
for usuario in usuarios3:
  if usuario == 'roberto':
    continue
  print(usuario)
