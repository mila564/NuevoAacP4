class Manada:
    def __init__(self, id_manada, lista_animales, puntuacion, velocidad_manada):
        self.__id_manada = id_manada
        self.__animales = lista_animales
        self.__puntuacion = puntuacion
        self.__velocidad_manada = velocidad_manada

    def agregar_animal(self, animal):
        self.__animales.append(animal)

    def __str__(self):
        print("Manada " + str(self.__id_manada))

    @property
    def id_manada(self):
        return self.__id_manada

    @id_manada.setter
    def id_manada(self, id_man):
        self.__id_manada = id_man

    @property
    def animales(self):
        return self.__animales

    @animales.setter
    def animales(self, lista_anim):
        self.__animales = lista_anim

    @property
    def puntuacion(self):
        return self.__puntuacion

    @puntuacion.setter
    def puntuacion(self, var_puntuacion):
        self.__puntuacion = var_puntuacion

    @property
    def velocidad_manada(self):
        return self.__velocidad_manada

    @velocidad_manada.setter
    def velocidad_manada(self, velocidad_manada):
        self.__velocidad_manada = velocidad_manada