# escribir código para calcular año bisiesto

# se pide al usuario que ponga un año
year = int(input("Escriba un año: "))

# otra manera de hacerlo pero dividido en partes
# print((year % 400 == 0))
# aqui se establece una concicion y la negacion 
# print(((year % 4 == 0) and (year % 100 != 0)))

# este es otra forma, pero todo de corrido
print("Es bisiesto: ", ((year % 400 == 0 ) or ((year % 4 == 0) and (year % 100 != 0))))

