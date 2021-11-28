import threading
import random
from time import sleep

from Casilla import Casilla


class Entorno:
    def __init__(self):
        self.__entorno = None
        self.__size = 0
        self.__mutex_size = threading.Lock()

    def rellenar_entorno_con_casillas_vacias(self, dimensiones):
        self.__dimensiones = dimensiones
        self.__entorno = dimensiones * [None]
        for i in range(dimensiones):
            self.__entorno[i] = dimensiones * [None]
        for i in range(dimensiones):
            for j in range(dimensiones):
                self.__entorno[i][j] = Casilla(i, j, threading.Lock(), None)

    def __str__(self):
        if self.__entorno is None:
            return "None"
        else:
            cadena = 2 * " "
            for i in range(self.__dimensiones):
                cadena += str(i) + " "
            cadena += "\n"
            for i in range(self.__dimensiones):
                cadena += str(i) + " "
                for j in range(self.__dimensiones):
                    cadena += str(self.__entorno[i][j]) + " "
                cadena += "\n"
            return cadena

    def tiene_espacio(self):
        return self.__size < self.__dimensiones * self.__dimensiones

    def colocar_manada(self, manada):
        x = y = 0
        while self.tiene_espacio():
            x = random.randint(0, self.__dimensiones - 1)
            y = random.randint(0, self.__dimensiones - 1)
            if self.__entorno[x][y].animal is None:
                break
        for animal in manada.animales:
            if self.tiene_espacio():
                self.__entorno[x][y].animal = animal
                animal.mi_casilla = self.__entorno[x][y]
            else:
                break
            self.__size += 1
            while self.tiene_espacio():
                if y == self.__dimensiones - 1:
                    x = (x + 1) % self.__dimensiones
                y = (y + 1) % self.__dimensiones
                if self.__entorno[x][y].animal is None:
                    break
            print("Colocado " + str(animal) + "- Id Ind = " + str(animal.id_animal) + "- Id Manada = " + str(animal.id_manada) + " Pos: (" + str(animal.mi_casilla.x) + ", " + str(animal.mi_casilla.y) + ")")
        print()
        print(self.__str__())

    def colocar_animal(self, animal):
        x = y = 0
        while self.tiene_espacio():
            x = random.randint(0, self.__dimensiones - 1)
            y = random.randint(0, self.__dimensiones - 1)
            if self.__entorno[x][y].animal is None:
                break
        if self.tiene_espacio():
            self.__entorno[x][y].animal = animal
            animal.mi_casilla = self.__entorno[x][y]
            self.__size += 1

    def get_casilla(self, x, y):
        return self.__entorno[x][y]

    def decrementar_size(self):
        while self.__mutex_size.locked():
            sleep(0.1)
        self.__mutex_size.acquire()
        self.__size -= 1
        self.__mutex_size.release()

    @property
    def dimensiones(self):
        return self.__dimensiones
