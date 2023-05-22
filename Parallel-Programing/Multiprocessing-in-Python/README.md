# Multiprocessing in Python — LucidProgramming <!-- omit in toc -->

En este curso vamos a aprender a usar el módulo ``multiprocessing``.

1. Introducción
   
2. Bloqueos
3. Inicio de sesión
4. Pool
5. Comunicación entre procesos



## Introducción

### Parte 1

Python está diseñado para que el código se ejecute en un hilo a la vez. El mecanismo responsable de esto es el Global Interpreter Lock (GIL). La biblioteca ``multiprocessing`` elude este bloqueo: permite que todos los núcleos de procesamiento de nuestra PC puedan trabajar simultáneamente en la ejecución del código.



