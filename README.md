# Ejercicios de listas y diccionarios

# 1. Agregar y eliminar elementos de una lista

Crea una lista con 5 frutas. Luego:

- agrega una fruta al final con append()
- inserta una fruta en la posición 2 con insert()
- elimina una fruta con remove()
- elimina el último elemento con pop()
- Objetivo: practicar modificación básica de listas.

# 2. Ordenar y contar elementos en una lista

Dada esta lista:

```py
numeros = [4, 2, 7, 2, 9, 1, 2]
```

Haz lo siguiente:

- ordénala con sort()
- invierte el orden con reverse()
- cuenta cuántas veces aparece el número 2 con count()
- busca en qué posición aparece el número 7 con index()
- Objetivo: usar métodos de búsqueda y ordenamiento.

# 3. Copiar y extender listas

Crea dos listas:

```py
a = [1, 2, 3]
b = [4, 5, 6]
```

Luego:

- copia a en otra lista usando copy()
- une b a la copia usando extend()
- muestra la lista final
- Objetivo: entender la diferencia entre copiar y modificar.

# 4. Vaciar una lista

Crea una lista con nombres de estudiantes. Después:

- muestra la lista original
- vacíala completamente con clear()
- imprime la lista otra vez

Objetivo: practicar cómo borrar todos los elementos de una lista.

# 5. Crear y consultar un diccionario

Crea un diccionario con información de una persona:

```py
persona = {
    "nombre": "Ana",
    "edad": 25,
    "ciudad": "Bogotá"
}
```

Luego:

- muestra el valor de "nombre"
- usa get() para consultar "edad"
- usa get() para consultar "telefono" y devuelve "No existe" si no está
- Objetivo: practicar acceso seguro a claves.

# 6. Agregar, actualizar y eliminar claves en un diccionario

Con el diccionario del ejercicio anterior:

- agrega una nueva clave "profesion"
- cambia la edad por otro valor
- elimina "ciudad" usando pop()
- imprime el valor eliminado y el diccionario final
- Objetivo: modificar diccionarios y usar pop().

# 7. Recorrer claves, valores y elementos

Crea un diccionario de productos con precios. Por ejemplo:

```py
productos = {
    "pan": 1500,
    "leche": 3200,
    "huevos": 9000
}
```

Haz lo siguiente:

- recorre las claves con keys()
- recorre los valores con values()
- recorre clave y valor con items()
- Objetivo: aprender distintas formas de recorrer un diccionario.

# 8. Unir diccionarios y actualizar datos

Crea dos diccionarios:

```py
d1 = {"a": 1, "b": 2}
d2 = {"b": 5, "c": 3}
```

Luego:

- une d2 dentro de d1 usando update()
- imprime el resultado
- observa qué pasó con la clave "b"
- Objetivo: entender cómo funciona update().

# 9. Eliminar el último par clave-valor

Crea un diccionario con al menos 4 elementos. Después:
* elimina el último elemento insertado con popitem()
* muestra qué elemento se eliminó 
* imprime el diccionario restante Objetivo: practicar popitem().

# 10. Combinar listas y diccionarios

Crea una lista de diccionarios con información de 3 estudiantes, por ejemplo:

```py
estudiantes = [
    {"nombre": "Luis", "nota": 4.5},
    {"nombre": "Marta", "nota": 3.8},
    {"nombre": "Carlos", "nota": 4.2}
]
```

Haz lo siguiente:

- imprime el nombre de cada estudiante
- calcula el promedio de las notas
- muestra solo los estudiantes con nota mayor a 4.0
- Objetivo: combinar listas y diccionarios en un mismo ejercicio.