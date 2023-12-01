# EJERCICIO 4 FIBONACCI SIN RECURSION

# IMPLEMENTA UNA FUNCION ITERATIVA QUE GENERE LOS PRIMEROS N NUMEROS DE LA SECUENCIA DE
# FIBONACCI


def fib(n):
   a=0
   b=1
   for k in range(n):
       c=a+b
       a=b
       b=c
       return b
   for x in range(20):
       print(fib(x))
    

