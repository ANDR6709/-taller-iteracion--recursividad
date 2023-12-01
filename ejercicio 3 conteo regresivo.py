# EJERCICIO 3 CONTEO REGRESIVO

# IMPLEMENTA UNA FUNCION ITERATIVA QUE REALICE UN CONTEO REGRESIVO DESDE UN NUMERO DADO

# HASTA 1

# CONVIERTELA A UNA FUNCION RECURSIVA


def conteo_regresivo(num):
    num -= 1
    if num > 0:
        print(num)
        conteo_regresivo(num)
    else:
        print("Boooooooom!")
    print("Fin de la función", num)

conteo_regresivo(5)



def conteo_regresivo(num):
    print("Valor inicial ->",num)
    if num > 1:
        num = num * conteo_regresivo(num -1)
    print("valor final ->",num)
    return num

print(conteo_regresivo(5))


    