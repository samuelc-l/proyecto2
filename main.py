import preguntas
class Trivial:
    preguntas_historia: dict
    preguntas_geografía: dict
    preguntas_arte_literatura: dict
    preguntas_ciencia_naturaleza: dict
    preguntas_deportes: dict
    preguntas_cine: dict

    def __init__(self, preguntas_historia, preguntas_geografía, preguntas_arte_literatura, preguntas_ciencia_naturaleza, preguntas_deportes, preguntas_cine):
        self.preguntas_historia = preguntas_historia
        self.preguntas_geografía = preguntas_geografía
        self.preguntas_arte_literatura = preguntas_arte_literatura
        self.preguntas_ciencia_naturaleza = preguntas_ciencia_naturaleza
        self.preguntas_deportes = preguntas_deportes
        self-preguntas_cine = preguntas_cine