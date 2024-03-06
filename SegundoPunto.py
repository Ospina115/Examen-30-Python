#2. Elabore un programa en Python que permita leer la información de un usuario
#Y la almacene en un diccionario. La información del usuario es la siguiente(15 ptos):
#id
#nombres
#apellidos
#ubicación
#dirección
#ciudad
#longitud
#latitud
#email
#edad
#ocupación

user_info = {}

user_info['id'] = input("Ingrese su ID: ")
user_info['nombres'] = input("Ingrese sus NOMBRES: ")
user_info['apellidos'] = input("Ingrese sus APELLIDOS: ")
user_info['ubicacion'] = input("Donde se ubica?: ")
user_info['direccion'] = input("Ingrese su direccion: ")
user_info['ciudad'] = input("En Que ciudad?: ")
user_info['longitud'] = input("Longitud de la ciudad: ")
user_info['latitud'] = input("Latitud de la ciudad: ")
user_info['email'] = input("Ingrese su Email: ")
user_info['edad'] = input("Cual es su edad?: ")
user_info['ocupacion'] = input("A que se dedica?: ")

print("Informacion del usuario:")
print(user_info)