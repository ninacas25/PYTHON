# definimos que es decimal a binario
def decimalBinary(numero):
# el "" clasifica como un string
    bi = ""
    if decimal == 0:
        return "0"

# clasificamos el procediiento del binario
    while numero // 2 >= 1:
    # define variables y operaciones
        bi = str(numero % 2) + bi
        numero = numero // 2

# retornar el resultado de la funcipon a la variable binario
    return str(numero) + bi

decimal  = int(input("Inserte el valor que desea convertir a binario: "))
binario = decimalBinary(decimal)

#print("Su numero {} en binario es {}".format(decimal, binario) )
print('Su numero ',decimal, ' en binario es ',binario)
 

