class Pregunta:
    enunciado: str
    respuesta_usuario: str
    respuesta_correcta: str

    def __init__(self, enunciado, respuesta_usuario, respuesta_correcta):
        self.enunciado = enunciado
        self.respuesta_usuario = respuesta_usuario
        self.respuesta_correcta = respuesta_correcta

    def es_correcta(self):
        
        if self.respuesta_usuario == self.respuesta_correcta:
            print("Correcto")
        else:
            print("Incorrecto")
