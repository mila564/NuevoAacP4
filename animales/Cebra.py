import random
from time import sleep

from animales.Animal import Animal


class Cebra(Animal):
    def __init__(self, id_animal, id_manada, simulacion, velocidad_animal, mi_casilla, cazado):
        super().__init__(id_animal, id_manada, simulacion, velocidad_animal, mi_casilla)
        self.__cazado = cazado
        self.__recien_creada = True

    @property
    def cazado(self):
        return self.__cazado

    @cazado.setter
    def cazado(self, var_booleano):
        self.__cazado = var_booleano

    def run(self):
        descansar = 15
        esperar_a_moverse = 5
        while not self.__cazado and not self.simulacion.ganador.booleano:
            if self.__recien_creada:
                if esperar_a_moverse == 0:
                    self.__recien_creada = False
                else:
                    esperar_a_moverse -= 1
            if esperar_a_moverse == 0:
                self.mover()
            if descansar == 0:
                tiempo_descanso = random.randint(1, 2)
                sleep(tiempo_descanso)
                descansar = 15
            else:
                sleep(abs(65 - self.velocidad_animal))
                descansar -= 1

    def __str__(self):
        return "C"
