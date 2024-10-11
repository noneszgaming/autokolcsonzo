#External
from abc import ABC, abstractmethod
from enum import Enum


class AutoMarka(Enum):
    TOYOTA = 1
    HONDA = 2
    FORD = 3
    BMW = 4
    MERCEDES = 5
    AUDI = 6
    VOLKSWAGEN = 7
    TESLA = 8
    NISSAN = 9
    CHEVROLET = 10
    VOLVO = 11
    SEAT = 12
    SCANIA = 13
    CITROEN = 14
    OPEL = 15
    IVECO = 16
    MAN = 17
    SKODA = 18
    RENAULT = 19


class Auto(ABC):
    def __init__(self, rendszam, marka: AutoMarka, berleti_dij):
        self.rendszam = rendszam
        self.marka = marka
        self.berleti_dij = berleti_dij

    @abstractmethod
    def __str__(self):
        pass
