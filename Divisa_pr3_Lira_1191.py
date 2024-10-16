print(" ")#espacio a agregar
print("Lira Hernandez Dayana Yamileth:")#datos del realizador
print("Muestra la divisa de las variables")#descripcion del codigo
print(" ")#espacio a agregar

# Se solicita al usuario que introduzca el nombre de una divisa
divisa = {'Euro': '€', 'Dollar': '$', 'Yen': '¥', 'Won': '₩'}
# Se verifica si la divisa introducida se encuentra en el diccionario
divisa_input = input("Introduce una divisa (Euro, Dollar, Yen, Won): ")
# Si está, se imprime el símbolo correspondiente a la divisa
if divisa_input in divisa:
    print(f"La divisa de {divisa_input} es {divisa[divisa_input]}")
else:
    print("Esa divisa no esta dentro del diccionario")
# Si no está, se informa al usuario que la divisa no está en el diccionario
print(" ")#espacio a agregar