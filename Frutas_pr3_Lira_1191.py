print(" ")#espacio a agregar
print("Lira Hernandez Dayana Yamileth:")#datos del realizador
print("Muestra el precio por kilo de fruta elegida")#descripcion del codigo
print(" ")#espacio a agregar

precios_frutas = {
    'manzana': 3.0,# Precio por kilo
    'plátano': 2.5,# Precio por kilo
    'naranja': 4.0,# Precio por kilo
    'fresa': 5.5 # Precio por kilo
}

# Preguntar al usuario por la fruta y el número de kilos
fruta_input = input("Introduce la fruta (manzana, plátano, naranja, fresa): ")
# Solicita la fruta
kilos_input = float(input("Introduce el número de kilos: "))
# Solicita los kilos
#Verifica si la fruta ingresada está en el diccionario
if fruta_input in precios_frutas:
    precio_total = precios_frutas[fruta_input] * kilos_input
    print(f"El precio total de {kilos_input} kilos de {fruta_input} es: ${precio_total:.2f}")
else: #Informa al usuario si la fruta no está en el diccionario
    print("La fruta seleccionada no está en el diccionario.")
print(" ")#espacio a agregar