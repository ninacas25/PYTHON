
# Escribe tú código aquí
# def itera(lista,inicio = 0,fin = None,incremento = 1):
def itera(lista,inicio,fin,incremento):

  for i in range(inicio,fin,incremento): # ran
    print(lista [i])

# inicio 0,1,2 fin 5,6 incremento 1,2
inicio = 1
fin = 10
incremento = 1
lista = [1,2,3,4,5,6,7,8,9,10]
itera(lista, inicio, fin, incremento)
