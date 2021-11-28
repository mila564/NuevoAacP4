class Puntuacion:
    def __init__(self, puntos, mutex):
        self.__puntos = puntos
        self.__mutex = mutex

    @property
    def puntos(self):
        return self.__puntos

    @property
    def mutex(self):
        return self.__mutex

    @puntos.setter
    def puntos(self, var_puntos):
        self.__puntos = var_puntos

    @mutex.setter
    def mutex(self, var_mutex):
        self.__mutex = var_mutex
