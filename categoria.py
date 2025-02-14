import random
from pregunta import Pregunta

class Categoria:
    preguntas: list [Pregunta]
    nombre_categoria: str

    def __init__(self, nombre_categoria):
        self.preguntas = []
        self.nombre_categoria = nombre_categoria

    def elige_pregunta(self):
        return random.choice(self.preguntas)
    
    def añade_pregunta(self, pregunta):
        self.preguntas.append(pregunta)