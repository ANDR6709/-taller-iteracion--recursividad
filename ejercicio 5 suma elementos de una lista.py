# EJERCICIO 5 SUMA ELEMENTOS DE UNA LISTA

# CREA UNA FUNCION ITERATIVA QUE SUME TODOS LOS ELEMENTOS DE UNA LISTA

# CONVIERTELA A UNA FUNCION RECURSIVA


def suma(listaNumeros):
    for numero in listaNumeros:
         print(numero)
         if numero==listaNumeros[0]:
             print(numero)
             suma(listaNumeros[0+1])
         else:
             listaNumeros=[1,2,3,4,5,6,7,8]
             suma(listaNumeros)
           


def sumar(lista):
    if len(lista) == 1:
        print(lista[0])
        return lista[0]
    else:
        print(lista[0])
        return lista[0] + sumar(lista[1:])



listaNumeros = [1,2,3,4,5,6,7,8]
print("Total Sumado: ", sumar(listaNumeros))
   