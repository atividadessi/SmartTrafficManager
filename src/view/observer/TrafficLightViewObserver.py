import logging
from abc import ABC, abstractmethod

from src.model.Via import Via


class TrafficLightViewObserver(ABC):
    @abstractmethod
    def update(self, *vias: Via):
        pass

    def __init__(self):
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
        self.logger = logging.getLogger()

class TrafficLightView(TrafficLightViewObserver):
    def update(self, *vias: Via):
        for via in vias:
            self.logger.info(f'{via.nome}: Sinal {via.semaforo.status.value} por {via.semaforo.time} segundos. Veiculos restantes: {via.qtd_veiculos}')
        self.logger.info("-------------------------------------------------------------")
