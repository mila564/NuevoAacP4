import random
import threading

from Entorno import Entorno
from Ganador import Ganador
from Manada import Manada
from Puntuacion import Puntuacion
from animales.Cebra import Cebra
from animales.Hiena import Hiena
from animales.Leon import Leon


class Simulacion:
    def __init__(self):
        self.__entorno = Entorno()
        self.__ganador = Ganador(False, threading.Lock())
        self.__animales = []
        self.__contador_animales = 0
        self.__contador_manadas = 0
        self.__manadas = {}

    def iniciar_entorno(self, dimensiones):
        self.__entorno.rellenar_entorno_con_casillas_vacias(dimensiones)

    def iniciar_animales(self, num_leones, num_hienas, num_cebras, num_manadas_leones, num_manadas_hienas,
                      num_manadas_cebras):
        # Declaramos las listas de manadas por cada especie
        manadas_leones = []
        manadas_hienas = []
        manadas_cebras = []
        # Inicializamos las manadas de cada especie
        self.inicializar_manadas(manadas_leones, num_manadas_leones, 0)
        self.inicializar_manadas(manadas_hienas, num_manadas_hienas, 1)
        self.inicializar_manadas(manadas_cebras, num_manadas_cebras, 2)
        # Se asignan animales a las diferentes manadas
        self.crear_manadas(manadas_leones, num_leones, num_manadas_leones, 0)
        self.crear_manadas(manadas_hienas, num_hienas, num_manadas_hienas, 1)
        self.crear_manadas(manadas_cebras, num_cebras, num_manadas_cebras, 2)
        # Se reparten los animales en las casillas del entorno
        self.colocar_animales(manadas_cebras, manadas_hienas, manadas_leones, num_manadas_cebras, num_manadas_hienas,
                              num_manadas_leones)

    def inicializar_manadas(self, lista_manadas, num_manadas, id_tipo_animal):
        for i in range(num_manadas):
            if id_tipo_animal == 0:  # león
                velocidad_manada = random.randint(80, 90)
            elif id_tipo_animal == 1:  # hiena
                velocidad_manada = random.randint(50, 60)
            else:  # cebra
                velocidad_manada = random.randint(55, 65)
            manada = Manada(self.__contador_manadas, [], Puntuacion(0, threading.Lock()), velocidad_manada)
            lista_manadas.append(manada)
            self.__manadas[manada.id_manada] = manada
            self.__contador_manadas += 1

    def crear_manadas(self, lista_manadas, num_individuos, num_manadas, id_tipo_animal):
        j = 0
        for i in range(num_individuos):
            vel_manada = lista_manadas[j].velocidad_manada
            id_manada = lista_manadas[j].id_manada
            if id_tipo_animal == 0:  # león
                vel_propia = vel_manada + random.randint(-10, 10)
                animal = Leon(self.__contador_animales, id_manada, self, vel_propia, None)
            elif id_tipo_animal == 1:  # hiena
                vel_propia = vel_manada + random.randint(-10, 10)
                animal = Hiena(self.__contador_animales, id_manada, self, vel_propia, None, False)
            else:  # cebra
                vel_propia = vel_manada + random.randint(-10, 10)
                animal = Cebra(self.__contador_animales, id_manada, self, vel_propia, None, False)
            lista_manadas[j].animales.append(animal)
            self.__animales.append(animal)
            j = (j + 1) % num_manadas
            self.__contador_animales += 1

    def colocar_animales(self, manadas_cebras, manadas_hienas, manadas_leones, num_manadas_cebras, num_manadas_hienas,
                         num_manadas_leones):
        i = 0
        while (self.__entorno.tiene_espacio() and i < num_manadas_hienas
               or i < num_manadas_leones or i < num_manadas_cebras):
            if i < num_manadas_leones:
                self.__entorno.colocar_manada(manadas_leones[i])
            if i < num_manadas_hienas:
                self.__entorno.colocar_manada(manadas_hienas[i])
            if i < num_manadas_cebras:
                self.__entorno.colocar_manada(manadas_cebras[i])
            i += 1

    def lanzar_simulacion(self):
        for animal in self.__animales:
            animal.start()
        for animal in self.__animales:
            animal.join()

    def get_manada(self, id_manada):
        return self.__manadas.get(id_manada)

    def crear_cebra(self, manada_cazada):
        vel_propia = manada_cazada.velocidad_manada + random.randint(-2, 2)
        animal_creado = Cebra(self.__contador_animales, manada_cazada.id_manada, self, vel_propia, None, False)
        self.__contador_animales += 1
        self.entorno.colocar_animal(animal_creado)
        manada_cazada.agregar_animal(animal_creado)
        animal_creado.start()
        return animal_creado

    def decrementar_size_entorno(self):
        self.__entorno.decrementar_size()

    @property
    def entorno(self):
        return self.__entorno

    @property
    def ganador(self):
        return self.__ganador

    @property
    def contador_animales(self):
        return self.__contador_animales


