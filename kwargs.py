# kwargs

# def myFunc(**kwargs):
#     for key, value in kwargs.items():
#         print("%s == %s" % (key, value))
#         print(type(value))

# myFunc(nombre="Nina",apellido_1="Casanova", apellido_2="Cruz")


def myFunc(**kwargs):
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))
        print(type(value))
        
nombres = ["Nina", "Dennis", "Ernesto"]
edades = [18,21,23]
alturas = [1.59,1.74,1.75]

for i in range(len(nombres)):

    myFunc(Nombre=nombres[i], Edad=edades[i], Alturas=alturas[i])
    