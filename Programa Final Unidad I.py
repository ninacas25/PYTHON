# Inicializar variables para la calificación y el número de aciertos
calificacion = 0
Aciertos = 0

# Definir las preguntas y las opciones de respuesta en una lista de tuplas
preguntas = [

    (
    "Pregunta 1. " + "¿En que país se encuentra Yucatán?",
    ["México","Francia","Estados Unidos","Brasil"], 
    1
    ),

    (
    "Pregunta 2. " + "Es un país que está en Oceanía", 
    ["Irán","China","Egipto","Nueva Zelanda"], 
    4
    ),

    (
    "Pregunta 3. " + "¿Cuál es la ciudad de los rascacielos?", 
    ["Dubai","Nueva York","Chicago","Tokio"], 
    2
    ),

    (
    "Pregunta 4. " + "¿Cuál es el río más largo del mundo?", 
    ["Nilo", "Amazonas", "Yangtsé", "Misisipi"], 
    1
    ),

    (
    "Pregunta 5. " + "¿Cuál es el planeta más grande del sistema solar?", 
    ["Venus", "Júpiter", "Marte", "Saturno"], 
    2
    ),

    (
    "Pregunta 6. " + "¿En qué país se usó la primera bomba atómica?", 
    ["China","Rusia","Japón","Siria"], 
    3
    ),

    (
    "Pregunta 7. " + "¿Quién pintó la Mona Lisa?", 
    ["Pablo Picasso", "Vincent van Gogh", "Leonardo da Vinci", "Michelangelo"],
    3
    ),

    (
    "Pregunta 8. " + "¿En qué continente se encuentra Egipto?", 
    ["Asia", "Europa", "África", "America"], 
    3
    ),

    (
    "Pregunta 9. " + "¿Cuál es el océano más grande del mundo?", 
    ["Océano Atlántico", "Océano Índico", "Océano Pacífico", "Océano Antártico"], 
    1
    ),

    (
    "Pregunta 10. " + "¿Cuántos huesos hay en el cuerpo humano?",
    ["205","224","215","206"], 
    4
    )
    ]

# Iterar a través de las preguntas, mostrar opciones y solicitar respuestas al usuario
for pregunta, opciones, respuesta in preguntas:
    print(pregunta)
    for i, opcion in enumerate(opciones):

        # pido que las opciones esten nuemradas pero i+1 para que comience en 1
        print(f"{i+1}) {opcion}")
   
    # determinar que las respuestas del usuario sea de 1 a 4
    while True:
        try:
            respuesta_usuario = int(input("\n" "Elige la opción correcta: "))
            if 1 <= respuesta_usuario <= 4:
                break
            # si el usuario pone un numero que no sea del 1 al 4
            else:
                print("Por favor, elige una opción válida (1, 2, 3, 4).")

        #en caso de que el usuario escriba otra cosa que no sea números
        except ValueError:
            print("Por favor, introduce un número válido.")

    # pedimos que nos imprima la respuesta y si es correcto o no
    if respuesta_usuario == respuesta:

        # pedimos que a la calificacion y a los Aciertos le sume 1
        Aciertos += 1
        calificacion += 1
        print("\n","CORRECTO","\n")
    else:
        print("\n","INCORRECTO","\n")

promedio = (calificacion * 100 / 10)

# Mostrar la calificación y el número de Aciertos
print("\n" "Tu calificación final es: ", calificacion, "de 10", "\n")
print("Número de Aciertos: ",Aciertos)
print("Tu promedio es de: ",promedio,"/ 100")
      