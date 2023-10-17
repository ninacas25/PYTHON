# argumentos
# con el asterisco se entiende que es un listado de datos

# defien variable de suma
# itera por cada elemento de parms
# suma los elementos de parms
# regresa el valor de la suma

def sum(*datos):
    sum = 0
    
    for i in datos:
        sum += i
    return sum

datos = [1,2,3,4,5]
print(sum(*datos))

