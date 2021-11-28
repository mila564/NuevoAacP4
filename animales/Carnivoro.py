from abc import abstractmethod, ABC

from animales.Animal import Animal


class Carnivoro(ABC, Animal):
    @abstractmethod
    def cazar(self):
        pass