import logging

class TrafficLight:
    def __init__(self):
        self.logger = logging.getLogger('TrafficLight')
        self.logger.info('Semáforo iniciado.')