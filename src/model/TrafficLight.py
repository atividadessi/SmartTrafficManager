import logging
import random
from enum import Enum


class Color(Enum):
    VERDE = "verde"
    VERMELHO = "vermelho"
    AMARELO = "amarelo"

class Semaforo:

    def __init__(self, via):
        self.via = via
        self.status = Color.VERMELHO
        self.time = 5

