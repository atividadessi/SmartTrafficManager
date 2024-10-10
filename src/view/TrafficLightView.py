import logging
from typing import List

from src.model.Via import Via


class TrafficLightView:
    def __init__(self):
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
        self.logger = logging.getLogger()

    def exibe_infos_vias(self, *vias: Via):
        # self.logger.info(f"--- Estado atual das vias -- ")
        for via in vias:
            self.logger.info(f'{via.nome}: Sinal {via.semaforo.status.value} por {via.semaforo.time} segundos. Veiculos restantes: {via.qtd_veiculos}')
        self.logger.info("-------------------------------------------------------------")
