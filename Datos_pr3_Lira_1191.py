
print(" ")#espacio a agregar
print("Lira Hernandez Dayana Yamileth:")#datos del realizador
print("Muestra los datos del usuario en un diccionario")#descripcion del codigo
print(" ")#espacio a agregar

usuario = {}
#Solicita nombre, edad, direccion y telefono al usuario
usuario['nombre'] = input("Introduce tu nombre: ")#se almacena en el diccionario
usuario['edad'] = input("Introduce tu edad: ")#se almacena en el diccionario
usuario['direccion'] = input("Introduce tu dirección: ")#se almacena en el diccionario
usuario['telefono'] = input("Introduce tu número de teléfono: ")#se almacena en el diccionario
#imprime lo ingresado en un orden especifico
print(f"{usuario['nombre']} tiene {usuario['edad']} años,")
print(f"vive en {usuario['direccion']} ")
print(f"y su número de teléfono es {usuario['telefono']}.")

print(" ")#espacio a agregar