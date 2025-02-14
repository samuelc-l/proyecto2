import json
import random
from categoria import Categoria
from pregunta import Pregunta

class Biblioteca:
    categorias: list
    preguntas: dict

    def __init__(self):
        self.categorias = []

        #Volcamos json en el constructor
        with open("preguntas.json", "r", encoding='utf-8') as archivo_preguntas:
            self.preguntas = json.load(archivo_preguntas)

        for categoria in self.preguntas.keys():
            c = Categoria(categoria)
            for pregunta in self.preguntas[categoria]:
                p = Pregunta(pregunta, self.preguntas[categoria][pregunta])
                c.añade_pregunta(p)
            self.categorias.append(c)

            

    def elige_categoria_aleatoria(self):
        return random.choice(self.categorias)
    
if __name__ == "__main__":
    b = Biblioteca()
    categoria = b.elige_categoria_aleatoria()
    print(categoria.elige_pregunta().enunciado)