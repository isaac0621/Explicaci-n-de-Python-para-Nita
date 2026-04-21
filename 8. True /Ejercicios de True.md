# 🔥 Ejercicios — `True` en Python

Practicá el uso de `True` en condiciones y bucles con estos ejercicios progresivos.

---

## Ejercicio 1 — Mensaje con `if True`

**Enunciado:** Escribí un bloque `if` que siempre se ejecute e imprima un mensaje de bienvenida.

**Debe usar:** `if`, `True`, `print()`

**Pista:** Si la condición es literalmente `True`, el bloque siempre se ejecuta sin necesidad de evaluar nada.

```python
# Tu código aquí
```

---

## Ejercicio 2 — Bucle que imprime una sola vez

**Enunciado:** Creá un bucle infinito que imprima `"Hola"` una única vez y luego se detenga.

**Debe usar:** `while True`, `print()`, `break`

**Pista:** `break` corta el bucle en el momento en que Python lo encuentra.

```python
# Tu código aquí
```

---

## Ejercicio 3 — Bucle con palabra de salida

**Enunciado:** Pedile texto al usuario repetidamente. Cuando escriba `"fin"`, el programa debe terminar.

**Debe usar:** `while True`, `input()`, `if`, `break`

**Pista:** Compará el valor ingresado con el string `"fin"` dentro del bucle.

```python
# Tu código aquí
```

---

## Ejercicio 4 — Números hasta el cero

**Enunciado:** Pedí números al usuario uno por uno. Cuando ingrese `0`, el programa debe detenerse.

**Debe usar:** `while True`, `input()`, `int()`, `if`, `break`

**Pista:** Convertí el input a número con `int()` antes de compararlo con `0`.

```python
# Tu código aquí
```

---

## Ejercicio 5 — Menú repetible

**Enunciado:** Mostrá un menú con opciones numeradas. El menú debe volver a aparecer después de cada elección hasta que el usuario elija la opción de salir.

**Debe usar:** `while True`, `print()`, `input()`, `if`, `break`

**Pista:** Usá varios `if` / `elif` para manejar cada opción, y reservá una para el `break`.

```python
# Tu código aquí
```

---

## Ejercicio 6 — Nombre obligatorio

**Enunciado:** Pedí el nombre del usuario. Si deja el campo vacío y presiona Enter, volvé a pedirlo hasta que escriba algo.

**Debe usar:** `while True`, `input()`, `if`, `break`

**Pista:** Un string vacío `""` es falsy en Python; podés usar `if nombre:` para verificar que no esté vacío.

```python
# Tu código aquí
```

---

## Ejercicio 7 — Edad válida

**Enunciado:** Pedí la edad del usuario. Si ingresa `0` o un número negativo, volvé a pedirla hasta obtener un valor mayor a `0`.

**Debe usar:** `while True`, `input()`, `int()`, `if`, `break`

**Pista:** Convertí el input a entero y verificá que sea `> 0` antes de aceptarlo.

```python
# Tu código aquí
```

---

## Ejercicio 8 — Repetidor de mensajes

**Enunciado:** Pedí un mensaje al usuario e imprimilo. Repetí esto hasta que el usuario escriba `"no"`.

**Debe usar:** `while True`, `input()`, `print()`, `if`, `break`

**Pista:** Chequeá la respuesta del usuario *después* de imprimir el mensaje, no antes.

```python
# Tu código aquí
```

---

## Ejercicio 9 — Sistema de login

**Enunciado:** Simulá un login. Pedí la contraseña repetidamente hasta que el usuario ingrese la correcta (`"python123"`). Al lograrse, mostrá un mensaje de acceso concedido.

**Debe usar:** `while True`, `input()`, `if`, `break`, `print()`

**Pista:** Guardá la contraseña correcta en una variable antes del bucle y comparala con el input.

```python
# Tu código aquí
```

---

## Ejercicio 10 — Suma acumulada

**Enunciado:** Pedí números al usuario y sumalos. Cuando escriba `"stop"`, mostrá el total acumulado y terminá el programa.

**Debe usar:** `while True`, `input()`, `int()`, `if`, `break`, una variable acumuladora

**Pista:** Inicializá una variable `total = 0` antes del bucle y sumale cada número ingresado.

```python
# Tu código aquí
```

---

> 💡 **Recordá:** `while True` crea un bucle infinito. Siempre necesita un `break` para poder terminar.
