import random
import logging

from src.model.CorSemaforo import CorSemaforo
from src.model.Semaforo import Semaforo

class Via:
    def __init__(self, nome: str):
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
        self.logger = logging.getLogger()
        self.nome = nome
        self.qtd_veiculos = random.randint(5, 20)
        self.semaforo = Semaforo()

    def aumentar_congestionamento(self):
        self.qtd_veiculos += random.randint(1, 5)

    def diminuir_congestionamento(self):
        self.qtd_veiculos = max(0, self.qtd_veiculos - random.randint(1, 5))

    def atualiza_via(self):
        if self.semaforo.status == CorSemaforo.VERDE:
            self.diminuir_congestionamento()
        else:
            self.aumentar_congestionamento()