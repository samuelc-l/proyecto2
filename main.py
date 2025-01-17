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
    
    def pregunta_nueva(self):
        self.preguntas_historia = {
                        "¿En qué año comenzó la primera guerra mundial?": "1914",
                        "¿Qué tratado puso fin a la Primera Guerra Mundial?": "Tratado de Versalles",
                        "¿En qué año comenzó la Revolución Francesa?": "1789",
                        "¿Qué civilización antigua construyó Machu Picchu?": "Inca",
                        "¿Quién fue el primer presidente de los Estados Unidos?": "George Washington",
                        "¿Cuál fue el primer país en llegar al espacio?": "Unión Soviética",
                        "¿Quién descubrió América en 1492?": "Cristóbal Colón",
                        "¿Quién pintó la Capilla Sixtina?": "Miguel Ángel",
                        "¿En qué año se firmó la Declaración de Independencia de los Estados Unidos?": "1776",
                        "¿En qué año comenzó la Segunda Guerra Mundial?": "1939"
                    }

        self.preguntas_geografía = {
                        "¿Cúal es la capital de Moldavia?": "Chisinau",
                        "¿De que país es capital La Valeta": "Chipre",
                        "¿Cúal es el nombre del río más largo del mundo?": "Amazonas",
                        "¿Cúal es el nombre de la montaña más alta del mundo?": "Everest",
                        "¿Cúal es el nombre del océano más grande de la Tierra?": "Pacífico",
                        "¿Cuál es el país más extenso del mundo?": "Rusia",
                        "¿Cuál es el país con mayor población del mundo?": "India",
                        "¿Cúal es el nombre del desierto más grande del mundo?": "Sahara",
                        "¿Cuántos continentes hay en la Tierra?": "7",
                        "¿Cúal es el nombre del río más largo de España?": "Ebro"
                    }
        self.preguntas_arte_literatura = {
                        ""
                    }
        
        self.preguntas_ciencia_naturaleza = {
                        "¿Cómo se llama el proceso por el cual las plantas convierten la luz solar en energía química?": "Fotosíntesis",
                        "Cómo se llama el gas más abundante en la atmósfera terrestre?": "Nitrógeno",
                        "¿Cómo se llama el proceso por el cual el agua pasa de estado líquido a gaseoso?": "Evaporación",
                        "¿Cómo se llama la capa de la atmósfera terrestre donde se encuentra la capa de ozono?": "Estratosfera",
                        "¿Cómo se llama la rama de la biología que estudia la herencia y la variación de los caracteres biológicos?": "Genética",
                        "¿Cómo se llama la unidad de medida de la fuerza en el Sistema Internacional de Unidades?": "Newton",
                        "¿Cómo se llama la ciencia que estudia los seres vivos, incluyendo su origen, evolución, estructura, función y relaciones con el medio ambiente?": "Biología",
                        "¿Cómo se llama la adaptación de algunos animales para pasar el invierno en un estado de inactividad, con un metabolismo muy lento?": "Hibernación",
                        "¿Cómo se llama la parte del átomo con carga positiva que se encuentra en el núcleo?": "Protón",
                        "¿Cómo se llama el conjunto de todos los seres vivos que habitan la Tierra, junto con los ecosistemas en los que viven?": "Biosfera"
                    }
        
        self.preguntas_deportes = {
                        ""
                    }
        
        self.preguntas_cine = {
                        ""
                    }