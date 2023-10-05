# convertidor de monedas
# variables
tipocambio = [.85,.75,110.10]
tipomodena = ["EUR","GBD","JPY"]
montonconvetido = 0
montonAconvertir = 0

# establecer que nos del el usuario su dato
# cambio =  int(input("Inserte la moneda a convertir 0 EUR, 1 GBP, 2 JPY"))
cambio =  int(input("Inserte la moneda a convertir 0 EUR, 1 GBD, 2 JPY"))

monto = int(input ("teclea monto a convertir: "))
print(cambio, montonAconvertir)

# operaciones
montonconvetido = montonAconvertir * tipocambio [cambio]

# establece el resultado junto con el tipo de moneda y la camtidad
print ("El monto en:", tipomodena[cambio], "es",montonconvetido)
 
