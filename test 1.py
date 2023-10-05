puntaje = 0
# aqui va las preguntas, opciones y respuesta

pregunta = {
    
    {
    "pregunta:" "1.¿Cuándo acabó la II Guerra Mundial?",
    "opciones:" ["1939","1918", "1945","1946"],
    "respuesta:" "1945"
    },

    {
    "pregunta:" "2.¿En qué país se usó la primera bomba atómica?"
    "opciones:" ["lala", "lelele", "lilili"],
    "respuesta" "lala"
    }
}

# funcion par arealizar el examen
# def realiza examen(pregunta):
# codigo
for registro in pregunta: 
    puntos = 0

# organizacion de las preguntas, opciones y que nos de la respuesta
    print   [registro ("pregunta")]
    posicion = 0
    for opcion in registro ("opciones"):
        print(posicion, opcion)
        posicion += 1
    
respuesta = int(input["dame la respuesta"])
    
print ("Tu respuesta: ", respuesta, "respuesta correcta", registro["respuesta"])
if (respuesta == registro ["respuesta"]):
        puntos += 1

# para sacar la caificacion
calificacion = puntos / len(pregunta) * 100
print ("calificacion: ", puntos)

