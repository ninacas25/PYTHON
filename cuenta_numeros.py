# programa que va a identificar dos números 19 y por los menos 3 números
# Elaborado por: Nina

# variables
listal = [1,3,5,5,5,5,5,7,9,11,13,15,19,19,21,25,26]
contador19 = 0
contador5 = 0

# enterar : for (es empezar a ver cada uno de ellos)
for i in range(len(listal)):

# indice = i (ordena el contemido) e igual ordena nuestros numeros de nuestra lista
# print[i, "", lista(i)]

# definir donde está el 19
    if listal[i] == 19: 
        # incrementa contador en 1 cada que se tope con un 19
        contador19 += 1
# definir donde esta el 5
    if listal [i] == 5:
        # incrementa contador en 1 cada que se tope con un 19
        contador5 += 1 
# imprime
# de declara que hay 2 19 y por lo menos hay 3 cincos
# print(contador19 == 2 and contador5 >= 3)
print (contador19, " ", contador5)

# if(contador19 == 2 and contador5 >= 3):
#     print("true")
# else:
#     print("false")
    

