import json
import random
class Trivial:
    clase_preguntas: list
    preguntas: dict
    
    def __init__(self):
        #Volcamos el json en el constructor
        with open("preguntas.json", "r", encoding='utf-8') as archivo_preguntas:
            self.preguntas = json.load(archivo_preguntas)
        print(self.preguntas)

        #Hacemos una lista con las clases de preguntas
        self.clase_preguntas = list(self.preguntas.keys())
        
    def formula_pregunta(self):
        aleatorio = random.randint(0, 5)
        print("Te ha tocado pregunta sobre:", self.clase_preguntas[aleatorio])

        


            

        

trivial = Trivial()
#trivial.formula_pregunta()
