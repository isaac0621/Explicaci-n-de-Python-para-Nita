# 📝 Examen 2 – Soluciones

# 1. Control de acceso
edad = int(input("Edad: "))
if edad >= 18:
    print("Puede ingresar")
else:
    print("No puede ingresar")

# 2. Cálculo de compra
precio = float(input("Precio: "))
cantidad = int(input("Cantidad: "))
total = precio * cantidad
print("Total:", total)

# 3. Validación de edad
while True:
    edad = int(input("Ingrese edad válida: "))
    if edad > 0:
        break

# 4. Pedir números hasta 0
while True:
    numero = int(input("Número (0 para salir): "))
    if numero == 0:
        break

# 5. Clasificación de nota
nota = int(input("Nota: "))
if nota >= 90:
    print("Excelente")
elif nota >= 70:
    print("Aprobado")
else:
    print("Reprobado")

# 6. Acumulador
total = 0
while True:
    numero = int(input("Número: "))
    total += numero
    seguir = input("¿Seguir? (si/no): ")
    if seguir == "no":
        break
print("Total acumulado:", total)

# 7. Comparación
a = int(input("Número 1: "))
b = int(input("Número 2: "))
if a > b:
    print("Mayor:", a)
else:
    print("Mayor:", b)

# 8. Menú simple
while True:
    print("\n1. Saludar\n2. Salir")
    opcion = input("Opción: ")

    if opcion == "1":
        print("Hola 👋")
    elif opcion == "2":
        break

# 9. Par o impar
numero = int(input("Número: "))
if numero % 2 == 0:
    print("Par")
else:
    print("Impar")

# 10. Conteo
contador = 0
while True:
    numero = int(input("Número (0 para salir): "))
    if numero == 0:
        break
    contador += 1

print("Cantidad de números ingresados:", contador)
