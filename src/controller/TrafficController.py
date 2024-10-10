import logging
import math
from time import sleep

from src.model.CorSemaforo import CorSemaforo
from src.model.Via import Via
from src.view.TrafficLightView import TrafficLightView


class TrafficController:
    def __init__(self):
        self.logger = logging.getLogger('TrafficController')

    def run(self):
        via_1 = Via("via 1")
        via_2 = Via("via 2")
        execucao = 5

        TrafficLightView.exibe_infos_vias(self, via_1, via_2)

        for i in range(execucao):
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
            TrafficLightView.exibe_infos_vias(self,via_1, via_2)
            sleep(3)



