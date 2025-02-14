class Pregunta:
    enunciado: str
    respuesta_correcta: str

    def __init__(self, enunciado, respuesta_correcta):
        self.enunciado = enunciado
        self.respuesta_correcta = respuesta_correcta

    def es_correcta(self, respuesta_usuario):
        
        if respuesta_usuario == self.respuesta_correcta:
            return True
        else:
            return False


   