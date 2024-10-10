from src.model.CorSemaforo import CorSemaforo


class Semaforo:
    def __init__(self):
        self.status = CorSemaforo.VERMELHO
        self.time = 5

    def atualizar_semaforo(self, color: CorSemaforo):
        self.status = color