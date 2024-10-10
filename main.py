import logging
from src.controller.TrafficController import TrafficController
from src.controller.strategy.TrafficControlStrategy import BasicTrafficControlStrategy
from src.view.observer.TrafficLightViewObserver import TrafficLightView

if __name__ == "__main__":
    # Configuração do logger
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    logging.info('Iniciando o sistema de controle de tráfego.')

    controller = TrafficController(BasicTrafficControlStrategy(), TrafficLightView())

    controller.run()

    logging.info('Sistema finalizado.')