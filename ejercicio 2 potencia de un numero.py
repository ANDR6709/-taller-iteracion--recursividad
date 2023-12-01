 # EJERCICIO 2 POTENCIA DE UN NUMERO
 
 # CREA UNA FUNCION ITERATIVA QUE CALCULE LA POTENCIA DE UN NUMERO, POR EJEMPLO
 # BASE EXPONENTE
 
 # CONVIERTELA A UNA FUNCION RECURSIVA
 
 
def potencia_iterativa(a,b):
     resultado=1
     for i in range(b):
         resultado*=b
         return resultado
     print(a*b)
     
     print(potencia_iterativa(a,b))
     
     
     
     def potencia_recursiva(a,b):
         if  b ==0:
             return 1
         elif a==0:
             return 0
         elif b==1:
             return a
         else:
             return a * potencia_recursiva(a,b-1)
         
         
             
             
             
     
     
           
     
 
 