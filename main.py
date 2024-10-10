import logging
from src.controller.TrafficController import TrafficController

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    logging.info('Iniciando o sistema de controle de tráfego.')

    # Tempo de simulação em segundos
    controller = TrafficController()
    controller.run()



    logging.info('Sistema finalizado.')
