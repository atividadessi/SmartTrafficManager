import math
from abc import ABC, abstractmethod

from src.model.CorSemaforo import CorSemaforo


class SemaforoState(ABC):
    @abstractmethod
    def handle(self, semaforo):
        pass


class SemaforoVerde(SemaforoState):
    def handle(self, semaforo):
        semaforo.cor = CorSemaforo.VERDE
        semaforo.time = math.ceil(semaforo.via.qtd_veiculos * 0.2)
        semaforo.via.diminuir_congestionamento()

class SemaforoVermelho(SemaforoState):
    def handle(self, semaforo):
        semaforo.cor = CorSemaforo.VERMELHO
        semaforo.via.aumentar_congestionamento()