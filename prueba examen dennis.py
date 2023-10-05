# Inicializar variables para la calificación y el número de aciertos
calificacion = 0
aciertos = 0
Fallados = 0

# Definir las preguntas y las opciones de respuesta en una lista de tuplas
preguntas = [
    (
    "Pregunta: " + "¿En que país se encuentra Yucatán?", 

    ["México","Francia","Estados Unidos","Brasil"], 
    
      0
    )
]
    # (
    # "pregunta:" "Es un país que está en Oceanía", 
    #["Irán","China","Egipto","Nueva Zelanda"], 
    #"Nueva Zelanda"
    # ),

    # (
    # "pregunta:" "¿Cuál es la ciudad de los rascacielos?", 
    #["Dubai","Nueva York","Chicago","Tokio"], 
    #   "Nueva York"
    #  ),

    # (
    # "pregunta:" "¿Cuál es el río más largo del mundo?", 
    # "opciones;" ["Nilo", "Amazonas", "Yangtsé", "Misisipi"], 
    #  "Nilo"
    # ),

    # (
    # "¿Cuál es el planeta más grande del sistema solar?", 
    #["Venus", "Júpiter", "Marte", "Saturno"], 
    #"Júpiter"
    # ),

    # (
    #"¿En qué país se usó la primera bomba atómica?", 
    #["Colombia","Tokio","Japón","Siria"], 
    #"Tokio"
    # ),

    # (
    #"¿Quién pintó la Mona Lisa?", 
    #["Pablo Picasso", "Vincent van Gogh", "Leonardo da Vinci", "Michelangelo"],
    #"Leonardo da Vinci"
    # ),

    # (
    #"¿En qué continente se encuentra Egipto?", 
    #["Asia", "Europa", "África", "America"], 
    #"África"
    # ),

    # (
    #"¿Cuál es el océano más grande del mundo?", 
    #["Océano Atlántico", "Océano Índico", "Océano Pacífico", "Océano Antártico"], 
    #"Océano Atlántico"
    # ),

    # (
    #"¿Cuántos huesos hay en el cuerpo humano?", 
    #["205","224","206","215"], 
    #"206"
    # )
    # ]
#   ("¿En que país se encuentra Yucatán?", ["México","Francia","Estados Unidos","Brasil"], 0),
#     ("ES un país que está en Oceanía", ["Irán","China","Egipto","Nueva Zelanda"], 3),
#     ("¿Cuál es la ciudad de los rascacielos?", ["Dubai","Nueva York","Chicago","Tokio"], 1),
#     ("¿Cuál es el río más largo del mundo?", ["Nilo", "Amazonas", "Yangtsé", "Misisipi"], 1),
#     ("¿Cuál es el planeta más grande del sistema solar?", ["Venus", "Júpiter", "Marte", "Saturno"], 1),
#     ("¿En qué país se usó la primera bomba atómica?", ["Colombia","Tokio","Japón","Siria"], 2),
#     ("¿Quién pintó la Mona Lisa?", ["Pablo Picasso", "Vincent van Gogh", "Leonardo da Vinci", "Michelangelo"], 2),
#     ("¿En qué continente se encuentra Egipto?", ["Asia", "Europa", "África", "América"], 2),
#     ("¿Cuál es el océano más grande del mundo?", ["Océano Atlántico", "Océano Índico", "Océano Pacífico", "Océano Antártico"], 2),
#     ("¿Cuántos huesos hay en el cuerpo humano?", ["250","224","206","215"], 2)
#     ]

# Iterar a través de las preguntas, mostrar opciones y solicitar respuestas al usuario
for pregunta, opciones, respuesta in preguntas:
    print(pregunta)
    for i, opcion in enumerate(opciones):
        print(f"{i}) {opcion}")
   
    while True:
        try:
            respuesta_usuario = int(input("Elige la opción correcta: "))
            if 1 <= respuesta_usuario <= 4:
                break
            else:
                print("Por favor, elige una opción válida (0, 1, 2, 3).")
        except ValueError:
            print("Por favor, introduce un número válido.")

    if respuesta_usuario == respuesta:
        print("COREECTO")
        calificacion += 1
        aciertos += 1
    else:
        print("INCORRECTO")

# Mostrar la calificación y el número de aciertos
print("\nTu calificación final es:", calificacion, "de 10")
print("Número de aciertos:",aciertos)
      