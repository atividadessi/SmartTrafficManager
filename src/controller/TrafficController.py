import logging
from time import sleep

from src.controller.strategy.TrafficControlStrategy import TrafficControlStrategy
from src.model.Via import Via
from src.view.observer.TrafficLightViewObserver import TrafficLightViewObserver


class TrafficController:
    def __init__(self, strategy: TrafficControlStrategy, view: TrafficLightViewObserver):
        self.logger = logging.getLogger('TrafficController')
        self.strategy = strategy
        self.view = view

    def run(self):
        via_1 = Via("via 1")
        via_2 = Via("via 2")
        execucao = 5

        self.view.update(via_1, via_2)

        for i in range(execucao):
            self.strategy.control_traffic(via_1, via_2)
            self.view.update(via_1, via_2)
            sleep(via_1.semaforo.time)