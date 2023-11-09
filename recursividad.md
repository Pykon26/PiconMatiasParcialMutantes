# Recursividad
La recursividad o recursión es un concepto que proviene de las matemáticas, y que aplicado al mundo de la programación nos permite resolver problemas o tareas donde las mismas pueden ser divididas en subtareas cuya funcionalidad es la misma.
Cualquier función recursiva tiene dos secciones de código claramente divididas:

*   Por un lado tenemos la sección en la que la función se llama a sí misma.
*    Por otro lado, tiene que existir siempre una condición en la que la función retorna sin volver a llamarse. Es muy importante porque de lo contrario, la función se llamaría de manera indefinida.
### Factorial
Uno de los ejemplos mas usados para entender la recursividad, es el cálculo del factorial de un número n!. El factorial de un número n se define como la multiplicación de todos sus números predecesores hasta llegar a uno. Por lo tanto 5!, leído como cinco factorial, sería 5x4x3x2x1
``` 
# Enfoque no recursivo

def factorial_normal(n):
    r = 1
    i = 2
    while i <= n:
        r *= i
        i += 1
    return r

# Enfoque recursivo

def factorial_recursivo(n):
    if n == 1:
        return 1
    else:
        return n * factorial_recursivo(n-1)
```
**NOTA:** Algo muy importante a tener en cuenta es que si realizamos demasiadas llamadas a la función, podríamos llegar a tener un error del tipo **RecursionError**. Esto se debe a que todas las llamadas van apilándose y creando un contexto de ejecución, algo que podría llegar a causar un **stack overflow**. Es por eso por lo que Python lanza ese error, para protegernos de llegar a ese punto.
### Serie de Fibonacci
Otro ejemplo muy usado para ilustrar las posibilidades de la recursividad, es calcular la serie de fibonacci. Dicha serie calcula el elemento n sumando los dos anteriores n-1 + n-2. Se asume que los dos primeros elementos son 0 y 1.
``` 
# Enfoque no recursivo

def fibonacci_recursivo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursivo(n-1) + fibonacci_recursivo(n-2)
```
### Ejercicio 1
Cree un programa recursivo que cuente la cantidad de cifras en un numero



```
def contar_cifras(n):
    if n < 10:
        return 1
    else:
        return 1 + contar_cifras(n // 10)

# Ejemplo de uso
numero = 3542
print(f"El número de cifras en {numero} es: {contar_cifras(numero)}")
```