import math
from abc import ABC, abstractmethod

from src.model.CorSemaforo import CorSemaforo


class TrafficControlStrategy(ABC):
    @abstractmethod
    def control_traffic(self, via_1, via_2):
        pass

class BasicTrafficControlStrategy(TrafficControlStrategy):
    def control_traffic(self, via_1, via_2):
        if via_1.qtd_veiculos > via_2.qtd_veiculos:
            via_1.semaforo.atualizar_semaforo(CorSemaforo.VERDE)
            via_1.semaforo.time = math.ceil(via_1.qtd_veiculos * 0.3)
            for time in range(via_1.semaforo.time):
                via_1.diminuir_congestionamento()

            via_2.aumentar_congestionamento()
            via_2.semaforo.atualizar_semaforo(CorSemaforo.VERMELHO)
        else:
            via_2.semaforo.atualizar_semaforo(CorSemaforo.VERDE)
            via_2.semaforo.time = math.ceil(via_2.qtd_veiculos * 0.3)
            for time in range(via_2.semaforo.time):
                via_2.diminuir_congestionamento()

            via_1.aumentar_congestionamento()
            via_1.semaforo.atualizar_semaforo(CorSemaforo.VERMELHO)
