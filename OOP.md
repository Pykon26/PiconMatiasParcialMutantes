# Programación Orientado a Objetos
La programación orientada a objetos está basada en 6 principios o pilares básicos:

*    Herencia
*    Cohesión
*    Abstracción
*    Polimorfismo
*    Acoplamiento
*    Encapsulamiento
### Clases
Cosas de lo más cotidianas como un perro o un coche pueden ser representadas con clases. Estas clases tienen diferentes características, que en el caso del perro podrían ser la edad, el nombre o la raza. Llamaremos a estas características, **atributos**.

Por otro lado, las clases tienen un conjunto de funcionalidades o cosas que pueden hacer. En el caso del perro podría ser andar o ladrar. Llamaremos a estas funcionalidades **métodos**.

Hasta antes de que existieran las clases, solo teniamos funciones que son utiles para reutilizar comportamientos. Pero tenian el problema de que no permitian guardar datos luego de la ejecucion. Por tanto para cuando nuestro codigo este enfocado en acciones debemos pensar en funciones pero cuando nuestro codigo tenga que mantener y cambiar estados a lo largo del tiempo debemos pensar en clases.

En definitiva es un tipo de variable nueva, en este caso no es un int ni un float, sino que se tratará del objeto de clase que hemos creado. Esto nos permite crear nuestros propios tipos de datos con sus respectivos atributos y funciones.
``` 
class Perro:
    # El método __init__ es un constructor
    def __init__(self, nombre, raza):
        print(f"Creando perro {nombre}, {raza}")

        # Atributos de instancia
        self.nombre = nombre
        self.raza = raza

```
Seguramente te hayas fijado en el self que se pasa como parámetro de entrada del método. Es una variable que representa la instancia de la clase, y deberá estar siempre ahí.

El uso de ** __ init __ ** y el doble __ no es una coincidencia. Cuando veas un método con esa forma, significa que está reservado para un uso especial del lenguaje. En este caso sería lo que se conoce como constructor. Hay gente que llama a estos métodos mágicos o *dunder*.

Hasta ahora hemos definido atributos de instancia, ya que son atributos que pertenecen a cada perro concreto. Ahora vamos a definir un atributo de clase, que será común para todos los perros. Por ejemplo, la especie de los perros es algo común para todos los objetos Perro.
```
class Perro:
    # Atributo de clase
    especie = 'mamífero'

    # El método __init__ es llamado al crear el objeto
    def __init__(self, nombre, raza):
        print(f"Creando perro {nombre}, {raza}")

        # Atributos de instancia
        self.nombre = nombre
        self.raza = raza
```
## Herencia
La herencia es un proceso mediante el cual se puede crear una clase hija que hereda de una clase padre, compartiendo sus métodos y atributos.
        
```
# Definimos una clase padre
class Animal:
    pass

# Creamos una clase hija que hereda de la padre
class Perro(Animal):
    pass
print(Perro.__bases__)
print(Animal.__subclasses__())
```
## Super
En pocas palabras, la función **super()** nos permite acceder a los métodos de la clase padre desde una de sus hijas. Volvamos al ejemplo de Animal y Perro
```
# Definimos una clase padre
class Animal:
    def mover():
        print("Mover")

# Creamos una clase hija que hereda de la padre
class Perro(Animal):
    def mover():
        print(super().mover()+" los pies")
```
### Herencia Múltiple
```
class Clase1:
    pass
class Clase2:
    pass
class Clase3(Clase1, Clase2):
    pass
```
Llegados a este punto nos podemos plantear lo siguiente. Que pasa si llamo a un método que todas las clases tienen en común ¿a cuál se llama?. Pues bien, existe una forma de saberlo.
La forma de saber a que método se llama es consultar el MRO o Method Order Resolution. Esta función nos devuelve una tupla con el orden de búsqueda de los métodos. Como era de esperar se empieza en la propia clase y se va subiendo hasta la clase padre, de izquierda a derecha.
```
print(Clase3.__mro__)
```