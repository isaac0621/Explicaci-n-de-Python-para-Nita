# 🔥 True en Python

## 🧠 ¿Qué es `True`?

`True` es un valor booleano en Python que significa **"verdadero"**. Es uno de los dos valores posibles del tipo `bool` (el otro es `False`).

```python
print(True)  # Salida: True
```

---

## 📌 ¿Dónde se usa?

Se usa principalmente en **condiciones y bucles** para controlar el flujo de un programa.

### Ejemplo básico con `if`

```python
if True:
    print("Esto siempre se ejecuta")
```

---

## 📂 ejemplos.py

### Ejemplo 1 — Condición siempre verdadera

```python
if True:
    print("Siempre se ejecuta")
```

### Ejemplo 2 — Bucle con `break`

```python
while True:
    print("Hola")
    break
```

### Ejemplo 3 — Bucle interactivo con condición de salida

```python
while True:
    texto = input("Escribí algo (salir para terminar): ")
    if texto == "salir":
        break
    print("Ingresaste:", texto)
```

---

## 💡 Notas

- `True` siempre va con **mayúscula** en Python (es sensible a mayúsculas).
- Usar `while True:` crea un **bucle infinito** que solo termina con un `break` o interrupción manual.
- En contextos numéricos, `True` equivale a `1`.
