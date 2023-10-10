# crea funcion para el número Armtrong. El numero debe ser igual a la suma de los
#cubos de todos los digitos.153 1 al 3  = 

# variables
sum = 0
# num = 153 
num = int(input("Número Armstrong: "))

# definimos que la i se eleve al cubo y conforme pase al otro se vaya acumulando +=
for i in  str(num) :
    sum += int(i) **3

print("Es armstrong",sum == num)

