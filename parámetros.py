# # parámetros por valor o por referencia
# def funcion(x):
#     # funcion
#     print("Origina: ",x)
#     x = 10
#     print("Nuevo: ",x)

#     # código principal
#     # se corre a la izquierda por que es el código principal y
#     # si se alinea con el de arriba da a entender que es parte de y es un arreglo, entonces
#     # por eso se mueve
# x = 20
# y = funcion(x)
# print("Valor retornado: ",x)

# crea tu funcion aqui
def  funcion(valor, referencia):
    # cambia el valor
    # hace que agregemos valores a referencia como una lista
    referencia.append(5)
    referencia.append(6)
    referencia.append(7)

# cambia la referecia agregar un elemento por ejemplo 5
# el valor debe estar abajo de .append para que lo agrarre, ya que si esta arriba de no lo va agarrar

valor = 5
# en reerencia va a salir los numeros que agregamos en .append
referencia = []

# aqui nos imprime las funciones
funcion(valor, referencia)
print("Valor ",valor)
print("referencia", referencia)


