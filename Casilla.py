class Casilla:
    def __init__(self, x, y, mutex, animal):
        self.__x = x
        self.__y = y
        self.__mutex = mutex
        self.__animal = animal

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def mutex(self):
        return self.__mutex

    @property
    def animal(self):
        return self.__animal

    @x.setter
    def x(self, var_x):
        self.__x = var_x

    @y.setter
    def y(self, var_y):
        self.__y = var_y

    @mutex.setter
    def mutex(self, var_mutex):
        self.__mutex = var_mutex

    @animal.setter
    def animal(self, var_animal):
        self.__animal = var_animal

    def __str__(self):
        contenido_casilla = self.__animal
        if contenido_casilla is None:
            return "N"
        else:
            return str(contenido_casilla)
