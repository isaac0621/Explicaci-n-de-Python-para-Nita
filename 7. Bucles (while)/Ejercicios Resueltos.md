# 🔁 Ejercicios Resueltos — `while` en Python

---

## Ejercicio 1 — Números del 1 al 10

**Enunciado:** Mostrá en pantalla todos los números del `1` al `10`, uno por línea.

```python
numero = 1
while numero <= 10:
    print(numero)
    numero = numero + 1
```

**Salida:**
```
1
2
3
4
5
6
7
8
9
10
```

---

## Ejercicio 2 — Números del 10 al 1

**Enunciado:** Mostrá en pantalla los números del `10` al `1` en orden descendente, uno por línea.

```python
numero = 10
while numero >= 1:
    print(numero)
    numero = numero - 1
```

**Salida:**
```
10
9
8
7
6
5
4
3
2
1
```

---

## Ejercicio 3 — Números pares del 2 al 20

**Enunciado:** Mostrá solo los números pares entre `2` y `20`, uno por línea.

```python
numero = 2
while numero <= 20:
    print(numero)
    numero = numero + 2
```

**Salida:**
```
2
4
6
8
10
12
14
16
18
20
```

---

## Ejercicio 4 — Números impares del 1 al 15

**Enunciado:** Mostrá solo los números impares entre `1` y `15`, uno por línea.

```python
numero = 1
while numero <= 15:
    print(numero)
    numero = numero + 2
```

**Salida:**
```
1
3
5
7
9
11
13
15
```

---

## Ejercicio 5 — Contar hasta un número

**Enunciado:** Pedile al usuario un número y mostrá todos los números del `1` hasta ese número.

```python
limite = int(input("Ingresá un número: "))
contador = 1
while contador <= limite:
    print(contador)
    contador = contador + 1
```

**Ejemplo de ejecución:**
```
Ingresá un número: 5
1
2
3
4
5
```

---

## Ejercicio 6 — Números hasta el cero

**Enunciado:** Pedí números al usuario uno por uno. Cuando ingrese `0`, el programa debe detenerse.

```python
numero = int(input("Ingresá un número (0 para salir): "))
while numero != 0:
    print("Ingresaste:", numero)
    numero = int(input("Ingresá un número (0 para salir): "))
print("Saliste del programa.")
```

**Ejemplo de ejecución:**
```
Ingresá un número (0 para salir): 7
Ingresaste: 7
Ingresá un número (0 para salir): 3
Ingresaste: 3
Ingresá un número (0 para salir): 0
Saliste del programa.
```

---

## Ejercicio 7 — Suma hasta el cero

**Enunciado:** Pedí números al usuario y sumalos. Cuando ingrese `0`, mostrá el total acumulado.

```python
total = 0
numero = int(input("Ingresá un número (0 para terminar): "))
while numero != 0:
    total = total + numero
    print("Total hasta ahora:", total)
    numero = int(input("Ingresá un número (0 para terminar): "))
print("Total final:", total)
```

**Ejemplo de ejecución:**
```
Ingresá un número (0 para terminar): 10
Total hasta ahora: 10
Ingresá un número (0 para terminar): 5
Total hasta ahora: 15
Ingresá un número (0 para terminar): 20
Total hasta ahora: 35
Ingresá un número (0 para terminar): 0
Total final: 35
```

---

## Ejercicio 8 — Contar cuántos números ingresa el usuario

**Enunciado:** Pedí números al usuario. Cuando ingrese `0`, mostrá cuántos números escribió en total (sin contar el `0`).

```python
contador = 0
numero = int(input("Ingresá un número (0 para terminar): "))
while numero != 0:
    contador = contador + 1
    numero = int(input("Ingresá un número (0 para terminar): "))
print("Ingresaste", contador, "números en total.")
```

**Ejemplo de ejecución:**
```
Ingresá un número (0 para terminar): 4
Ingresá un número (0 para terminar): 9
Ingresá un número (0 para terminar): 1
Ingresá un número (0 para terminar): 0
Ingresaste 3 números en total.
```

---

## Ejercicio 9 — Tabla del 3

**Enunciado:** Mostrá la tabla de multiplicar del `3` del `1` al `10` usando un bucle `while`.

```python
numero = 1
while numero <= 10:
    resultado = 3 * numero
    print("3 x", numero, "=", resultado)
    numero = numero + 1
```

**Salida:**
```
3 x 1 = 3
3 x 2 = 6
3 x 3 = 9
3 x 4 = 12
3 x 5 = 15
3 x 6 = 18
3 x 7 = 21
3 x 8 = 24
3 x 9 = 27
3 x 10 = 30
```

---

## Ejercicio 10 — Sistema de contraseña

**Enunciado:** Pedí una contraseña al usuario repetidamente hasta que ingrese la correcta (`"1234"`). Al lograrlo, mostrá un mensaje de acceso concedido.

```python
contrasena_correcta = "1234"
intento = input("Ingresá la contraseña: ")
while intento != contrasena_correcta:
    print("❌ Contraseña incorrecta. Intentá de nuevo.")
    intento = input("Ingresá la contraseña: ")
print("✅ Acceso concedido. ¡Bienvenido!")
```

**Ejemplo de ejecución:**
```
Ingresá la contraseña: hola
❌ Contraseña incorrecta. Intentá de nuevo.
Ingresá la contraseña: 0000
❌ Contraseña incorrecta. Intentá de nuevo.
Ingresá la contraseña: 1234
✅ Acceso concedido. ¡Bienvenido!
```

---

> 💡 **Recordá:** Estos son solo una forma de resolver cada ejercicio. Puede haber otras soluciones igualmente válidas.
