import json
import random

class Biblioteca:
    categorias: list
    preguntas: dict

    def __init__(self):
        #Volcamos json en el constructor
        with open("preguntas.json", "r", encoding='utf-8') as archivo_preguntas:
            self.preguntas = json.load(archivo_preguntas)

        #Hacemos una lista con las categorías
        self.categorias = list(self.preguntas.keys())

    def elige_categoria_aleatoria(self):
        return random.choice(self.categorias)