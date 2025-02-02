import random

class Categoria:
    preguntas: list
    nombre_categoria: str

    def __init__(self, preguntas, nombre_categoria):
        self.preguntas = preguntas
        self.nombre_categoria = nombre_categoria

    def elige_pregunta(self):
        return random.choice(self.preguntas)