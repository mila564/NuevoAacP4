import random
from time import sleep

from animales.Carnivoro import Carnivoro
from animales.Cebra import Cebra


class Hiena(Carnivoro):
    def __init__(self, id_animal, id_manada, simulacion, velocidad_animal, mi_casilla, cazado):
        super().__init__(id_animal, id_manada, simulacion, velocidad_animal, mi_casilla)
        self.__cazado = cazado

    @property
    def cazado(self):
        return self.__cazado

    @cazado.setter
    def cazado(self, var_booleano):
        self.__cazado = var_booleano

    def run(self):
        descansar = 10
        while not self.__cazado and not self.simulacion.ganador.booleano:
            self.mover()
            caze = self.cazar()
            if not caze and not self.simulacion.ganador.booleano:
                self.mover()
            if descansar == 0:
                tiempo_descanso = random.randint(1, 2)
                sleep(tiempo_descanso)
                descansar = 10
            else:
                sleep(abs(75 - self.velocidad_animal))
                descansar -= 1

    def cazar(self):
        if self.mi_casilla is not None:
            x = self.mi_casilla.x
            y = self.mi_casilla.y
            vector_desplazamiento = [-1, 0, 1]
            casillas_candidatas = []
            manada_animal = self.simulacion.get_manada(self.id_manada)
            mutex_puntuacion = manada_animal.puntuacion.mutex
            mutex_ganador = self.simulacion.ganador.mutex
            estado_entorno = ""
            for i in range(3):
                for j in range(3):
                    x_casilla_candidata = x + vector_desplazamiento[i]
                    y_casilla_candidata = y + vector_desplazamiento[j]
                    if 0 <= x_casilla_candidata < self.simulacion.entorno.dimensiones and 0 <= y_casilla_candidata < self.simulacion.entorno.dimensiones:
                        casilla_candidata = self.simulacion.entorno.get_casilla(x_casilla_candidata,
                                                                                y_casilla_candidata)
                        if casilla_candidata is not None and not casilla_candidata.mutex.locked() and (
                                isinstance(casilla_candidata.animal, Cebra) and self.superioridad_numerica()):
                            casillas_candidatas.append(casilla_candidata)
                            casilla_candidata.mutex.acquire()
            if len(casillas_candidatas) == 0 or self.simulacion.ganador.booleano:
                for casilla_candidata in casillas_candidatas:
                    casilla_candidata.mutex.release()
                return False
            else:
                self.mi_casilla.mutex.acquire()
                i = random.randint(0, len(casillas_candidatas) - 1)
                casilla_donde_cazamos = casillas_candidatas[i]
                old_casilla = self.mi_casilla
                animal_cazado = casilla_donde_cazamos.animal
                self.mi_casilla = casilla_donde_cazamos
                casilla_donde_cazamos.animal.cazado = True
                casilla_donde_cazamos.animal = self
                old_casilla.animal = None
                self.simulacion.decrementar_size_entorno()
                for casilla_candidata in casillas_candidatas:
                    casilla_candidata.mutex.release()
                old_casilla.mutex.release()
                while mutex_puntuacion.locked():
                    sleep(0.01)
                mutex_puntuacion.acquire()
                manada_animal.puntuacion.puntos += 1
                mutex_puntuacion.release()
                estado_entorno += str(self) + " - Id. Ind = " + str(self.id_animal) + " - Id. Manada = " + str(
                    self.id_manada) + " caza desde (" + str(old_casilla.x) + ", " + str(
                    old_casilla.y) + ") al animal " + str(
                    animal_cazado) + " - Id. Ind = " + str(
                    animal_cazado.id_animal) + " - Id. Manada = " + str(
                    animal_cazado.id_manada) + " situado en (" + str(
                    self.mi_casilla.x) + ", " + str(
                    self.mi_casilla.y) + ") obteniéndose " + str(
                    manada_animal.puntuacion.puntos) + " punto/s\n"
                if manada_animal.puntuacion.puntos >= 20:
                    while mutex_ganador.locked():
                        sleep(0.01)
                    mutex_ganador.acquire()
                    self.simulacion.ganador.booleano = True
                    estado_entorno += "Manada con Id = " + str(manada_animal.id_manada) + " ganadora\n"
                    estado_entorno += "Lista de animales pertenecientes a la misma: \n"
                    for animal in manada_animal.animales:
                        estado_entorno += str(animal) + " - Id. Ind = " + str(animal.id_animal) + "\n"
                    mutex_ganador.release()
                if isinstance(animal_cazado, Cebra):
                    manada_cazada = self.simulacion.get_manada(animal_cazado.id_manada)
                    animal_creado = self.simulacion.crear_cebra(manada_cazada)
                    if animal_creado.mi_casilla is None:
                        estado_entorno += "Se ha generado " + str(animal_creado) + "- Id. Ind = " + str(
                            animal_creado.id_animal) + " - Id. Manada = " + str(
                            animal_creado.id_manada) + " y no se coloca en ningún sitio\n"
                    else:
                        estado_entorno += "Se ha generado " + str(animal_creado) + "- Id. Ind = " + str(
                            animal_creado.id_animal) + " - Id. Manada = " + str(
                            animal_creado.id_manada) + " y se coloca en (" + str(
                            animal_creado.mi_casilla.x) + ", " + str(
                            animal_creado.mi_casilla.y) + ")\n"
                estado_entorno += str(self.simulacion.entorno)
                print(estado_entorno)
                return True

    def superioridad_numerica(self):
        if self.mi_casilla is not None:
            x = self.mi_casilla.x
            y = self.mi_casilla.y
            vector_desplazamiento = [-1, 0, 1]
            num_hienas = num_cebras = 0
            for i in range(3):
                for j in range(3):
                    x_casilla_candidata = x + vector_desplazamiento[i]
                    y_casilla_candidata = y + vector_desplazamiento[j]
                    if 0 <= x_casilla_candidata < self.simulacion.entorno.dimensiones and 0 <= y_casilla_candidata < self.simulacion.entorno.dimensiones:
                        casilla_candidata = self.simulacion.entorno.get_casilla(x_casilla_candidata,
                                                                                y_casilla_candidata)
                        if casilla_candidata.animal is not None:
                                if isinstance(casilla_candidata.animal, Hiena):
                                    num_hienas += 1
                                elif isinstance(casilla_candidata.animal, Cebra):
                                    num_cebras += 1
            return num_hienas >= num_cebras

    def __str__(self):
        return "H"
