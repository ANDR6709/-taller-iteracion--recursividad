# IIERACIONES Y RECURSIVIDAD



# EJERCICIO 1   SUMA DE NUMEROS



# ESCRIBE UNA FUNCION ITERATIVA QUE SUME LOS PRIMEROS N NUMEROS NATURALES





# CONVIERTELA  A UNA FUNCION RECURSIVA

def suma_iterativa_numeros_n_naturales(n):
    suma=0
    for i in range(1,n+1):
        suma+=i
        return suma
    print(suma_iterativa_numeros_n_naturales(n))
    
    
    def suma_recursiva(n):
        
        if n==0:
            return 0
        return n+suma_recursiva(n-1)

    
    
    
   