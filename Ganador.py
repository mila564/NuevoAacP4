class Ganador:
    def __init__(self, booleano, mutex):
        self.__booleano = booleano
        self.__mutex = mutex

    @property
    def booleano(self):
        return self.__booleano

    @property
    def mutex(self):
        return self.__mutex

    @booleano.setter
    def booleano(self, var_booleano):
        self.__booleano = var_booleano

    @mutex.setter
    def mutex(self, var_mutex):
        self.__mutex = var_mutex