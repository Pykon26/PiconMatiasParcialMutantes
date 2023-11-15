# MUTANTES

### Nombre: Matias Picon Cueli
### Correo: matipicon1@hotmail.com
### Legajo: 51619


##  De que trata este codigo

El codigo trata sobre el analisis de ADN, se busca poder detectar que personas son mutantes o no por su secuencia de ADN, validando si coinciden las mismas letras al menos 4 veces (en diagonal, horizontal, vertical). 
La mision aca es poder ingresar un secuencia completa de ADN y que se determine si es mutante o no

## Como esta hecho

La secuencia de ADN se ingresa manualmente, despues esta secuencia es almacenada en un array. A este array se le hacen distintas funciones para validar si las letras de la secuencia se repiten o no consecutivamente, estas funciones retornan la cantidad de secuencias consecutivas que encontraron.
Despues de validar todo por las funciones se suma los valores devueltos por las funciones, si es mayor que dos este valor se determina que la persona es mutante y se le pregunta al usuario si desea agregar otra secuencia

##
Tiene que ingresar una secuencia de Letras (A,T,C,G) sin espacios toda junta, tienen que ser 6 letras, si se equivoca en algo el codigo le pedira que llene nuevamente la secuencia. Asi le pedira las 6 secuencias de ADN para poder completar el array de DNA.

Luego de completado el ingreso de las secuencias se determina si es mutante o no. 
