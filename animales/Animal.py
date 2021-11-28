import random
import threading
from threading import Thread


class Animal(Thread):
    def __init__(self, id_animal, id_manada, simulacion, velocidad_animal, mi_casilla):
        threading.Thread.__init__(self)
        self.__id_animal = id_animal
        self.__id_manada = id_manada
        self.__simulacion = simulacion
        self.__velocidad_animal = velocidad_animal
        self.__mi_casilla = mi_casilla

    def mover(self):
        if self.__mi_casilla is not None:
            x = self.__mi_casilla.x
            y = self.__mi_casilla.y
            vector_desplazamiento = [-1, 0, 1]
            casillas_candidatas = []
            estado_entorno = ""
            for i in range(3):
                for j in range(3):
                    x_casilla_candidata = x + vector_desplazamiento[i]
                    y_casilla_candidata = y + vector_desplazamiento[j]
                    if 0 <= x_casilla_candidata < self.simulacion.entorno.dimensiones and 0 <= y_casilla_candidata < self.simulacion.entorno.dimensiones:
                        casilla_candidata = self.__simulacion.entorno.get_casilla(x_casilla_candidata,
                                                                                  y_casilla_candidata)
                        if not casilla_candidata.mutex.locked() and casilla_candidata.animal is None or casilla_candidata == self.__mi_casilla:
                            casillas_candidatas.append(casilla_candidata)
                            casilla_candidata.mutex.acquire()
            if len(casillas_candidatas) == 0 or self.simulacion.ganador.booleano:
                for casilla_candidata in casillas_candidatas:
                    casilla_candidata.mutex.release()
                return False
            else:
                i = random.randint(0, len(casillas_candidatas) - 1)
                casilla_donde_nos_desplazamos = casillas_candidatas[i]
                if self.__mi_casilla != casilla_donde_nos_desplazamos:
                    old_casilla = self.mi_casilla
                    self.__mi_casilla = casilla_donde_nos_desplazamos
                    casilla_donde_nos_desplazamos.animal = self
                    old_casilla.animal = None
                    estado_entorno += str(self) + "- Id. Ind = " + str(self.__id_animal) + "- Id. Manada = " + str(
                        self.__id_manada) + " se desplaza desde (" + str(old_casilla.x) + ", " + str(
                        old_casilla.y) + ") a (" + str(self.__mi_casilla.x) + ", " + str(
                        self.__mi_casilla.y) + ")\n"
                else:
                    estado_entorno += str(self) + "- Id. Ind = " + str(self.__id_animal) + "- Id. Manada = " + str(
                        self.__id_manada) + " se queda en (" + str(self.__mi_casilla.x) + ", " + str(
                        self.__mi_casilla.y) + ")\n"
                estado_entorno += str(self.simulacion.entorno)
                for casilla_candidata in casillas_candidatas:
                    casilla_candidata.mutex.release()
                print(estado_entorno)

    @property
    def id_animal(self):
        return self.__id_animal

    @property
    def id_manada(self):
        return self.__id_manada

    @property
    def simulacion(self):
        return self.__simulacion

    @property
    def velocidad_animal(self):
        return self.__velocidad_animal

    @property
    def mi_casilla(self):
        return self.__mi_casilla

    @id_animal.setter
    def id_animal(self, var_id_animal):
        self.__id_animal = var_id_animal

    @id_manada.setter
    def id_manada(self, var_id_manada):
        self.__id_manada = var_id_manada

    @velocidad_animal.setter
    def velocidad_animal(self, var_velocidad_animal):
        self.__velocidad_animal = var_velocidad_animal

    @mi_casilla.setter
    def mi_casilla(self, var_mi_casilla):
        self.__mi_casilla = var_mi_casilla
