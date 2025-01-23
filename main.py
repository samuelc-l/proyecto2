import json
import random
class Trivial:
    clase_preguntas: list
    preguntas: dict
    
    def __init__(self):
        #Volcamos el json en el constructor
        with open("preguntas.json", "r", encoding='utf-8') as archivo_preguntas:
            self.preguntas = json.load(archivo_preguntas)
        

        #Hacemos una lista con las clases de preguntas
        self.clase_preguntas = list(self.preguntas.keys())
        
    def formula_pregunta(self):
        try:
            #Generamos un número aleatorio
            aleatorio = random.randint(0, 5)
            #Utilizamos dicho número para elegir aleatoriamente una categoría de pregunta
            clase = self.clase_preguntas[aleatorio]
            print("Te ha tocado pregunta sobre:", clase)
                
            #Pasamos el diccionario a lista para poder mostrar la primera pregunta
            pregunta = list(self.preguntas[clase].keys())[0]
            print(pregunta)

            #Pedimos al jugador la respuesta a la pregunta
            respuesta = input()

            #Comparamos si la respuesta introducida por el usuario es correcta
            if respuesta.lower() == self.preguntas[clase][pregunta].lower():
                print("Correcto")
            else:
                print("Incorrecto")

            #Una vez mostrada la pregunta la eliminamos del diccionario para que no se repitan las preguntas
            del self.preguntas[clase][pregunta]
        except IndexError:
            print("Nos hemos quedado sin preguntas seguiremos mejorando el juego, Lo siento :(")
        

            

trivial = Trivial()
for i in range(5):
    trivial.formula_pregunta()
